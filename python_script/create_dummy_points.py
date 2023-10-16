import json
import random

# 日本の主要な緯度経度範囲
LAT_MIN, LAT_MAX = 35.0, 36.5
LON_MIN, LON_MAX = 138.5, 140.5

# ポイントの数
NUM_POINTS = 10000

# GeoJSONオブジェクトの初期化
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# ランダムなポイントを生成
for _ in range(NUM_POINTS):
    lat = random.uniform(LAT_MIN, LAT_MAX)
    lon = random.uniform(LON_MIN, LON_MAX)
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat]
        }
    }
    geojson["features"].append(feature)

# GeoJSONファイルに書き込み
with open(r'./../src/assets/data/random_coordinates_in_japan.json', 'w') as f:
    json.dump(geojson, f)
