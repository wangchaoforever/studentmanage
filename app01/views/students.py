#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.views import View
from app01 import models

class GetStuents(View):
    """
    学生列表
    """
    def get(self, request):
        student_list = models.Students.objects.all()
        return render(request, 'students.html', {'student_list': student_list})


class AddStuents(View):
    """
    添加学生
    """
    def get(self, request):
        class_list = models.Classes.objects.all()
        return render(request, 'add_students.html', {'class_list': class_list})

    def post(self, request):
        new_name = request.POST.get('name')
        new_age = request.POST.get('age')
        new_gender = request.POST.get('gender')
        new_cs_id = request.POST.get('cs')
        models.Students.objects.create(
            name=new_name,
            age=new_age,
            gender=new_gender,
            cs_id=new_cs_id
        )
        return redirect('/students')


class DelStuents(View):
    """
    删除学生
    """
    def get(self, request):
        nid = request.GET.get('nid')
        models.Students.objects.filter(id=nid).delete()
        return redirect('/students')


class EditStuents(View):
    """
    编辑学生
    """
    def get(self, request):
        nid = request.GET.get('nid')
        current_obj = models.Students.objects.filter(id=nid)[0]
        class_list = models.Classes.objects.all()
        return render(request, 'edit_students.html', {'current_obj': current_obj, 'class_list': class_list})


    def post(self, request):
        nid = request.GET.get('nid')
        new_name = request.POST.get('name')
        new_age = request.POST.get('age')
        new_gender = request.POST.get('gender')
        new_cs_id = request.POST.get('cs')
        models.Students.objects.filter(id=nid).update(
            name=new_name,
            age=new_age,
            gender=new_gender,
            cs_id=new_cs_id
        )
        return redirect('/students')
