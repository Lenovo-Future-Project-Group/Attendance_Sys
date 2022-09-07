from pyecarts import pyecharts_bar
from data import rdata, excel, images
from utils import configure, illustrate
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def os_run():
    app.run(debug=True)


@app.route('/')
def os_app():
    return redirect(url_for('os_home'))


# todo 程序初始化 需要完善

@app.route('/home/')
def os_home():
    cou = request.args.get('course')

    red = request.args.get('redate')

    if not cou:
        cou = excel.read_cou()['cou'][0]  # 默认 语文

    if not red:
        red = excel.read_red()['red'][0]  # 默认 系统

    Bar_options = pyecharts_bar.base()

    Cloud_options = pyecharts_bar.wordcloudpic()

    data = \
        {
            'reinix': illustrate.ini(),  # 说明文档
            'reiniy': configure.ini(),  # 配置文档
            'images': images.images(),  # 照片和个人简介
            'redata': excel.exc()[cou],  # 班级和学生信息
            'recous': excel.read_cou()['cou'],  # 所有课程
            'recour': excel.read_cou(cou)['cou'],  # 当前请求的课程
            'reclas': excel.read_cla(cou)['cla'],  # 当前请求的班级
            'rsdate': excel.read_red(red)['red'],  # 当前请求的课时
            'Bar_options': Bar_options.dump_options(),  #
            'Cloud_options': Cloud_options.dump_options(),  # 词云图

        }

    # print(data)
    return render_template('index.html', data=data)


# todo 初始页面 需要完善


@app.route('/index/')
def os_index():
    cou = request.args.get('course')

    red = request.args.get('redate')

    if not cou:
        cou = excel.read_cou()['cou'][0]  # 默认 语文

    if not red:
        red = excel.read_red()['red'][0]

    Bar_options = pyecharts_bar.base()

    Cloud_options = pyecharts_bar.wordcloudpic()

    data = \
        {
            'reinix': illustrate.ini(),  # 说明文档
            'reiniy': configure.ini(),  # 配置文档
            'images': images.images(),  # 照片和个人简介
            'redata': excel.exc()[cou],  # 班级和学生信息
            'recous': excel.read_cou()['cou'],  # 所有课程
            'recour': excel.read_cou(cou)['cou'],  # 当前请求的课程
            'reclas': excel.read_cla(cou)['cla'],  # 当前请求的班级
            'rsdate': excel.read_red(red)['red'],  # 当前请求的课时
            'Bar_options': Bar_options.dump_options(),  #
            'Cloud_options': Cloud_options.dump_options(),  # 词云图

        }

    # print(data)
    return render_template('index.html', data=data)


# todo 考勤页面 需要完善

@app.route('/get_cla/<cla>/', methods=['GET', 'POST'])
def os_get_read(cla):
    if request.method == 'POST':
        return \
            f'<script>' \
            f'alert("现在是[POST]请求，请求有误，请联系联想班学员处理。");' \
            f'window.location.href = "/home/#section-attendance";' \
            f'</script>'
    else:
        data = excel.read_stu(cla)

    return data


# todo 获取班级 路由 需要完善

@app.route('/get_nam/<stu>/', methods=['GET', 'POST'])
def os_get_name(stu):
    if request.method == 'POST':
        # data = request.form.to_dict()
        return \
            f'<script>' \
            f'alert("现在是[POST]请求，请求有误，请联系联想班学员处理。");' \
            f'window.location.href = "/home/#section-attendance";' \
            f'</script>'

    if request.method == 'GET':
        name = excel.Named(stu)
        return name
    return redirect(url_for('os_index'))


# todo 随机点名 Form 需要完善

@app.route('/submit_kq_data/', methods=['GET', 'POST'])
def os_index_submit_data():
    if request.method == 'GET':
        return \
            f'<script>' \
            f'alert("现在是[GET]请求，请求有误，请联系联想班学员处理。");' \
            f'window.location.href = "/home/#section-attendance";' \
            f'</script>'

    if request.method == 'POST':
        data = request.form.to_dict()
        # 将数据保存到excel
        rdata.data_save_info(data)
        return \
            f'<script>' \
            f'alert("数据已保存到[考勤总表]。");' \
            f'window.location.href = "/home/#section-attendance";' \
            f'</script>'
    return redirect(url_for('os_index'))


# todo 数据保存 Form 需要完善

@app.route('/submit_kq_inis/', methods=['GET', 'POST'])
def os_index_submit_inis():
    """ 接收提交的配置信息，并保存到配置文件中 """
    old_data = configure.ini()  # 读取原配置，方便后面做对比
    old_sett = \
        {
            'error': old_data['error'][0],
            'infor': old_data['infor'][0],

        }
    if request.method == 'GET':
        return \
            f'<script>' \
            f'alert("现在是[GET]请求，请求有误，请联系联想班学员处理。");' \
            f'window.location.href = "/home/#section-attendance";' \
            f'</script>'

    if request.method == 'POST':
        new_sett = request.form.to_dict()
        # 判断原设置数据和提交上来的配置数据是否相同
        # 如果不同，则按照提交配置进行更改
        for k, v in new_sett.items():
            # 如果配置相同，则无需更改，跳过
            if old_sett[k].replace('\n', '') == new_sett[k].replace('\r', '').replace('\n', ''):
                continue
            # 不同的数据，判断是哪些地方不同
            # 如果是考勤情形不同，则修改考勤内容
            # 如果是上课情形不同，则修改上课情形
            v = ''.join(('\n', v, '\n')).replace('\r', '')
            # 恢复UTF-8的数据格式并更新配置文件
            configure.ini_save(old_sett[k], v)
    return redirect(url_for('os_index'))


# todo 配置保存 Form 需要完善

if __name__ == '__main__':
    app.run(debug=True)
