import os
import random
import traceback
import pandas as pd
from data import rdate
from utils import configure
from openpyxl import load_workbook as wk


def exc_path():
    try:
        exc_read(os.path.abspath('.') + r'/1-学生名单表/学生名单.xlsx')
        return os.path.abspath('.') + r'/1-学生名单表/学生名单.xlsx', os.path.abspath('.') + r'/2-考勤结果/点名文档.txt'
    except FileNotFoundError:
        exc_read(os.path.abspath('../..') + r'/1-学生名单表/学生名单.xlsx')
        return os.path.abspath('../..') + r'/1-学生名单表/学生名单.xlsx', os.path.abspath('../..') + r'/2-考勤结果/点名文档.txt'


# todo """根据读取数据，获取[学生名单]执行路径""" 需要完善

def exc():
    result = {}
    for x in read_cou()['cou']:
        try:
            data = pd.read_excel(exc_path()[0], sheet_name=f'{x}')
        except ValueError:
            traceback.print_exc()
            raise Exception('您的excel表格中可能没有数据，请您核验一下。')
        classes, student, all_dict = data['班级'], data['名单'], {}

        # noinspection PyAssignmentToLoopOrWithParameter
        for y in set(classes):
            all_dict[y] = []

        # noinspection PyAssignmentToLoopOrWithParameter
        for z in range(len(data)):
            row = data.iloc[z]
            all_dict[row['班级']].append(row['名单'])
        result[x] = all_dict

    return result


# 读取Excel原始数据 需要完善
#  #
#  test : data = dict([(k, v) for i, v in all_cla.items() for k in i.split(';')])
#  #
#  test = \
#     {
#         {
#             '语文': {
#                 '1班': ['崔昊元', '贾靖程', '吴俊岳', '王浩羽', '吕梦丽', '牛皓冬', '张阔', '孙佳奇', '郑佳睦', '王孝天', '付一鸣', '李蓉轩', '陈观绅', '赵鑫博', '张子豪', '叶平'],
#                 '2班': ['侯文杰', '黄新之', '杨智恒', '杨悦昕', '刘洋', '靳馨娴', '白轶臣', '蒋文拓', '赵梓豪', '杨梓琦', '吕铭', '刘子豪']},
#             '政治': {
#                 '1班': ['崔昊元', '贾靖程', '吴俊岳', '王浩羽', '吕梦丽', '牛皓冬', '张阔', '孙佳奇', '郑佳睦', '王孝天', '付一鸣', '李蓉轩', '陈观绅', '赵鑫博', '张子豪', '叶平'],
#                 '3班': ['陈龙', '钱炳东', '黄文龙', '田亮', '林俊如', '付鹏洲', '朱震霆', '谢泽和', '刘燕玲', '苏丽莹', '苏樟林', '吴晓涛']}
#         }
#     }

# noinspection PyArgumentList
def exc_read(path):
    try:
        data = pd.read_excel(path)
        return data
    except ValueError:
        traceback.print_exc()
        raise Exception('您的excel表格中可能没有数据，请您核验一下。')


# """读取数据，获取人员名单""" 需要完善

def read_cou(cou=None):
    if not cou:
        data = {'cou': wk(exc_path()[0]).sheetnames}
        return data
    else:
        data = {'cou': cou}
        return data


# """ 获取科目 """ 需要完善

def read_red(red=None):
    if not red:
        data = {'red': [rdate.lesson(), '']}
        return data
    else:
        data = {'red': red}
        return data


# """ 获取课时 """ 需要完善

def read_cla(cla):
    """
    它读取命令行参数并返回参数字典

    :param cla: 命令行参数。
    """
    result = exc()
    data = {'cou': cla, 'cla': list(result[cla].keys())}

    return data


# """ 根据科目，获取它对应的哪些班级 """ 需要完善

def read_stu(stu):
    """ 根据班级，获取它对应的哪些学生 """
    result = exc()
    data = {'cla': stu, 'stu': []}
    for course, cs_dict in result.items():
        if stu in list(cs_dict.keys()):
            data['stu'] = cs_dict[stu]
            return data
    return data


# 需要完善

def read_stu_info():
    restu = configure.ini()['restu'][1]
    stu_info = []
    for k, v in restu.items():
        stu_info.append(v)

    #
    stu_dict = dict(zip(read_stu('1班')['stu'], stu_info))

    return stu_dict


# 需要完善

def Named(stu):
    student_file = stu.split(',')
    with open(exc_path()[1], 'a+', encoding='utf-8') as called_file:
        called_file.seek(0)
        called_students = called_file.readlines()

        not_called_list = list(set(student_file) - set([i.replace('\n', '') for i in called_students]))
        if not not_called_list:
            called_file.truncate(0)
            not_called_list.extend(student_file)
        name = random.choice(not_called_list)

        not_called_list.remove(name)

        called_file.writelines(name + '\n')
        return name


# 随机点名V1.0本地存储-save版 需要完善


if __name__ == '__main__':
    pass
