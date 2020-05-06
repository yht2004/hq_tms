
'''
    递归菜单列表
    id： 父菜单ID
    menus： 父菜单的子菜单列表
'''
def sub_menu(id,menus):
    subMenus = [] #子菜单列表
    for menu in menus: #遍历子菜单列表
        if menu.parent_id == id:
            subMenus.append(menu)
    for sub in subMenus:  #遍历子菜单的子菜单
        menu2 = queryByParent(sub.id)
        if len(menus):
            sub.subMenus = sub_menu(sub.id,menu2) #i菜单列表不为空
    return subMenus
    if len(subMenus):
        return None
