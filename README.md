Python Flask 小程序订餐系统
=====================
##启动
* export ops_config=local|production && python manage.py runserver

##flask-sqlacodegen

    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
    flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/user.py"  --flask



##可参考资料
* [python-Flask（jinja2）语法：过滤器](https://www.jianshu.com/p/3127ac233518)
* [SQLAlchemy 各种查询语句写法](https://wxnacy.com/2017/08/14/python-2017-08-14-sqlalchemy-filter/)
我的博客 https://www.cnblogs.com/crazymagic/p/9716546.html
