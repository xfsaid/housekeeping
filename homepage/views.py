#coding:utf-8
import json
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
from .models import TeacherInfo,GradeSubjectMenu,Subject



# Create your views here.
def welcome(request):
    st = loadjsonfile()
    return HttpResponse(u"%s" % st)

def index(request):
    subjects = Subject.objects.all()


    tec_info_list_all = TeacherInfo.objects.all()
    paginator = Paginator(tec_info_list_all, 3)
    page = request.GET.get('page')

    try:
        tec_info_list = paginator.page(page)
    except PageNotAnInteger:
        tec_info_list = paginator.page(1)
    except EmptyPage:
        tec_info_list = paginator.page(paginator.num_pages)

    grade_subject_dict = {}
    grade_dict = GradeSubjectMenu.objects.values('tab_grade').distinct()

    for grade in grade_dict:
        key = grade['tab_grade']
        grade_subject_dict[key] = GradeSubjectMenu.objects.filter(tab_grade=key)

    return render_to_response('index.html',{
        'tec_info_list':tec_info_list,
        'grade_subject_dict':grade_subject_dict})


def loadjsonfile():
    j_f = open("jsonfiles/tabs.json",'r')
    tabs = json.load(j_f)
    family = tabs['fontSize']
    return family['2']