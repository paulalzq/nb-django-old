from django.shortcuts import render
from .models import Servicio
from .models import Portafolio
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

# Create your views here.

def home(request):
	
	form_class = ContactForm
	services = Servicio.objects.all()
	solutions = Portafolio.objects.all()
	
	if request.method == 'POST':
		form = form_class(data=request.POST)
		
		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name',
				''
				)
			contact_email = request.POST.get(
				'contact_email',
				''
				)
			form_content = request.POST.get(
				'form_content',
				''
				)
			
			# Perfil del correo con la información de contacto
						
			email = EmailMessage(
				"Posible Servicio",
				form_content,
				"Web de NoBinarix" + '',
				['nobinarix@gmail.com'],
				headers = {
					'Reply-To': contact_email
					}
				)
			email.send(
				print("enviado")
				)
			return redirect(redirect, 'home')
	
	return render(
		request, 'index/home.html', {
			'services': services,
			'solutions': solutions,
			'form': form_class,
			}
		)
