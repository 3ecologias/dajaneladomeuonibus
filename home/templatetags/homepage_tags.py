from django import template
from home.models import *
from django.core.mail import EmailMessage
from django.template.loader import get_template

register = template.Library()

@register.inclusion_tag('home/tags/about_page.html')
def about_page():
 	about = About.objects.live()
 	return {
 	 'about' : about

 	}


@register.inclusion_tag('home/tags/participe_page.html')
def participe_page():
 	participe = Participe.objects.live()
 	return {
 	 'participe' : participe

 	}

@register.inclusion_tag('home/tags/news_page.html')
def news_page():
 	news = News.objects.live().order_by('-date')
 	return {
 	 'news' : news

 	}

@register.inclusion_tag('home/tags/instagram_slide.html', takes_context=True)
def instagram_slide(context):
    return {
        'post': Post.objects.all(),
        'lastest': Post.objects.all().order_by('-date')[:20],
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/search_results.html')
def search_results():
 	post = Post.objects.all()
 	return {
 	 'post' : post

 	}

@register.inclusion_tag('home/tags/testimonials.html')
def testimonials():
 	testimonials = Testimonials.objects.all()
 	return {
 	 'testimonials' : testimonials

 	}

@register.inclusion_tag('home/tags/footer.html')
def footer():

	footer = ContactForm
	return{
	 'footer' : footer
	}
