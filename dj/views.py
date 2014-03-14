from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
import json

from django.template import Context, Template
from django.template.loader import get_template
from django.utils import simplejson
from dj.models import Publisher

import MySQLdb
 
def index(request):
  return HttpResponse('aaaa')

def home(request, year):
  html = 'chen jian ping'
  data = {"answer": "abc"}
  t = get_template('home.html')
  html = t.render(Context({'name': 'chen ping ping.'}))
  return HttpResponse(html)

  # return HttpResponse(json.dumps(data, ensure_ascii=False), mimetype="application/json")
  # return HttpResponse(simplejson.dumps(data, ensure_ascii=False))
  # return HttpResponse(html)
  # return HttpResponseRedirect(reverse('home', args=(2015,)))
  # return render_to_response('home.html', {'name': year})

def testa(request):
    return HttpResponse('ping ping ping chen chen')
    
def test(request):
  dic = {'name': 'chen', 'addr': 'Bei jin Chao'}
  li = {}
  li['data'] = dic
  li['price'] = ('12', '2-13-12-12')
  # return HttpResponse(simplejson.dumps(li), mimetype="application/json")
  # return HttpResponse(request.META['REMOTE_ADDR'])

def db(request):
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='111111', port=3306) #, db='blog')
        cur = conn.cursor()
        conn.select_db('blog')
        cur.execute('insert into blog_user(`name`, `age`, `addr`) values(%s, %s, %s)', ('chen ping2', 23, 'Bei Jing Caho Yang'))
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print e
    return HttpResponse('index')