import xlrd
'''解析上传到服务器的测试用例文件'''

def parse_case(fileName):
    '''解析测试用例'''
    data = xlrd.open_workbook(fileName)
    table = data.sheet_by_index(0)
    dataFile = []

    for rowNum in range(table.nrows):
        if rowNum > 0:
            dataFile.append(table.row_values(rowNum))

    return dataFile