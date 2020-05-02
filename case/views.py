from django.shortcuts import render,redirect
from case.models import Case,Project
from django.http.response import HttpResponse
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import json,os
from utils import parse_file

def add_case(request):
    '''添加测试用例'''
    case_name = request.POST['case_title']
    project_name = request.POST['project_name']
    run_step = request.POST['run_step']
    except_result = request.POST['except_result']
    case_type = request.POST['case_type']
    name = Project.objects.get(project_name=project_name)
    print(case_type)
    Case.objects.create(case_title=case_name,project_name=name,run_step=run_step,expect_result=except_result,case_type=case_type)
    return redirect('/case/case_html')


def get_case_html(request):
    '''用例页面'''
    cases = Case.objects.all()
    projects = Project.objects.all()
    caseType = Case.case_types
    types = []
    for v in dict(caseType).values():
        types.append(v)

    return render(request,'case/case.html',{'cases':cases,'projects':projects,'types':types})

def case_index(request):
    '''获取用例列表'''
    rows = []
    cases = Case.objects.all()
    for case in cases:
        project = Project.objects.get(project_name=case.project_name)
        name = project.project_name
        rows.append({
            'id':case.id,
            'case_no':case.case_no,
            'project_name':name,
            'level':case.get_level_display(),
            'case_name':case.case_title,
            'case_type':case.get_case_type_display(),
            'project_model':case.project_model,
            'case_statu':case.get_case_statu_display(),
            'case_result':case.get_case_result_display(),
            'run_step': case.run_step,
            'expect_result': case.expect_result,
            'expect_reality': case.expect_reality
        })
    return HttpResponse(json.dumps(rows))


def get_case_byId(request):
    '''根据id查询用例'''
    id = request.POST['id']
    print(id)
    case = Case.objects.filter(id=id)
    name = case.get().case_title
    case_dict = {
        'case_name':name,
    }
    return HttpResponse(json.dumps(case_dict))


def update_case_byID(request):
    '''修改数据'''
    case_id = request.POST['case_id']
    case_name = request.POST['case_title']
    run_step = request.POST['run_step']
    expect_result = request.POST['except_result']
    project_name = request.POST['project_name']
    case_type = request.POST['case_type']
    name = Project.objects.get(project_name=project_name)
    Case.objects.filter(id=case_id).update(case_title=case_name,project_name=name,
                                           case_type=case_type,run_step=run_step,expect_result=expect_result)
    print('前台传入的数据：',case_id)
    print('前台传入的用例类型：', case_type)
    return redirect('/case/case_html')

def run_case(request):
    '''执行用例'''
    id = request.POST['case_id']
    expect_reality = request.POST['expect_reality']
    Case.objects.filter(id=id).update(expect_reality=expect_reality)
    return redirect('/case/case_html')


def del_case_byId(request):
    '''根据ID删除用例'''
    case_id = request.POST['case_id']
    Case.objects.filter(id=case_id).delete()
    return  render(request,'case/case.html')

def import_case(request):
    '''用例导入'''
    project_name = request.POST['project_name']
    case_file = request.FILES.get("case_file")
    file_name = request.POST['file_name']
    if case_file.size < 20480000:
        case_file.name = file_name+'case.xlsx'
        path = default_storage.save('media/' + case_file.name,ContentFile(case_file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT,path)
    else:
        print('文件过大,不要超过2M')
    datas = parse_file.parse_case(path)



    for data in datas:
        projectName = Project.objects.get(project_name=project_name)
        Case.objects.create(
            case_no= data[0],
            project_name=projectName,
            project_model=data[2],
            case_title=data[4],
            run_step=data[6],
            expect_result=data[7],
            case_type=data[10])

    return redirect('/case/case_html')

def project_html(request):
    projects = Project.objects.all()
    return render(request,'project/project.html',{'projects':projects})


