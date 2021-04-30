## 安装扩展

```
pip3 install -r requirements.txt
```

## 配置环境变量
```
cp .env.example .env
```

## 启动web服务
```
python manage.py runserver
```

## 启动celery异步任务服务

```
 celery -A videos worker -l INFO
```

## 接口文档：
http://localhost:8000/swagger/


#### 未解决问题

- drf_yasg 文档 auth 鉴权不生效，不能测试登陆限制接口