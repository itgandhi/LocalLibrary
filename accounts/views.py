from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.forms import SignUpForm
from accounts.tokens import account_activation_token
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode


@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            
            
            
            '''
            message = "\r\n".join([
                "From: locallibrarydemo@gmail.com",
                "To:"+form.cleaned_data.get('email'),
                "Subject:Activate Your Local Library Account",
                "",
                "hello kartik,"
                ])
            '''
            #print(' [Printed message]',message)
            #print(' [Printed message]',form.cleaned_data.get('email'))
            
            #s=smtplib.SMTP("smtp.gmail.com",587)
            #s.starttls()
            #s.login("locallibrarydemo@gmail.com", "Nnniii1213#")
            
            
            
            #s.sendmail("locallibrarydemo@gmail.com",form.cleaned_data.get('email'), message)
        
            #s.quit()
        
            subject = 'Activate Your Local Library Account'
            
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            
            to_email = form.cleaned_data.get('email')
            
            email = EmailMessage(
                subject,message,to=[to_email]
                )
            email.send()
            
            return HttpResponseRedirect(reverse('account_activation_sent') )
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

@csrf_protect
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

@csrf_protect
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'account_activation_invalid.html')
    
    
    
    
    
    