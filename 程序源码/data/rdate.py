import datetime


def date():
    """获取当前的年月日"""
    # 获取当地时间
    now = datetime.datetime.now()
    # return now.year, now.month, now.day
    return now.strftime('%Y%m%d')


def weekday():
    """ 获取当前是周几 """
    week = {'1': '周一', '2': '周二', '3': '周三', '4': '周四', '5': '周五', '6': '周六', '7': '周日', }
    weekdays = datetime.datetime.today().isoweekday()
    return week[str(weekdays)]


def lesson_info():
    """ 判断此时是第几节课 """
    # todo 需要完善
    #  问题：如果是课间进行的考勤，该如何进行判断？没想好，暂时弃用这种方法。
    #  每节课的时间段

    lessons_time = [{
        f'第1节课': ['08:30:00', '09:00:00'],
        f'第2节课': ['09:20:00', '09:50:00'],
        f'第3节课': ['10:20:00', '10:50:00'],
        f'第4节课': ['11:10:00', '11:40:00'],
        f'第5节课': ['14:00:00', '14:30:00'],
        f'第6节课': ['14:50:00', '15:20:00'],
    }]

    alist = []
    for i in lessons_time[0]:
        blist = lessons_time[0][i]
        alist.append(blist)

    now = datetime.datetime.now()
    today = str(datetime.date.today())

    # 判断此时是第几节课
    index = 0
    for time_zone in alist:
        index += 1
        start_time = datetime.datetime.strptime(f'{today} {time_zone[0]}', '%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strptime(f'{today} {time_zone[1]}', '%Y-%m-%d %H:%M:%S')

        if start_time < now < end_time:
            data = f'现在是第{index}节课'
            # print(data)
            return data, lessons_time[0]
    else:
        data = '现在是课余时间'
        # print(f'现在是课余时间')
        return data, lessons_time[0]


# todo 需要完善

def lesson():
    data = lesson_info()[0]
    lessons_time = [{f'{data}': ['00:00:00', '00:00:00']}]
    return list(lessons_time[0])[0]


# todo 需要完善

if __name__ == '__main__':
    test = lesson()
    print(test)
