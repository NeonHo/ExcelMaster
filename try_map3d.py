import os
from pyecharts import options as opts
from pyecharts.charts import Map3D
from utils.BuildExcel import markdown_to_excel
from pyecharts.globals import ThemeType
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

markdown_path = os.path.join('projectCities', 'data', 'radius_cities.md')
with open(markdown_path, 'r') as f:
    markdown = f.read()
df = markdown_to_excel(
    markdown=markdown,
    file_path=os.path.join('projectCities', 'data', 'radius_cities.xlsx')
)



# 添加经纬度数据（手动定义）
city_coords = {
    '上海市': (121.4737, 31.2304),
    '重庆市': (106.9123, 29.4316),
    '北京市': (116.4074, 39.9042),
    '深圳市': (114.0579, 22.5431),
    '天津市': (117.2010, 39.0842),
    '广州市': (113.2644, 23.1291),
    '成都市': (104.0668, 30.5728),
    '大连市': (121.6186, 38.9140),
    '杭州市': (120.1551, 30.2741),
    '哈尔滨市': (126.5340, 45.8038),
    '南京市': (118.7969, 32.0603),
    '济南市': (117.1205, 36.6512),
    '沈阳市': (123.4315, 41.8057),
    '郑州市': (113.6253, 34.7466),
    '武汉市': (114.3052, 30.5928),
    '长沙市': (112.9388, 28.2282),
    '西安市': (108.9398, 34.3416),
    '苏州市': (120.5853, 31.2989),
    '昆明市': (102.8332, 24.8801),
    '佛山市': (113.1215, 23.0215),
    '青岛市': (120.3826, 36.0671),
    '东莞市': (113.7518, 23.0205),
    '宁波市': (121.5497, 29.8683),
    '乌鲁木齐市': (87.6168, 43.8256),
    '长春市': (125.3236, 43.8171),
    '厦门市': (118.0894, 24.4798),
    '石家庄市': (114.4995, 38.1006),
    '合肥市': (117.2272, 31.8206),
    '贵阳市': (106.6302, 26.6477),
    '常州市': (119.9740, 31.8110),
    '无锡市': (120.3119, 31.4910),
    '太原市': (112.5489, 37.8706),
    '福州市': (119.2965, 26.0745),
    '南昌市': (115.8581, 28.6820),
    '南宁市': (108.3663, 22.8177),
    '南通市': (120.8943, 31.9802),
    '温州市': (120.6994, 27.9943),
    '银川市': (106.2309, 38.4872),
    '兰州市': (103.8342, 36.0611),
    '徐州市': (117.2841, 34.2058),
    '西宁市': (101.7778, 36.6173),
    '绍兴市': (120.5802, 30.0303),
    '洛阳市': (112.4536, 34.6197),
    '呼和浩特市': (111.7510, 40.8415),
    '海口市': (110.1999, 20.0440)
}

example_data = []
for row in df.iterrows():
    city_name = row[-1].values[0]
    radius = float(row[-1].values[2])
    example_data.append((city_name, [city_coords[city_name][0], city_coords[city_name][1], radius]))

map3d = Map3D()

map3d.add_schema(
    itemstyle_opts=opts.ItemStyleOpts(color="rgba(0, 0, 0, 0)", opacity=1),
    map3d_label=opts.Map3DLabelOpts(
        is_show=False,
    ),
    light_opts=opts.Map3DLightOpts(
        main_color="#fff",
        main_intensity=1.2,
        is_main_shadow=False,
    ),
    view_control_opts=opts.Map3DViewControlOpts(
        projection="perspective",
        auto_rotate=True,
        auto_rotate_speed=10,
        zoom_sensitivity=1,
        rotate_sensitivity=1,
    ),
)


map3d = Map3D(
    init_opts=opts.InitOpts(
        theme=ThemeType.PURPLE_PASSION,
        width='900px',
        height='600px',
        bg_color='rgba(0, 0, 51, 1)'  # Dark blue background color
    )
)

map3d.add_schema(
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgba(75,0,130,0.5)",  # Dark purple color with transparency
            opacity=0.5,
            border_width=1,
            border_color="rgba(0,0,139,0.5)",  # Dark blue color with transparency
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
        ),
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            color="#fff",
            font_size=10,
            background_color="rgba(0,0,0,0.5)",  # Semi-transparent black
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#9370DB",  # Medium purple light
            main_intensity=1.5,
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=30,
            ambient_intensity=0.4,
        ),
).add(
    series_name="通勤半径",
    data_pair=example_data,
    type_=ChartType.BAR3D,
    bar_size=0.32,
    shading="realistic",  # More realistic shading
    label_opts=opts.LabelOpts(
        is_show=False,
    ),
    itemstyle_opts=opts.ItemStyleOpts(
        opacity=0.7,
    ),
).set_global_opts(
    title_opts=opts.TitleOpts(title="中国城市通勤半径", pos_top='3%', pos_left='center', title_textstyle_opts=opts.TextStyleOpts(color="#9370DB")),  # Medium purple title
    tooltip_opts=opts.TooltipOpts(
        formatter=JsCode("function(data){return data.name + ' 通勤半径：' + data.value[2];}"),
    ),
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        min_=20,
        max_=50,
        pos_left="left",
        pos_top="bottom",
        dimension=2,
    )
)


map3d.render("map3d_china_cities.html")