import os
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
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
    example_data.append((city_name, radius))

c = (
    Map()
    .add(
        "通勤半径",
        example_data,
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("map_china_cities.html")
)
