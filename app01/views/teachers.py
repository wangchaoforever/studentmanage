#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.views import View
from app01 import models

class GetTeachers(View):
    """
    老师列表
    """
    def get(self, request):
        teacher_list = models.Teachers.objects.all()
        return render(request, 'teachers.html', {'teacher_list': teacher_list})


class AddTeachers(View):
    """
    添加老师
    """
    def get(self, request):
        return render(request, 'add_teachers.html')

    def post(self, request):
        new_name = request.POST.get('name')
        new_age = request.POST.get('age')
        models.Teachers.objects.create(name=new_name,age=new_age)
        return redirect('/teachers')


class DelTeachers(View):
    """
    删除老师
    """
    def get(self, request):
        nid = request.GET.get('nid')
        models.Teachers.objects.filter(id=nid).delete()
        return redirect('/teachers')


class EditTeachers(View):
    """
    编辑老师
    """
    def get(self, request):
        nid = request.GET.get('nid')
        current_obj = models.Teachers.objects.filter(id=nid)[0]
        return render(request, 'edit_teachers.html', {'current_obj': current_obj})

    def post(self, request):
        nid = request.GET.get('nid')
        new_name = request.POST.get('name')
        new_age = request.POST.get('age')
        models.Teachers.objects.filter(id=nid).update(name=new_name, age=new_age)
        return redirect('/teachers')


class SetClass(View):
    """
    分配班级
    """
    def get(self, request):
        nid = request.GET.get('nid')
        # teacher_obj = models.Teachers.objects.filter(id=nid).first()
        teacher_class_list = models.Teachers.objects.filter(id=nid).values_list('classes__id', 'classes__title')
        if len(list(zip(*teacher_class_list))) > 0:
            id_list = list(zip(*teacher_class_list))[0]
        else:
            id_list = []
        all_class_list = models.Classes.objects.all()
        return render(request, 'set_class.html', {'nid': nid, 'id_list': id_list, 'all_class_list': all_class_list})

    def post(self, request):
        nid = request.GET.get('nid')
        ids = request.POST.getlist('class_ids')
        teacher_obj = models.Teachers.objects.filter(id=nid).first()
        teacher_obj.classes_set.set(ids)
        return redirect('/teachers')
