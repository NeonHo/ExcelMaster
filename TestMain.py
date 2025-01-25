import os
from utils.BuildExcel import markdown_to_excel
from projectCities.map3d import map3d
from pyecharts.globals import ChartType
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Map3D
from pyecharts.globals import ThemeType


def main():
    markdown_path = os.path.join('projectCities', 'data', 'radius_cities.md')
    with open(markdown_path, 'r') as f:
        markdown = f.read()
    df = markdown_to_excel(
        markdown=markdown,
        file_path=os.path.join('projectCities', 'data', 'radius_cities.xlsx')
    )
    
    list = []
    for row in df.iterrows():
        print(row)
        city_name = row[-1].values[0]
        radius = int(row[-1].values[2])
        list.append([city_name, [0, 0, radius]])
    
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
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
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
    ).add(
        series_name="bar3D",
        data_pair=list,
        type_=ChartType.BAR3D,
        bar_size=1,
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="中国城市通勤半径", pos_top='3%', pos_left='center'),
    ).render(
        path=os.path.join('projectCities', 'China3DwithBar3D.html')
    )
    

if __name__ == '__main__':
    main()
