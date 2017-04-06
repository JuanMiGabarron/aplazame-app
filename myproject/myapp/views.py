from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from myapp.models import Alumno, Curso


import logging
import json

logger = logging.getLogger(__name__)


# View for home page
def index(request):
    group = ''
    if not request.user.is_anonymous:
        group = request.user.groups.all()[0].name
    return render(request, 'myapp/index.html', {'group':group})

@login_required
def new_curso(request):
    return render(request, 'myapp/new_curso.html')


@login_required
def curso(request, curso):
    group = ''
    if not request.user.is_anonymous:
        group = request.user.groups.all()[0].name
    alumno_id = Alumno.objects.get(usuario=request.user.id)
    return render(request, 'myapp/curso.html',
        {'curso':curso, 'group':group, 'alumno_id': alumno_id.id})

# view to create a new user
def sign_in(request):
    return render(
        request,
        'myapp/signin.html',
    )


# view to create a new user (cocinero or alumno)
def create_user(request):
    payload = {
            'success':'',
            'message': '',
            'data': '',
        }
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        alumno = request.POST.get('alumno', '')
        name = request.POST.get('nombre', '')
        last_name = request.POST.get('apellidos', '')
        cpostal = request.POST.get('codigo_postal', '')
        cpais = request.POST.get('codigo_pais', '')
        payload['data'] = email
           
        if email and password:
            if not User.objects.filter(email=email):
                new_user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )
                new_user.save()
                logger.info("Usuario creado")
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                if alumno:
                    new_user.first_name = name
                    new_user.last_name = last_name
                    new_user.save()
                    new_alumno = Alumno.objects.create(
                        usuario=new_user,
                        codigo_postal=cpostal,
                        codigo_pais=cpais,
                    )
                    new_alumno.save()
                    g, create = Group.objects.get_or_create(name='alumnos')
                else:
                    g, create = Group.objects.get_or_create(name='cocineros')
                new_user.groups.add(g.id)
                payload['success'] = True
                payload['message'] = 'usuario creado con exito'
                return HttpResponse(json.dumps(payload))
            else:
                logger.warning("Email en uso")
                payload['message'] = 'email en uso'
        else:
            logger.warning("Email o password incorrectos")
            payload['message'] = 'email o password incorrectos'
    logger.warning('No POST on method')
    payload['success'] = False
    return HttpResponse(json.dumps(payload))


def login_user(request):
    payload = {'success':''}
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            payload['success'] = True
            return HttpResponse(json.dumps(payload))
        else:
            payload['success'] = False
            return HttpResponse(json.dumps(payload))  


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')
