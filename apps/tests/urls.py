"""ova_poo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('subtema1.1/',subtema1_1, name='actividad1'),
    path('subtema1.2/',subtema1_2, name='actividad2'),
    path('subtema1.3/',subtema1_3, name='actividad3'),
    path('subtema1.4/',subtema1_4, name='actividad4'),
    path('subtema1.5/',subtema1_5, name='actividad5'),
    path('subtema2.1/',subtema2_1, name='actividad6'),
    path('subtema2.2/',subtema2_2, name='actividad7'),
    path('subtema2.3/',subtema2_3, name='actividad8'),
    path('subtema2.4/',subtema2_4, name='actividad9'),
    path('subtema3.1/',subtema3_1, name='actividad10'),
    path('subtema3.2/',subtema3_2, name='actividad11'),
    path('subtema3.3/',subtema3_3, name='actividad11'),
    path('subtema3.4/',subtema3_4, name='actividad12'),
    path('subtema3.5/',subtema3_5, name='actividad13'),
    path('subtema3.6/',subtema3_6, name='actividad14'),
    path('subtema3.7/',subtema3_7, name='actividad15'),
    path('subtema3.8/',subtema3_8, name='actividad16'),
    path('subtema3.9/',subtema3_9, name='actividad17'),
    path('subtema3.10/',subtema3_10, name='actividad18'),
    path('subtema4.1/',subtema4_1, name='actividad19'),
    path('subtema4.2/',subtema4_2, name='actividad20'),
    path('subtema4.3/',subtema4_3, name='actividad21'),
    path('subtema4.4/',subtema4_4, name='actividad22'),
    path('subtema4.5/',subtema4_5, name='actividad23'),
    path('subtema4.6/',subtema4_6, name='actividad24'),
    path('subtema4.7/',subtema4_7, name='actividad25'),
    path('subtema4.8/',subtema4_8, name='actividad26'),
    path('ejercicioPracticoFinal/',ejercicio_final, name='actividad27'),
    path('test1/',test_1, name='test1'),
    path('test2/',test_2, name='test2'),
    path('test3/',test_3, name='test3'),
    path('test4/',test_4, name='test4'),
    path('resultado_test1/',resultado_test_1, name='resultado_test1'),
    path('resultado_test2/',resultado_test_2, name='resultado_test2'),
    path('resultado_test3/',resultado_test_3, name='resultado_test3'),
    path('resultado_test4/',resultado_test_4, name='resultado_test4'),
    path('home/',home, name='index'),

    path('admin_dashboard/',admin_dashboard, name='admin_dashboard'),  
    path('admin_estudiantes/',admin_estudiantes, name='admin_estudiantes'),  
    path('admin_estudiantes_show/',admin_show_estudiantes, name='admin_estudiantes_show'),
    path('admin_estudiantes_edit/',admin_estudiantes_edit, name='admin_estudiantes_edit'),   
    path('admin_estudiantes_edit_password/',admin_estudiantes_edit_password, name='admin_estudiantes_edit_password'),  

    path('subtema1.2_actv1/',subtema1_2_actv1, name='subtema1_2_actv1'),
    path('subtema1.2_actv2/',subtema1_2_actv2, name='subtema1_2_actv2'),
    path('subtema1.2_actv3/',subtema1_2_actv3, name='subtema1_2_actv3'),

    path('subtema1.3_actv1/',subtema1_3_actv1, name='subtema1_3_actv1'),
    path('subtema1.3_actv2/',subtema1_3_actv2, name='subtema1_3_actv2'),
    path('subtema1.3_actv3/',subtema1_3_actv3, name='subtema1_3_actv3'),
    path('subtema1.4_actv1/',subtema1_4_actv1, name='subtema1_4_actv1'),
    path('subtema1.4_actv2/',subtema1_4_actv2, name='subtema1_4_actv2'),

    path('subtema2.1_actv1/',subtema2_1_actv1, name='subtema2_1_actv1'),
    path('subtema2.2_actv1/',subtema2_2_actv1, name='subtema2_2_actv1'),
    path('subtema2.3_actv1/',subtema2_3_actv1, name='subtema2_3_actv1'),
    path('subtema2.4_actv1/',subtema2_4_actv1, name='subtema2_4_actv1'),

    path('subtema3.1_actv1/',subtema3_1_actv1, name='subtema3_1_actv1'),
    path('subtema3.2_actv1/',subtema3_2_actv1, name='subtema3_2_actv1'),
    path('subtema3.3_actv1/',subtema3_3_actv1, name='subtema3_3_actv1'),
    path('subtema3.4_actv1/',subtema3_4_actv1, name='subtema3_4_actv1'),
    path('subtema3.5_actv1/',subtema3_5_actv1, name='subtema3_5_actv1'),
    path('subtema3.6_actv1/',subtema3_6_actv1, name='subtema3_6_actv1'),
    path('subtema3.7_actv1/',subtema3_7_actv1, name='subtema3_7_actv1'),
    path('subtema3.8_actv1/',subtema3_8_actv1, name='subtema3_8_actv1'),
    path('subtema3.9_actv1/',subtema3_9_actv1, name='subtema3_9_actv1'),
    path('subtema3.10_actv1/',subtema3_10_actv1, name='subtema3_10_actv1'),

    path('subtema4.1_actv1/',subtema4_1_actv1, name='subtema4_1_actv1'),
    path('subtema4.2_actv1/',subtema4_2_actv1, name='subtema4_2_actv1'),
    path('subtema4.3_actv1/',subtema4_3_actv1, name='subtema4_3_actv1'),
    path('subtema4.4_actv1/',subtema4_4_actv1, name='subtema4_4_actv1'),
    path('subtema4.5_actv1/',subtema4_5_actv1, name='subtema4_5_actv1'),
    path('subtema4.6_actv1/',subtema4_6_actv1, name='subtema4_6_actv1'),
    path('subtema4.7_actv1/',subtema4_7_actv1, name='subtema4_7_actv1'),

    path('subtema4.8_actv1/',subtema4_8_actv1, name='subtema4_8_actv1'),
    path('subtema4.8_actv2/',subtema4_8_actv2, name='subtema4_8_actv2'),
    path('subtema4.8_actv3/',subtema4_8_actv3, name='subtema4_8_actv3'),
    
    
]
