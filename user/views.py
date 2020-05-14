from django.shortcuts import render
from resource.models import Menus

def index(request):

    root_menu = Menus.objects.filter(parent_id=None)  # 一级菜单
    for root in root_menu:
        root.sub_menus = Menus.objects.filter(parent_id=root.id)  # 二级菜单列表
        for menu2 in root.sub_menus:
            menu2.sub_menus = Menus.objects.filter(parent_id=menu2.id)  # 三级菜单列表

    return render(request, 'index.html', {'menus': root_menu})


def dashboard(request):
    return render(request,'dashboard.html')