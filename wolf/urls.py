# -*- coding: utf-8 -*-
from django.urls import path
import wolf.views as view

urlpatterns = [
        path('', view.start, name='start'),
        path('player/',view.now_player, name='player'),
        path('create/',view.create, name='create'),
        path('edit/<int:num>/', view.edit, name='edit'),
        path('delete/<int:num>/', view.delete, name='delete'),
        path('job_create/', view.job_create, name='job_create'),
        path('job_how/', view.job_how, name='job_how'),
        path('sub_start/', view.sub_start, name='sub_start'),
        path('how_many/', view.how_many, name='how_many'),
        path('check_job/<int:num>/', view.check_job, name='check_job'),
        path('look_job/<int:num>/', view.look_job, name='look_job'),
        path('finish/', view.finish, name='finish')
        ]