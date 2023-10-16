<template>
  <div id="map">
    <l-map :zoom="13" :center="[35.6895, 139.6917]">
      <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
      <l-geo-json :geojson="geojsonData">
        <template v-slot:default="{ latLng }">
          <l-marker :lat-lng="latLng">
            <l-icon :icon-url="markerImg" :shadow-url="markerShadowImg" />
          </l-marker>
        </template>
      </l-geo-json>
    </l-map>
  </div>
</template>

<script>
import L from 'leaflet';
import { LMap, LTileLayer, LMarker, LIcon, LGeoJson } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';
import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import geojsonData from '@/assets/data/random_coordinates_in_japan.json'; // GeoJSONデータのインポート

// 複数ポイントをマーカー表示しようとしたら、Leafletライブラリのデフォルトのマーカー画像参照元が、うまく読み込めない画像を参照するようになってしまったため、デフォルト値を手動設定している。
// データ元：https://stackoverflow.com/questions/49441600/react-leaflet-marker-files-not-found
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon,
    LGeoJson
  },
  data() {
    return {
      markerImg: markerImg,
      markerShadowImg: markerShadowImg,
      geojsonData // インポートしたGeoJSONデータを使用
    }
  }
};
</script>

<style scoped>
#map {
  height: 400px;
  width: 100%;
}
</style>
