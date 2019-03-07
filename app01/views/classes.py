#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.views import View
from app01 import models


class GetClasses(View):
    """
    编辑列表
    """
    def get(self, request):
        class_list = models.Classes.objects.all()
        return render(request, 'classes.html', {'class_list': class_list})


class AddClasses(View):
    """
    添加班级
    """
    def get(self, request):
        return render(request, 'add_classes.html')

    def post(self, request):
        new_title = request.POST.get('title')
        models.Classes.objects.create(title=new_title)
        return redirect('/classes')


class DelClasses(View):
    """
    删除班级
    """
    def get(self, request):
        nid = request.GET.get('nid')
        models.Classes.objects.filter(id=nid).delete()
        return redirect('/classes')


class EditClasses(View):
    """
    编辑班级
    """
    def get(self, request):
        nid = request.GET.get('nid')
        current_obj = models.Classes.objects.filter(id=nid)[0]
        return render(request, 'edit_classes.html', {'current_obj': current_obj})

    def post(self, request):
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/classes')


class SetTeacher(View):
    """
    分配老师
    """
    def get(self, request):
        nid = request.GET.get('nid')
        cls_obj = models.Classes.objects.filter(id=nid).first()
        cls_teacher_list = cls_obj.teacher.all().values_list('id', 'name')
        if len(list(zip(*cls_teacher_list))) > 0:
            id_list = list(zip(*cls_teacher_list))[0]
        else:
            id_list = []
        all_teacher_list = models.Teachers.objects.all()
        return render(request,'set_teacher.html', {'nid': nid, 'id_list': id_list, 'all_teacher_list': all_teacher_list})

    def post(self, request):
        nid = request.GET.get('nid')
        ids = request.POST.getlist('teacher_ids')
        cls_obj = models.Classes.objects.filter(id=nid).first()
        cls_obj.teacher.set(ids)
        return redirect('/classes')



