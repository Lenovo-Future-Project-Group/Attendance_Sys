import os
import re


def ini_read(path):
    """读取数据，验证数据状态"""
    try:
        with open(path, 'r+', encoding='utf-8', errors='ignore') as f:
            f.read()
    except ValueError:
        raise Exception('您的配置文件中可能没有数据，请您核验一下。')


# todo 数据验证 需要完善

def ini_path():
    """读取数据，判断文件路径"""
    try:
        ini_read(os.path.abspath('.') + r'/0-说明文档和配置文档/配置文档.txt')
        return os.path.abspath('.') + r'/0-说明文档和配置文档/配置文档.txt'
    except FileNotFoundError:
        ini_read(os.path.abspath('../..') + r'/0-说明文档和配置文档/配置文档.txt')
        return os.path.abspath('../..') + r'/0-说明文档和配置文档/配置文档.txt'


# todo 路径判断 需要完善

def ini():
    with open(ini_path(), 'r+', encoding='utf-8', errors='ignore') as f:
        content = f.read()

        usall = re.findall('【(.*?)】', content, re.S)

        # print(i)

    def ini_info(data_info):
        data_in = re.findall(data_info, content, re.S)
        dict_to_str = ' '.join(data_in)

        dict_info = {}
        for x in dict_to_str.strip('\n').split('\n'):
            if not x.strip():
                continue
            j = x.split('、')
            dict_info[j[0]] = j[1]
        return dict_to_str, dict_info

    # todo re'正则'插件 数据读取 需要完善

    error = [ini_info('考勤异常配置：(.*?)注意：.*【异常配置】')[0], ini_info('考勤异常配置：(.*?)注意：.*【异常配置】')[1]]

    infor = [ini_info('考勤课时配置：(.*?)注意：.*【课时配置】')[0], ini_info('考勤课时配置：(.*?)注意：.*【课时配置】')[1]]

    data = {'error': error, 'infor': infor, 'usall': usall}

    return data


# todo 配置信息 需要完善

def ini_save(old_str, new_str):
    """ 保存修改 """
    with open(ini_path(), 'r+', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        save = content.replace(old_str, new_str)
        f.seek(0)
        f.write(save)


if __name__ == '__main__':
    test = ini()
    print(test)
