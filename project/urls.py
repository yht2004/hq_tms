
from django.urls import path
from project import views

urlpatterns = [
    path('pro_html',views.project_html),     #项目页面
    path('prodata',views.get_project_data),  #项目列表数据
    path('add',views.add_project),           #添加项目
    path('del',views.del_project),           #删除项目
]
