<template>
  <div class="about">
    <Header />
    <div class="space"/>

   <div class="content">
     <div class="info">
       <MapInfo :field="state.field"/>

       id: {{id}}
     </div>

     <div class="map">
       <GoogleMap />

     </div>

   </div>
   


  </div>
  



</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import GoogleMap from '@/components/field-info/GoogleMap.vue'
import MapInfo from '@/components/field-info/MapInfo.vue'


export default {
  name: 'FieldInfo',
  components: {
    Header,
    GoogleMap,
    MapInfo
  },
  data(){
    return{
      id: 1,
      state: this.$testStore.fields.state
    }
  },
  methods:{
    getField(id){
      this.$testStore.fields.getField(id).then((response)=>{
        if(response==200){
          this.$EventBus.$emit('notify', "Loaded Field Successfully", "green");
        }else{
          this.$EventBus.$emit('notify', "There was an error loading this field", "red");
        }
      }).catch(()=>{
        this.$EventBus.$emit('notify', "Something wierd happened", "yellow");
      });
    }
  },
  created() {
      this.id = this.$route.params.id;
      this.getField(this.id);
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