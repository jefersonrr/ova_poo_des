from django.shortcuts import render
from django.http import JsonResponse
import json
from json import loads,dumps 
from django.views.decorators.csrf import csrf_exempt
from apps.users.models import User,Person, Rol
from apps.tests.models import *
from apps.tests.views import consultar_estudiantes

# Create your views here.
@csrf_exempt
def Home(request):
    
    if request.POST:
        
        dic = dumps(request.POST)
        df = json.loads(dic)
        user= User.objects.filter(email=df['email'],password=df['password'])
        
        
        if len(user)>0:
            inten = IntentoTest.objects.filter(user=user[0])
            request.session['user'] = request.session['user'] = user[0].person.name + " " + user[0].person.last_name
            request.session['rol'] = user[0].rol.id
            request.session['nit'] = user[0].id
            
            request.session['test2'] = "pointer-events:none; cursor:default;background-color: rgb(215, 207, 207);"
            request.session['test3'] = "pointer-events:none; cursor:default;background-color: rgb(215, 207, 207);"
            request.session['test4'] = "pointer-events:none; cursor:default;background-color: rgb(215, 207, 207);"
            for ten in inten:
                
                if ten.test.id >= 1:
                    request.session['test2'] = ""
                if ten.test.id >= 2:
                    request.session['test3'] = ""
                if ten.test.id >= 3:
                    request.session['test4'] = ""
            user_sesion= request.session.get('user','DE')
            context = {
            'user':user_sesion,
            'test2': validar_test(request,2),
            'test3': validar_test(request,3),
            'test4': validar_test(request,4)
                }
        else:
            context = {
            'valido':"2",
                }
            return render(request,'login/login.html',context=context)
    else:
        
        if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
        user_sesion= request.session.get('user','DE')
        
        
        context = {
        'user':user_sesion,
    }
        
    
    if request.session.get('rol','DE') == 1:
        
        
        return render(request,'home/index.html',context=context)
    else :
        context = {
        'user':user_sesion,
        'estudiantes':consultar_estudiantes(),
        }
        return render(request,'admin/index.html',context=context)
@csrf_exempt
def login(request):
    name = ""
    if request.session.get('user','DE') == 'DE':
        context = {
            'valido':"0",
                }
        return render(request,'login/login.html', context=context)
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
        }
    
    if request.session.get('rol','DE') == 1:
        return render(request,'home/index.html',context=context)
    else :
        return render(request,'admin/index.html',context=context)

def cerrar_session(request):
    if 'user' in request.session:
        del request.session['user']
    if 'rol' in request.session:
        del request.session['rol']
    if 'rol' in request.session:
        del request.session['nit']
    if 'test2' in request.session:
        del request.session['test2']
    if 'test3' in request.session:
        del request.session['test3']
    if 'test4' in request.session:
        del request.session['test4']
    
   
    return render(request,'login/login.html')

def validar_test(request,test):
    
    if test==2 and request.session.get('test2','DE') != 'DE':
        
        return request.session.get('test2','DE')
    if test==3 and request.session.get('test3','DE') != 'DE':
        
        return request.session.get('test3','DE')
    if test==4 and request.session.get('test4','DE') != 'DE':
        
        return request.session.get('test4','DE')
    return ""

def registrarse(request):
    
    if request.POST:
        
        
        dic = dumps(request.POST)
        df = json.loads(dic)
        
        user_cedula= Person.objects.filter(cedula=df['document'])
        
        user_email= User.objects.filter(email=df['email'])

        if len(user_cedula)>0:
            context = {
            'valido_cedula':"2",
                }
            return render(request,'login/register.html',context=context)
        if len(user_email)>0:
            context = {
            'valido_cedula':"1",
                }
            return render(request,'login/register.html',context=context)   

        if len(user_cedula)==0 and len(user_email)==0:

            per = Person()
            per.cedula = df['document']
            per.email = df['email']
            per.name = df['name']
            per.last_name = df['lastname']
            per.type_document = df['document_type_id']
            per.phone = df['telephone']
            per.birthdate = df['birthdate']
            per.birthdate_place = df['place_b']
            per.address = df['address']
            per.codigo = df['code']
            per.save()

            user = User()
            user.person = per
            user.rol = Rol.objects.get(id=1)
            user.email = df['email']
            user.password = df['password']
            user.save()

            request.session['user'] = request.session['user'] = per.name + " " + per.last_name
            user= request.session.get('user','DE')
            context = {
            'user':user,
            'test2': validar_test(request,2),
            'test3': validar_test(request,3),
            'test4': validar_test(request,4)
                }
            return  render(request,'home/index.html',context=context)
        else:
            context = {
            'valido':"2",
                }
            return render(request,'login/login.html',context=context)
    else:
        context = {
            'valido_cedula':"0",
                }
        return render(request,'login/register.html',context=context)
