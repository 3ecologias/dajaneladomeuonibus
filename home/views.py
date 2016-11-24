from django.shortcuts import render
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.http import HttpResponseRedirect, Http404, HttpResponse
from home.models import ContactForm
from django.template import Context

def send(request):

	form_class = ContactForm

	if request.method == 'POST':

		form = form_class(data=request.POST)

		if form.is_valid():

			name = request.POST.get('name', '')

			email_contact = request.POST.get('email_contact', '')

			message = request.POST.get('message', '')

            # Email the profile with the 
            # contact information
			template = get_template('home/tags/email_template.txt')

			context_email = Context({
				'name': name,
				'email_contact': email_contact,
				'message': message,
			})
			content = template.render(context_email)
			
			email_host = 'smtp.gmail.com'
			email_host_user = 'juliaroberts@3ecologias.net'
			email_host_password = 'Tatub0lana0b0la'
			email_use_tls = True 
			email_port = 587

			with get_connection(host=email_host, port=email_port, username=email_host_user, password=email_host_password,
				use_tls=email_use_tls) as connection:

				EmailMessage(
					"Novo contato",
					content,
					"3Ecologias" +'',to=
					['admon@3ecologias.net'],
					headers = {'Reply-To': email_contact },
					connection=connection,
	 			).send(fail_silently=False)

			return HttpResponseRedirect('/')
 
	return render(request, 'home/home_page.html', {})