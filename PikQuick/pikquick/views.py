from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/usuario/ingreso')
def inicio(request):
    context = RequestContext(request)
    return render_to_response('inicio.html',
                              context)

@login_required(login_url='/usuario/ingreso')
def ajustes(request):
    context = RequestContext(request)
    return render_to_response('ajustes.html',
                              context)

@requires_csrf_token
@login_required(login_url='/usuario/ingreso')
def enviar_mail(request):
    context = RequestContext(request)
    if request.method=='POST':
        send_mail(request.POST['asunto'], request.POST['mensaje'], 'pikquickcontact@gmail.com',
    [request.POST['mail']], fail_silently=False)
    return render_to_response('ajustes.html',
                              context)

@requires_csrf_token
def nuevo_usuario(request):
    context = RequestContext(request)
    if request.method=='POST':
        n_u=User()
        username=request.POST['username']
        n_u.username=username
        n_u.email=request.POST['email']
        password=request.POST['password']
        n_u.set_password(password)
        n_u.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render_to_response('nuevousuario.html',
                              context)

@requires_csrf_token
def ingreso_usuario(request):
    context = RequestContext(request)
    if not request.user.is_authenticated():
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("");
                else:
                    return HttpResponse(status=203)
            else:
                return HttpResponse(status=203)
        else:
            return render_to_response('loguear.html',
                                              context)
    else:
        return render_to_response('loguear.html',
                                              context)

@login_required(login_url='/usuario/ingreso')
def salir_usuario(request):
    logout(request)
    context = RequestContext(request)
    return redirect('/')

@login_required(login_url='/usuario/ingreso')
def cambiar_pass(request):
    context = RequestContext(request)
    if request.method=='POST':
        if request.user.check_password(request.POST['password1']):
            request.user.set_password(request.POST['password2'])
            request.user.save()
            user= authenticate(username=request.user.username, password=request.POST['password2'])
            login(request, user)
            return redirect("/ajustes")
    return render_to_response('ajustes.html',
                              context)
