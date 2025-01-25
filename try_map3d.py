import os
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode
from utils.BuildExcel import markdown_to_excel

markdown_path = os.path.join('projectCities', 'data', 'radius_cities.md')
with open(markdown_path, 'r') as f:
    markdown = f.read()
df = markdown_to_excel(
    markdown=markdown,
    file_path=os.path.join('projectCities', 'data', 'radius_cities.xlsx')
)

example_data = []
for row in df.iterrows():
    city_name = row[-1].values[0]
    radius = float(row[-1].values[2])
    example_data.append((city_name, [50.1, 50.1, radius]))


c = (
    Map3D().add(
        series_name="通勤半径",
        data_pair=example_data,
        maptype="china-cities",
        type_=ChartType.BAR3D,
        bar_size=1,
        shading="lambert",
        label_opts=opts.LabelOpts(is_show=False)
    ).set_global_opts(
        title_opts=opts.TitleOpts(title="中国城市"),
        visualmap_opts=opts.VisualMapOpts(),
    ).render(
        "map3d_with_bar3d.html"
    )
)
