from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ThemeType


geo = Geo(
    init_opts=opts.InitOpts(
        theme=ThemeType.DARK,
        width='900px',
        height='600px',
    )
)

geo.add_schema(
    maptype='china',
    itemstyle_opts=opts.ItemStyleOpts(color='#000000', border_color='#1E90FF'),
    emphasis_label_opts=opts.LabelOpts(is_show=False),
    emphasis_itemstyle_opts=opts.ItemStyleOpts(color="#323c48")
).set_series_opts(
    label_opts=opts.LabelOpts(is_show=False)
).set_global_opts(
    title_opts=opts.TitleOpts(title="中国城市通勤半径", pos_top='3%', pos_left='center'),
    visualmap_opts=opts.VisualMapOpts()
).render('China.html')