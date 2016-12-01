from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from django import forms
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel)
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

class HomePage(Page):
  button = models.CharField(max_length=255)
  body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

  content_panels = Page.content_panels + [
    FieldPanel('button'),
    StreamFieldPanel('body')

	]

class About(Page):
	body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])


	content_panels = Page.content_panels + [
	  StreamFieldPanel('body')

	]

class Participe(Page):
  body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])


  content_panels = Page.content_panels + [
    StreamFieldPanel('body')

  ]
class News(Page):
     main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
     date = models.DateField("Post date")
     intro = models.CharField(max_length=250)
     body = RichTextField(blank=True)

     search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),

        ]

     content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
class Testimonials(Page):
    # body = StreamField([
    #     ('heading', blocks.CharBlock(classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ])
     main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    #  date = models.DateField("Post date")
     instagram_user = models.TextField(blank=True, null=True)
     name = models.CharField(max_length=255, null=True, blank=True)

     content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('name'),
        FieldPanel('instagram_user'),
    ]


@register_setting
class ApiTokenInstagramSettings(BaseSetting):
  INSTAGRAM_USER_ID = models.TextField()
  INSTAGRAM_CLIENT_ID = models.TextField()
  INSTAGRAM_CLIENT_SECRET = models.TextField()
  INSTAGRAM_ACCESS_TOKEN = models.TextField()


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL')
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @')
  #  trip_advisor = models.URLField(
   #     help_text='Your Trip Advisor page URL')
    #youtube = models.URLField(
     #   help_text='Your YouTube channel or user account URL')

from wagtail.wagtailsnippets.models import register_snippet
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

REDES_SOCIAIS_C = (
  ('FACEBOOK', 'Facebook'),
  ('TWITTER', 'Twitter'),
  ('INSTAGRAM', 'Instagram'),
)
@register_snippet
@python_2_unicode_compatible

class Post(models.Model, index.Indexed):
  """(Post description)"""
  texto = models.TextField()
  imagem = models.ImageField(upload_to='media/instagram',null=True,blank=True,)
  imagem_src = models.URLField(null=True,blank=True)
  redesocial = models.CharField(max_length=255, choices=REDES_SOCIAIS_C)
  pid = models.CharField(max_length=255)
  date = models.DateField()
  link = models.CharField(max_length=255, null=True, blank=True)
  ativo = models.BooleanField(default=True)

  search_fields = (
        index.SearchField('texto', partial_match=True, boost=10),
        index.FilterField('imagem_src'),
        )

  panels = [
        FieldPanel('texto'),
        FieldPanel('imagem'),
        FieldPanel('imagem_src'),
        FieldPanel('redesocial'),
        FieldPanel('pid'),
        FieldPanel('date'),
        FieldPanel('link'),
        FieldPanel('ativo'),
    ]


  class Meta:
    verbose_name, verbose_name_plural = u"Post" , u"Posts Instagram"
    ordering = ('-date',)

  def __str__(self):
    return self.texto


  def get_imagem(self):
    if self.imagem:
      return self.imagem
    elif self.imagem_src:
      return self.imagem_src
    return None

class ContactForm(forms.Form):

    name = forms.CharField(
      required=True,
      widget=forms.TextInput(
        attrs={'placeholder': 'Nome *', 'id': 'name', 'class': 'form-control margin_inputs', 'type': 'text'}))

    email_contact = forms.EmailField(
      required=True,
      widget=forms.EmailInput(
        attrs={'placeholder': 'Email *', 'id': 'email', 'class': 'form-control margin_inputs'}))

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Mensagem *', 'id': 'message', 'class': 'form-control margin_inputs'})
    )
