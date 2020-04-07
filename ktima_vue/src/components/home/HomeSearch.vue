<template>


  <div class="home-search">
    <div class="center"> 
      <div class="icon"> S </div>
      <input type="text" class="search" placeholder="Search Field" >   
    </div>
  </div>

 

</template>

<script>
//import {mapGetters , mapActions} from 'vuex'

export default {
  name: 'HomeSearch'

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.home-search{
    background-image: url("../../../public/trees2.jpg");
    margin-top: 50px;
    width: 100%;
    height: 400px;
}
.center{
  display:flex;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 300px;
  z-index: 1;
  background-color: aliceblue;
  padding: 5px;
  border-radius: 30px;
  border: 1px solid gray;
}

.search{
  width: 80%;
  border: none;
  background-color: aliceblue;
  padding: 10px;
  outline: none;
}
.icon{
  margin: auto 10px;
}
</style>