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
import re, json


def log(texto):
	print "===================================="
	print texto
	print "===================================="


def carga():
	log("INICIO DA ROTINA")
	from home.models import Post
	from home.models import ApiTokenInstagramSettings
	from instagram.client import InstagramAPI
	# AUTH REQUIRED
	access_token = '1345635461.7089ef3.9bc2cfb0180741d392728cc107b432fb'
	client_secret = 'cb86b8747fea45d9a745e95bb31110e0'
	user_id = '1345635461'
	api = InstagramAPI(access_token=access_token, client_secret=client_secret)
	recent_media, next_ = api.user_recent_media(user_id=user_id, count=10)
	#popular_media = api.media_popular(count=20)
	for media in recent_media:
		print dir(media)
		#print media.caption.text
		post = Post.objects.filter(pid=media.id)

		texto = media.caption.text if media.caption else None

		try:
			if post:
				post = post[0]
				post.texto = u'{0}'.format(texto)
				post.date = media.created_time
				post.imagem = media.get_standard_resolution_url()
				post.imagem_src = media.get_standard_resolution_url()
			else:
				post = Post(
					redesocial = 'INSTAGRAM',
					pid = media.id,
					texto = u'{0}'.format(texto),
					date = media.created_time,
					link = media.link,
					imagem = media.get_standard_resolution_url(),
					imagem_src = media.get_standard_resolution_url(),
				)
			post.save()
		except Exception, e:
			log(u"Erro ao inserir [{0}]: {1}".format(media.id, media.get_standard_resolution_url()))
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