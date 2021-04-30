from common.custom.models import *
from celery.result import AsyncResult
from celery import states
from kombu.utils.encoding import safe_repr
from celery.utils import get_full_cls_name


class Resource(models.Model):
    type = models.IntegerField(default=1)
    path = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Uploader(models.Model):
    uploader_id = models.CharField(max_length=32, unique=True)
    uploader = models.CharField(max_length=255, default='', db_index=True)
    uploader_url = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    video_id = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    upload_date = models.DateField(null=True)
    # 定义关联
    uploader = models.ForeignKey("Uploader", on_delete=models.SET_NULL, to_field="uploader_id", null=True)
    duration = models.IntegerField(null=True)
    view_count = models.IntegerField(null=True)
    average_rating = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    age_limit = models.IntegerField(null=True)
    like_count = models.IntegerField(null=True)
    dislike_count = models.IntegerField(null=True)
    video_resource = models.ForeignKey("Resource", related_name="video_resource_set",
                                       on_delete=models.SET_NULL, null=True)
    thumbnail_resource = models.ForeignKey("Resource", related_name="thumbnail_resource_set",
                                           on_delete=models.SET_NULL, null=True)
    channel_id = models.CharField(max_length=32, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def task_id(self):  # 可以在serializers中获取到该参数
        job = JobRelation.objects.filter(model=self._meta.__str__(), model_id=self.id).first()

        return job.task_id if job else None

    @property
    def task_progress(self):
        task_id = self.task_id
        if task_id is None:
            return None

        result = AsyncResult(task_id)
        state, retval = result.state, result.result
        data = {'id': task_id, 'status': state, 'result': retval}
        if state in states.EXCEPTION_STATES:
            traceback = result.traceback
            data.update(
                {'result': safe_repr(retval), 'exc': get_full_cls_name(retval.__class__), 'traceback': traceback}
            )
        return data

    @classmethod
    def task_type(cls):
        return cls._meta.__str__()


class VideoFormat(models.Model):
    video = models.ForeignKey("Video", related_name="video_format_set",
                              on_delete=models.CASCADE, to_field="video_id", null=True)
    format_id = models.CharField(max_length=32)
    asr = models.IntegerField(null=True)
    filesize = UnsignedBigIntegerField(null=True)
    format_note = models.CharField(max_length=255, null=True)
    fps = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    quality = models.IntegerField(null=True)
    ext = models.CharField(max_length=32, null=True)
    resource = models.ForeignKey("Resource", related_name='video_format_resource_set',
                                 on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('video_id', 'format_id',)
        db_table = "youtube_video_format"

    @classmethod
    def task_type(cls):
        return cls._meta.__str__()


class VideoThumbnail(models.Model):
    video = models.ForeignKey("Video", related_name='video_thumbnail_set', on_delete=models.CASCADE, to_field="video_id", null=True)
    thumbnail_id = models.CharField(max_length=32)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    resolution = models.IntegerField(null=True)
    resource = models.ForeignKey("Resource", related_name='video_thumbnail_resource_set',
                                 on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('video_id', 'thumbnail_id',)
        db_table = "youtube_video_thumbnail"


class JobRelation(models.Model):
    model = models.CharField(max_length=255)
    model_id = UnsignedBigIntegerField()
    task_id = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('model', 'model_id')
        db_table = "youtube_job_relation"


class Keyword(models.Model):
    keyword = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    video_set = models.ManyToManyField(to="Video", through='KeywordVideo')


class KeywordVideo(models.Model):
    video = models.ForeignKey(to="Video", related_name="video_keyword_set",
                              on_delete=models.CASCADE, to_field="video_id")
    keyword = models.ForeignKey(to="Keyword", related_name="video_keyword_set", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('video_id', 'keyword_id')
        db_table = "youtube_keyword_video"
