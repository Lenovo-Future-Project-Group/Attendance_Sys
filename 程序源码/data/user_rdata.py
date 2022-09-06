import os
import traceback

import pandas as pd
from openpyxl import load_workbook as wk
from openpyxl.styles import Font as fuck

from data import user_rdate


# import user_rdate


def data_path():
    try:
        data_read(os.path.abspath('.') + r'/2-考勤结果/考勤总表.xlsx')
        return os.path.abspath('.') + r'/2-考勤结果/考勤总表.xlsx'
    except FileNotFoundError:
        data_read(os.path.abspath('../..') + r'/2-考勤结果/考勤总表.xlsx')
        return os.path.abspath('../..') + r'/2-考勤结果/考勤总表.xlsx'


# todo

# noinspection PyArgumentList
def data_read(path):
    try:
        data = pd.read_excel(path)
        return data
    except ValueError:
        traceback.print_exc()
        raise Exception('您的excel表格中可能没有数据，请您核验一下。')


# todo

def data_conv(data):
    """
    将数据转成下面这种格式 :
    {
        'courrse':'语文',
        'date':'第一节课',
        '考勤情况': {
            '1班':{'崔昊元':'考勤正常', '张子豪':'迟到', '牛皓冬':'考勤正常'},
            '2班':{'杨梓琦':'考勤正常', '刘子豪':'迟到', '蒋文拓':'考勤正常'}
        }
    }
    """
    result = {'cour': data['cour'], 'date': data['date'], '考勤情况': {}}
    classes = []

    for k, v in data.items():
        if 'user' in k:
            classes.append(k.split('-')[1])

    for cla in list(set(classes)):
        result['考勤情况'][cla] = {}

    for k, v in data.items():
        if 'user' in k:
            cla = k.split('-')[1]  # 班级
            stu = k.split('-')[2]  # 学生
            result['考勤情况'][cla][stu] = v
    return result


# todo 需要完善

def data_save(data, path):
    """ 使用openpyxl保存数据到excel """
    # 表头
    work_book = wk(path)
    work_save = work_book[data['cour']]  # {'cour”:'kemu', '考勤情况':{'stu':考勤情况, 'stu':'大傻',""}}
    work_save.insert_cols(3)  # 将新的一列插入到第3列
    list_ws = list(work_save)

    def title():
        title_info = f'{user_rdate.date()}{user_rdate.weekday()}-{data["date"]}'
        return title_info

    for row in list_ws:
        cls = row[0].value
        stu = row[1].value
        if cls == '班级':
            row[2].value = title()
            continue

        if not cls:
            break

        if cls in list(data['考勤情况'].keys()):
            kq_sit = data['考勤情况'][cls][stu]
            row[2].value = kq_sit
            if kq_sit != '考勤正常':
                row[2].font = fuck(color='FF0000')

    work_book.save(path)


# todo 需要完善

def data_save_info(data):
    """ 将考勤数据保存到excel """
    data_info = data_conv(data)
    data_save(data_info, data_path())


# todo 需要完善

if __name__ == '__main__':
    test_data = {'date': '早读', 'user-1班-崔昊元': '考勤正常', 'user-1班-贾靖程': '请假', 'user-1班-吴俊岳': '旷课',
                 'user-1班-王浩羽': '考勤正常', 'user-1班-吕梦丽': '考勤正常', 'user-1班-牛皓冬': '考勤正常',
                 'user-1班-张阔': '做核酸', 'user-1班-孙佳奇': '考勤正常', 'user-1班-郑佳睦': '考勤正常',
                 'user-1班-王孝天': '考勤正常', 'user-1班-付一鸣': '考勤正常', 'user-1班-李蓉轩': '考勤正常',
                 'user-1班-陈观绅': '考勤正常', 'user-1班-赵鑫博': '考勤正常', 'user-1班-张子豪': '考勤正常',
                 'user-1班-叶平': '请假', 'cour': '语文'}
    data_save_info(test_data)
