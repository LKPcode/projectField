<template>
  <div class="map">
    <gmap-map
      :center="center"
      :zoom="15"
      style="width:100%;height: 100%;"
    >
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="center=m.position"
      ></gmap-marker>

        <gmap-polygon :paths="paths" :editable="true" @paths_changed="updateEdited($event)">
      </gmap-polygon>

    </gmap-map>
<!--
    <ul v-if="edited" @click="edited = null">
      <li v-for="path in edited" :key="path">
        <ol>
          <li v-for="point in path" :key="point">
            {{point.lat}}, {{point.lng}}
          </li>
        </ol>
      </li>
    </ul>
-->
  </div>
</template>

<script>
export default {
  name: "GoogleMap",
  data() {
    return {
      // default to Montreal to keep it simple
      // change this to whatever makes sense
      center: { lat: 1.380, lng: 103.810 },
      markers: [],
      places: [],
      currentPlace: null,

       edited: null,
          paths: [
            [ {lat: 1.380, lng: 103.800}, {lat:1.380, lng: 103.810}, {lat: 1.390, lng: 103.810}, {lat: 1.390, lng: 103.800} ],]
    };
  },


  methods: {
    // receives a place object via the autocomplete component

    updateEdited(mvcArray) {
            let paths = [];
            for (let i=0; i<mvcArray.getLength(); i++) {
              let path = [];
              for (let j=0; j<mvcArray.getAt(i).getLength(); j++) {
                let point = mvcArray.getAt(i).getAt(j);
                path.push({lat: point.lat(), lng: point.lng()});
              }
              paths.push(path);
            }
            this.edited = paths;
    }
  }
};
</script>

<style  scoped>
.map{
  width: 100%;
  height: 100%;
  padding: 0px;
  margin: 0px;
}

</style>