<template>
  <div id="map">
    <l-map :zoom="13" :center="[35.6895, 139.6917]">
      <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
      <l-marker :lat-lng="[35.6895, 139.6917]">
        <l-icon
          :icon-url="markerImg"
          :shadow-url="markerShadowImg"
        />      
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css';
import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon  
  },
  data(){
    return {
      markerImg : markerImg,
      markerShadowImg : markerShadowImg
    }
  },  
}
</script>

<style scoped>
#map {
  height: 400px;
  width: 100%;
}
</style>