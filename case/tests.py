import json
from datetime import *
import time
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


menus = {
    '测试管理':{
        '用例管理',
        '缺陷管理',
        '报告管理',
    },
    '项目管理':{
        '项目'
    },
    '系统管理':{
        '统计报表'
    },
    '系统设置':{
        '数据字典',
        '系统日志',
        '友情链接',
        '权限设置'
    }
}
def show_Menu(ch):
    for s in ch:
        print(s)
    print('返回/退出')
    p = input('您选择是')
    if p == '退出':
        exit()
    elif p == '返回'and ch != menus:
        print('ch数据：',ch)
        return
    else:
        if p in ch:
            show_Menu(ch[p])
        show_Menu(ch)
#show_Menu(menus)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

str = '2020-04-07 16:27:37+00:00'
print(datetime.now())
dt = datetime.now()
print ('(%Y-%m-%d %H:%M:%S ): ', dt.strftime('%Y-%m-%d %H:%M:%S ')  )
print ('(%Y-%m-%d  ): ', dt.strftime('%Y-%m-%d  ')  )




















