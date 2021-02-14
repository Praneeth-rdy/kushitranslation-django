from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage


from .models import *
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    services = Service.objects.all()
    faqs = Faq.objects.all()
    testimonials = Testimonial.objects.all()
    sliders = Slider.objects.all()
    counter_items = Counter.objects.all()
    industries = Industry.objects.all()
    professional_services = ProfessionalService.objects.all()
    languages = Language.objects.all()
    whys = WhyUs.objects.all()
    l=(len(faqs)//2)
    faqs1=[]
    faqs2=[]
    count = 0
    for faq in faqs:
        if count <= l:
            faqs1.append(faq)
            count += 1
        else:
            faqs2.append(faq)
    count = 0
    for slider in sliders:
        if count == 0:
            slider.is_active = True
            count += 1
        else:
            slider.is_active = False
    try:
        is_logged_in = request.user.is_authenticated
    except:
        is_logged_in = False
    context = {
        'is_logged_in': is_logged_in,
        'services': services,
        'faqs1': faqs1,
        'faqs2': faqs2,
        'testimonials': testimonials,
        'sliders': sliders,
        'counter_items': counter_items,
        'whys': whys,
        'industries': industries,
        'professional_services': professional_services,
        'languages': languages,
    }
    
    return render(request, 'home.html', context)

def get_quote(request):
    if request.method == 'GET':
        languages = Language.objects.all()
        context = {
            'languages': languages,
        }
        return render(request, 'get_quote.html', context)
    elif request.method == 'POST':
        source_language = request.POST.get('source_lang')
        target_language = request.POST.get('target_lang')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        document = request.FILES.get('document')

        is_doc = False
        if document is not None:
            is_doc = True

        mail_subject = 'Kushi Translations: Quote Request'
        message = render_to_string('quote_request.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'source_language': source_language,
            'target_language': target_language,
            'is_doc': is_doc,
        })
        email = EmailMessage(
            mail_subject, message, to=['k.praneeth1199@gmail.com']
        )
        email.attach(document.name, document.read(), document.content_type)

        email.send(fail_silently=False)
        print('\n\n', name, document, phone, '\n\n\n')
        return HttpResponse("<h1>Our team has recieved your request and will get in touch with you soon.</h1>")
    else:
        return HttpResponse("<h1>Invalid Option</h1>")

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        mail_subject = 'Kushi Translations: You Recieved a Message'
        message = render_to_string('leave_message.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })
        email = EmailMessage(
            mail_subject, message, to=['kushitranslations@gmail.com']
        )
        email.send(fail_silently=False)
        return HttpResponse("<h1>Your message has been sent. Thank You.</h1>")
    else:
        return HttpResponse("<h1>Invalid Try.</h1>")