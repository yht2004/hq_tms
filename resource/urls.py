
from django.urls import path,re_path
from resource import views

urlpatterns = [
    path('dd',views.demo_menus),           #获取菜单
    path('menus',views.menus),             #获取菜单

]
