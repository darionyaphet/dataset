
import json
from pyecharts.charts import Geo
from pyecharts import options as opts

from load_json import Province, City, load_response

resp = load_response()

confirmed = []
province = [Province(province) for province in resp['data']['listByArea']]

for p in province:
    confirmed.append((p.name[0:2], p.confirmed))

geo = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "China",
            confirmed,
            )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Confirmed"))
        )

geo.render()
