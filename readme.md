Python Flask订餐系统
=====================
##启动
* export ops_config=local|production && python manage.py runserver

##flask-sqlacodegen

        flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
        flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/user.py"  --flask

 domain:"http://172.16.140.105:5000/api"


flask-sqlacodegen 'mysql://root:mysql@127.0.0.1/food_db' --tables app_access_log --outfile "common/log/AppAccessLog.py"  --flask


flask-sqlacodegen 'mysql://root:mysql@127.0.0.1/food_db' --tables member --outfile "common/models/member/Member"  --flask
flask-sqlacodegen 'mysql://root:mysql@127.0.0.1/food_db' --tables oauth_member_bind --outfile "common/models/member/OauthMemberBbind.py"  --flask

flask-sqlacodegen 'mysql://root:mysql@127.0.0.1/food_db' --tables food --outfile "common/models/food/Food.py"  --flask
