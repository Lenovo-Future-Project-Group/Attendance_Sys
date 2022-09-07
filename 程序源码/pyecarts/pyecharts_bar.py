# pyecharts 的图上窜到HTML页面中

from random import randrange
from pyecharts.charts import Bar
from pyecharts import options as opts


def bar_base() -> Bar:
    data = (
        Bar()
        .add_xaxis(['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'])
        .add_yaxis('商家A', [randrange(0, 100) for _ in range(6)])
        .add_yaxis('商家B', [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title='Bar-基本示例', subtitle='我是副标题'))
    )
    return data


def get_bar_chart():
    data = bar_base()
    return data.dump_options_with_quotes()
