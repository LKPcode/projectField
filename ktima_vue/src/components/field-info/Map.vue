<template>
  <div style="height: 100%; width: 100%; z-index:0; border-radius: 10px;">
  
    <l-map
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: 100%; width:100%;border-radius: 10px;"
       @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
        <l-polygon :lat-lngs="coordinates" :color="polygon.color"></l-polygon>

    </l-map>
   
  </div>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LPolygon } from "vue2-leaflet";

export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LPolygon
  },
  props:["coordinates"],
  data() {
    return {
      zoom: 7,
      center: latLng(38.33303882235456, 23.1489082826517),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    
      showParagraph: false,

      currentZoom: 13,
      currentCenter: latLng(47.41322, -1.219482),

      mapOptions: {
        zoomSnap: 0.5
      },
     polygon: {
        latlngs: this.coordinates,
        color: 'green'
      },
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
     // console.log(this.currentCenter);
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    innerClick() {
      alert("Click!");
    },

  },
 
  created(){
    this.zoomUpdate(5);
    //this.polygon.latlngs = this.coordinates
  
  }
};
</script>