# -*- coding: utf-8 -*-
from application import app
from flask import request,g,jsonify

from common.models.member.Member import Member
from common.libs.member.MemberService import MemberService
import  re

'''
api认证
'''
@app.before_request
def before_request_api():
    api_ignore_urls = app.config['API_IGNORE_URLS']
    print(1)
    path = request.path
    if '/api' not in path:
        return
    print(2)
    member_info = check_member_login()
    g.member_info = None
    if member_info:
        g.member_info = member_info
    pattern = re.compile('%s' % "|".join( api_ignore_urls ))
    if pattern.match(path):
        return
    print(4)
    if not member_info :
        resp = {'code': -1, 'msg': '未登录~', 'data': {}}
        return jsonify(resp)
    print(5)
    return


'''
判断用户是否已经登录
'''
def check_member_login():
    auth_cookie = request.headers.get("Authorization")

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        member_info = Member.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if member_info is None:
        return False
    print(auth_info[0])
    print(MemberService.geneAuthCode( member_info ))
    if auth_info[0] != MemberService.geneAuthCode( member_info ):

        return False
    print(member_info.status)
    if member_info.status != 1:
        return False
    return member_info