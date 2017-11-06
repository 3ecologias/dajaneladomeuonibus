#!/usr/bin/env python
# coding: utf-8

from os.path import abspath, dirname
from datetime import datetime, date, timedelta
import sys, os, commands, time

SETTINGS_DIRECTORY = dirname(dirname(abspath(__file__)))

sys.path.insert(0, SETTINGS_DIRECTORY)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dajanela.settings.dev'

from django.conf import settings
from dajanela.settings import base
from django.db.models import Count, Min, Sum, Avg
from django.template.defaultfilters import slugify
from datetime import datetime
import re, json, requests


def log(texto):
	print "===================================="
	print texto
	print "===================================="


def carga():
	log("INICIO DA ROTINA")
	from home.models import Post
	from home.models import ApiTokenInstagramSettings
	# AUTH REQUIRED
	access_token = '1345635461.7089ef3.9bc2cfb0180741d392728cc107b432fb'
	url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={0}'.format(access_token)
	recent_media = requests.get(url)
	recent_media = recent_media.json()['data']
	post_number = 0

	for media in recent_media:
		post = Post.objects.filter(pid=media['id'])

		texto = media['caption']['text'] if media['caption'] else None

		try:
			if post:
				post = post[0]
				post.texto = u'{0}'.format(texto)
				post.date = datetime.fromtimestamp(float(media['created_time']))
				post.imagem = media['images']['standard_resolution']['url']
				post.imagem_src = media['images']['standard_resolution']['url']
			else:
				post = Post(
					redesocial = 'INSTAGRAM',
					pid = media['id'],
					texto = u'{0}'.format(texto),
					date = datetime.fromtimestamp(float(media['caption']['created_time'])),
					link = media['link'],
					imagem = media['images']['standard_resolution']['url'],
					imagem_src = media['images']['standard_resolution']['url'],
				)
			post.save()
			post_number+=1
		except Exception, e:
			log(u"Erro ao inserir [{0}]: {1}".format(media['id'], media['images']['standard_resolution']['url']))
			log(e)

	# AUTH NON REQUIRED
	#api = InstagramAPI(client_id=settings.INSTAGRAM_CLIENT_ID, client_secret=settings.INSTAGRAM_CLIENT_SECRET)
	#popular_media = api.media_popular(count=20)
	#for media in popular_media:
	#   print media.images['standard_resolution'].url

	log("FIM DA ROTINA")

if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'dajanela.settings.dev')
	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()

	carga()
