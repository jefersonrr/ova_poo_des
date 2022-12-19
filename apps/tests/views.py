from django.shortcuts import render
from django.http import JsonResponse
import json
from json import loads,dumps 
from apps.tests.models import Tests, Answers,AnswersValidate, Questions, IntentoTest
from apps.users.models import *
from apps.users.views import *

# Create your views here.

def home(request):
    return render(request,'home/index.html')

""" Esto no va aca, va en lo de admins """
def admin_dashboard(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        
    }
    return render(request,'admin/dashboard.html',context=context)

def admin_estudiantes(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'admin/index.html',context=context)

def admin_show_estudiantes(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'admin/show.html',context=context)

def admin_estudiantes_edit(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'admin/edit_student.html',context=context)

def admin_estudiantes_edit_password(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'admin/edit_student_password.html',context=context)



def subtema1_1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.1/prueba.html',context=context)

def subtema1_2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.2/prueba2.html',context=context)


def subtema1_3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.3/prueba1.3.html',context=context)


def subtema1_4(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.4/prueba1.4.html',context=context)


def subtema1_5(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.5/prueba1.5.html',context=context)


def subtema2_1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema2.1/subtema2.1.html',context=context)


def subtema2_2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema2.2/subtema2.2.html',context=context)


def subtema2_3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema2.3/subtema2.3.html',context=context)

def subtema2_4(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema2.4/subtema2.4.html',context=context)


def subtema3_1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.1/subtema3.1.html',context=context)

def subtema3_2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.2/subtema3.2.html',context=context)


def subtema3_3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.3/subtema3.3.html',context=context)

def subtema3_4(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.4/subtema3.4.html',context=context)
    
def subtema3_5(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.5/subtema3.5.html',context=context)

def subtema3_6(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.6/subtema3.6.html',context=context)

def subtema3_7(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.7/subtema3.7.html',context=context)

def subtema3_8(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.8/subtema3.8.html',context=context)

def subtema3_9(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.9/subtema3.9.html',context=context)

def subtema3_10(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema3.10/subtema3.10.html',context=context)


def subtema4_1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.1/subtema4.1.html',context=context)

def subtema4_2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.2/subtema4.2.html',context=context)

def subtema4_3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.3/subtema4.3.html',context=context)

def subtema4_4(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.4/subtema4.4.html',context=context)

def subtema4_5(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.5/subtema4.5.html',context=context)

def subtema4_6(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.6/subtema4.6.html',context=context)


def subtema4_7(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.7/subtema4.7.html',context=context)

def subtema4_8(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema4.8/subtema4.8.html',context=context)

def ejercicio_final(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'ejercicioPracticoFinal/ejercicio.html',context=context)

def test_1(request):
    
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit= request.session.get('nit','DE')
    ser_id = User.objects.filter(id=int(nit))
    inten = IntentoTest.objects.filter(user=ser_id[0],test=1)
    
    if(len(inten)>0):

        context = {
        'user':user,
        'promedio':inten[0].score_total,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
        }
        
        return render(request,'test1/resultadotest1.html',context=context)
    questions = Questions.objects.filter(test=1)
    arry = []
    i=1
    for quetion in questions:
        answers = Answers.objects.filter(question=quetion)
        array_opcions = []
        for answer in answers:
            dic_opcion = {"descripcion":answer.description, "id":answer.id}
            array_opcions.append(dic_opcion)
        dic = {"id":str(i), "descripcion":quetion.description,"id_q":quetion.id,
        "opcions":array_opcions}
        arry.append(dic)
        i+=1
    print(arry)
    context = {
        'user':user,
        "questions":arry,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test1/test.html',context=context)

def resultado_test_1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit = request.session.get('nit','DE')
    user_id = User.objects.filter(id=int(nit))
    

    if request.POST:
        print("post"*20)
        dic = dumps(request.POST)
        df = json.loads(dic)
        questions = Questions.objects.filter(test=1)
        promedio = 0
        
        for question in questions:
            valor = int(df.get(str(question.id)))
            rta = AnswersValidate.objects.filter(answers=valor)
            if(len(rta)>0):
                promedio+=question.score_question
        intento = IntentoTest()
        
        
        te = Tests.objects.filter(id=1)
        print(te)
        intento.user=user_id[0]
        intento.test=te[0]
        intento.score_total = promedio
        intento.save()
    request.session['test2'] = ""
    context = {
        'user':user,
        'promedio':promedio,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test1/resultadotest1.html',context=context)


def test_2(request):
    
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit= request.session.get('nit','DE')
    print("***************",nit)
    ser_id = User.objects.filter(id=int(nit))
    inten = IntentoTest.objects.filter(user=ser_id[0] ,test=2)
    print(inten)
    
    if(len(inten)>0):

        context = {
        'user':user,
        'promedio':inten[0].score_total,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
        }
        print(context)
        
        return render(request,'test2/resultadotest2.html',context=context)
    questions = Questions.objects.filter(test=2)
    arry = []
    i=1
    for quetion in questions:
        answers = Answers.objects.filter(question=quetion)
        array_opcions = []
        for answer in answers:
            dic_opcion = {"descripcion":answer.description, "id":answer.id}
            array_opcions.append(dic_opcion)
        dic = {"id":str(i), "descripcion":quetion.description,"id_q":quetion.id,
        "opcions":array_opcions}
        arry.append(dic)
        i+=1
    print(arry)
    context = {
        'user':user,
        "questions":arry,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test2/test2.html',context=context)

def resultado_test_2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit = request.session.get('nit','DE')
    user_id = User.objects.filter(id=int(nit))
    

    if request.POST:
        
        dic = dumps(request.POST)
        df = json.loads(dic)
        questions = Questions.objects.filter(test=2)
        promedio = 0
        
        for question in questions:
            valor = int(df.get(str(question.id)))
            rta = AnswersValidate.objects.filter(answers=valor)
            if(len(rta)>0):
                promedio+=question.score_question
        intento = IntentoTest()
        
        
        te = Tests.objects.filter(id=2)
        print(te)
        intento.user=user_id[0]
        intento.test=te[0]
        intento.score_total = promedio
        intento.save()
        request.session['test3'] = ""
    context = {
        'user':user,
        'promedio':promedio,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test2/resultadotest2.html',context=context)

def test_3(request):
    
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit= request.session.get('nit','DE')
    ser_id = User.objects.filter(id=int(nit))
    inten = IntentoTest.objects.filter(user=ser_id[0],test=3)
    
    if(len(inten)>0):

        context = {
        'user':user,
        'promedio':inten[0].score_total,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
        }
        
        return render(request,'test3/resultadotest3.html',context=context)
    questions = Questions.objects.filter(test=3)
    arry = []
    i=1
    for quetion in questions:
        answers = Answers.objects.filter(question=quetion)
        array_opcions = []
        for answer in answers:
            dic_opcion = {"descripcion":answer.description, "id":answer.id}
            array_opcions.append(dic_opcion)
        dic = {"id":str(i), "descripcion":quetion.description,"id_q":quetion.id,
        "opcions":array_opcions}
        arry.append(dic)
        i+=1
    print(arry)
    context = {
        'user':user,
        "questions":arry,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test3/test3.html',context=context)

def resultado_test_3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit = request.session.get('nit','DE')
    user_id = User.objects.filter(id=int(nit))
    

    if request.POST:
        print("post"*20)
        dic = dumps(request.POST)
        df = json.loads(dic)
        questions = Questions.objects.filter(test=3)
        promedio = 0
        
        for question in questions:
            valor = int(df.get(str(question.id)))
            rta = AnswersValidate.objects.filter(answers=valor)
            if(len(rta)>0):
                promedio+=question.score_question
        intento = IntentoTest()
        
        
        te = Tests.objects.filter(id=3)
        print(te)
        intento.user=user_id[0]
        intento.test=te[0]
        intento.score_total = promedio
        intento.save()
        request.session['test4'] = ""
    context = {
        'user':user,
        'promedio':promedio,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test3/resultadotest3.html',context=context)



def test_4(request):
    
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit= request.session.get('nit','DE')
    ser_id = User.objects.filter(id=int(nit))
    inten = IntentoTest.objects.filter(user=ser_id[0],test=4)
    
    if(len(inten)>0):

        context = {
        'user':user,
        'promedio':inten[0].score_total,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
        }
        
        return render(request,'test4/resultadotest4.html',context=context)
    questions = Questions.objects.filter(test=4)
    arry = []
    i=1
    for quetion in questions:
        answers = Answers.objects.filter(question=quetion)
        array_opcions = []
        for answer in answers:
            dic_opcion = {"descripcion":answer.description, "id":answer.id}
            array_opcions.append(dic_opcion)
        dic = {"id":str(i), "descripcion":quetion.description,"id_q":quetion.id,
        "opcions":array_opcions}
        arry.append(dic)
        i+=1
    print(arry)
    context = {
        'user':user,
        "questions":arry,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test4/test4.html',context=context)

def resultado_test_4(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    nit = request.session.get('nit','DE')
    user_id = User.objects.filter(id=int(nit))
    

    if request.POST:
        
        dic = dumps(request.POST)
        df = json.loads(dic)
        questions = Questions.objects.filter(test=4)
        promedio = 0
        
        for question in questions:
            valor = int(df.get(str(question.id)))
            rta = AnswersValidate.objects.filter(answers=valor)
            if(len(rta)>0):
                promedio+=question.score_question
        intento = IntentoTest()
        
        
        te = Tests.objects.filter(id=1)
        print(te)
        intento.user=user_id[0]
        intento.test=te[0]
        intento.score_total = promedio
        intento.save()
    
    context = {
        'user':user,
        'promedio':promedio,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'test4/resultadotest4.html',context=context)




























































































def subtema1_2_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.2/actividad1-1.2.html',context=context)

def subtema1_2_actv2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.2/actividad2-1.2.html',context=context)

def subtema1_2_actv3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.2/actividad3-1.2.html',context=context)

def subtema1_3_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.3/actividad1-1.3.html',context=context)

def subtema1_3_actv2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.3/actividad2-1.3.html',context=context)

def subtema1_3_actv3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.3/actividad3-1.3.html',context=context)

def subtema1_4_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.4/actividad1-1.4.html',context=context)

def subtema1_4_actv2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
        'test2': validar_test(request,2),
        'test3': validar_test(request,3),
        'test4': validar_test(request,4)
    }
    return render(request,'subtema1.4/actividad2-1.4.html',context=context)

def subtema2_1_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema2.1/actividad1-2.1.html',context=context)

def subtema2_2_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema2.2/actividad1-2.2.html',context=context)

def subtema2_3_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema2.3/actividad1-2.3.html',context=context)

def subtema2_4_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema2.4/actividad1-2.4.html',context=context)


def subtema3_1_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.1/actividad1-3.1.html',context=context)

def subtema3_2_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.2/actividad1-3.2.html',context=context)

def subtema3_3_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.3/actividad1-3.3.html',context=context)

def subtema3_4_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.4/actividad1-3.4.html',context=context)

def subtema3_5_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.5/actividad1-3.5.html',context=context)


def subtema3_6_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.6/actividad1-3.6.html',context=context)


def subtema3_7_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.7/actividad1-3.7.html',context=context)

def subtema3_8_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.8/actividad1-3.8.html',context=context)

def subtema3_9_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.9/actividad1-3.9.html',context=context)

def subtema3_10_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema3.10/actividad1-3.10.html',context=context)

def subtema4_1_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.1/actividad1-4.1.html',context=context)

def subtema4_2_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.2/actividad1-4.2.html',context=context)

def subtema4_3_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.3/actividad1-4.3.html',context=context)

def subtema4_4_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.4/actividad1-4.4.html',context=context)

def subtema4_5_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.5/actividad1-4.5.html',context=context)

def subtema4_6_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.6/actividad1-4.6.html',context=context)

def subtema4_7_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.7/actividad1-4.7.html',context=context)

def subtema4_8_actv1(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.8/actividad1-4.8.html',context=context)

def subtema4_8_actv2(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.8/actividad2-4.8.html',context=context)

def subtema4_8_actv3(request):
    if request.session.get('user','DE') == 'DE':
            return render(request,'login/login.html')
    user= request.session.get('user','DE')
    context = {
        'user':user,
    }
    return render(request,'subtema4.8/actividad3-4.8.html',context=context)