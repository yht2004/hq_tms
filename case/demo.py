from django.shortcuts import render
from django.http import response
from django.http.response import HttpResponse
from django.http import StreamingHttpResponse
from case.models import Case
import urllib
import xlwt,json,os
from io import BytesIO

def export_case(request):
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet('case',cell_overwrite_ok=True)

    #写入表头
    sheet.write(0, 0, '用例编号')
    sheet.write(0, 1, '所属项目')
    sheet.write(0, 2, '所属模块')
    sheet.write(0, 3, '相关需求')
    sheet.write(0, 4, '用例标题')
    sheet.write(0, 5, '前置条件')
    sheet.write(0, 6, '执行步骤')
    sheet.write(0, 7, '预期结果')
    sheet.write(0, 8, '实际结果')
    sheet.write(0, 9, '优先级')
    sheet.write(0, 10, '用例类型')
    sheet.write(0, 11, '用例创建者')
    sheet.write(0, 12, '用例评审者')
    sheet.write(0, 12, '评审结果')
    sheet.write(0, 12, '用例状态')
    sheet.write(0, 12, '用例执行结果')
    sheet.write(0, 12, '备注')

    cases = Case.objects.all()
    data_row = 1
    for case in  cases:
        sheet.write(data_row,4,case.case_title)
        sheet.write(data_row, 6, case.run_step)
        data_row += 1

    exist_file = os.path.exists('case_info.xls')

    if exist_file:
        os.remove(r'case_info.xls')

    wb.save('case_info.xls')

    file_name = 'case_info.xls'

    response = HttpResponse(open('case_info.xls', 'rb'), content_type='application/vnd.ms-excel')  # http返回支持微软excel
    response['Content-Disposition'] = 'attachment; filename="{0}";filename*=UTF-8\'\'{1}'.format(
        urllib.parse.quote_plus('case_info.xls'), urllib.parse.quote_plus('case_info.xls'))  # 为支持IE、火狐、Google浏览器，写的方法

    return response  # 文件流返回到浏览器后



