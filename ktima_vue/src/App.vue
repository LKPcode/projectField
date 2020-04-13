<template>
  <div id="app">
    <div id="nav">
      
    </div>
    <router-view/>

    <Notification/>
  </div>
</template>

<script>
import Notification from '@/components/Notification.vue'

export default {
  name:"App",
  components:{
    Notification
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height:100%;
}


body,html{
  margin: 0px;
  height:100%;
}


</style>
