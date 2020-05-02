
from django.urls import path,re_path
from case import views,demo

urlpatterns = [
    path('case_html',views.get_case_html),                          #case页面
    path('get_case',views.case_index),                              #case列表
    #re_path(r'^case/(?P<id>\d+)$',views.run_case,name='detail'),   #执行用例
    path('selectById',views.get_case_byId),
    path('add',views.add_case),                                     #添加用例
    path('update',views.update_case_byID),
    path('runcase',views.run_case),                                 #执行用例
    path('export',demo.export_case),                                #导出用例
    path('run',views.run_case),                                     #用例执行
    path('importCase',views.import_case),                           #用例导入
    path('delete',views.del_case_byId),                             #删除用例
    path('projects',views.project_html),                            #项目列表

]
