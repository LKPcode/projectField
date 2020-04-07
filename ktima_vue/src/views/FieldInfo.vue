<template>
  <div class="about">
    <Header />
    <div class="space"/>

   <div class="content">
     <div class="info">
       <MapInfo :field="getField"/>

       id: {{id}}
     </div>

     <div class="map">
       <Map/>

     </div>

   </div>



  </div>
  



</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Map from '@/components/field-info/Map.vue'
import MapInfo from '@/components/field-info/MapInfo.vue'
import { mapGetters, mapActions } from "vuex";




export default {
  name: 'FieldInfo',
  components: {
    Header,
    Map,
    MapInfo
   
  },
  data(){
    return{
      id: 1
    }
  },
  methods: {
    ...mapActions(["fetchField"])
  },
  computed: mapGetters(["getField"]),
  created() {
      this.id = this.$route.params.id;
      this.fetchField(this.id);
  },
}
</script>

<style scoped>
.space{
  height:50px;
}
.about{
  display:flex;
  flex-direction: column;
  height:100%;
}

.content{
  flex-grow: 2;
  display: flex;
  width:100%;
  background-color: aqua;
}

.info{
  height:100%;
  width: 30%;
  background-color: #77753a; 
  display:flex;
  flex-direction: column;
  justify-content: flex-start;

}
.map{ 
  background-color: #77753a;
  width:100%;
  height:100%;
}


@media only screen and (max-width: 600px) {
  .content{
    display:block;
  }
  .info{
    width: 100%;
  }

}


</style>