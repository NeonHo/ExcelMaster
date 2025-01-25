from pyecharts.charts import Map3D
from pyecharts import options as opts
from pyecharts.globals import ThemeType


map3d = Map3D(
    init_opts=opts.InitOpts(
        theme=ThemeType.PURPLE_PASSION,
        width='900px',
        height='600px',
    )
)

map3d.add_schema(
    maptype='china',
    itemstyle_opts=opts.ItemStyleOpts(
        color='#323c48', 
        opacity=1,
        border_width=0.8,
        border_color='#1E90FF',
    ),
    light_opts=opts.Map3DLightOpts(
        main_color='#fff',
        main_intensity=1.2,
        main_shadow_quality='high',
        is_main_shadow=False,
        main_alpha=55,
        main_beta=10,
        ambient_intensity=0.3,
    ),
    view_control_opts=opts.Map3DViewControlOpts(
        center=[-10, 0, 10],
    ),
    post_effect_opts=opts.Map3DPostEffectOpts(
        is_enable=False,
    ),
).set_global_opts(
    title_opts=opts.TitleOpts(title="中国城市通勤半径", pos_top='3%', pos_left='center'),
)