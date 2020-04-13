<template>
  <div class="map-info">

<div class="area"> Κέρκυρα </div>

<table>
  <tr>
    <td>Location </td>
    <td> {{field.location}} </td>
  </tr>
  <tr>
    <td>Number of Trees</td>
    <td> {{ field.num_of_trees }}</td>
  </tr>
  <tr>
    <td>Tree Kind</td>
    <td> Olive Trees</td>
  </tr>
  <tr>
    <td> Surface Area </td>
    <td> {{field.surface_area}} m<sup> 2 </sup></td>
  </tr>
</table>



<div class="description"> Many good things this field has </div>

<ImageGalery />

  </div>
</template>

<script>
import ImageGalery from '@/components/field-info/ImageGalery.vue'


export default {
  name: "MapInfo",
  props:["field"],
  components:{
      ImageGalery
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped >
.map-info {
  background-color: #77753a;
  color: black;
  width: 100%;
  border-radius: 10px;
}
@media only screen and (max-width: 600px) {
  .map-info {
     overflow: hidden;
    height: 400px;
    width: 95%;
    margin: auto;
    margin-top: 20px;
    border-radius: 10px;
    background-color: #77753a;
    color: white;
  }
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  height: 30%;

  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

td, th {
  border: 1px solid white;
  text-align: left;
  padding: 8px;
}
td{
  width:50%;
}

tr:nth-child(even) {
  background-color: rgb(100,100,100, 0.6);
}
table tr:last-child {
   border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}
.description{
   
    font-size: .9rem;
    padding: 20px;
    height: 5%;
     z-index: 3;
}

.area{
    font-size: 1.4rem;
    text-align: center;
    padding: 30px;
    background-color:rgb(100,100,100, 0.6)
}


</style>