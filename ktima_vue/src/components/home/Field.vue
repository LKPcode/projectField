<template>
  <div class="field">



<div class="img"> 
   <router-link class="router-link info" :to="{ name: 'FieldInfo', params: { id: field.id } }" >Field</router-link>
</div>

<div class="description"> Many good things this field has </div>

<table>
  <tr>
    <td>Location </td>
    <td>
     {{field.location}} 
    </td>
  </tr>
  <tr>
    <td>Number of Trees</td>
    <td> {{field.num_of_trees}} </td>
  </tr>
  <tr>
    <td>Tree Kind</td>
    <td> Olive Trees id:  {{ field.id }}</td>
  </tr>
  <tr>
    <td> Surface Area </td>
    <td> {{ field.surface_area }} m<sup> 2 </sup></td>
  </tr>
</table>



  </div>
</template>

<script>
export default {
  name: "Field",
  props: {
    field: Object
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped >
.field {
   overflow: hidden;
  border-radius: 10px;
  background-color: #77753a;
  color: black;
  height: 100%;
  width: 100%;
    display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
@media only screen and (max-width: 600px) {
  .field {
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
  padding: 3px;
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
    padding: 10px;
    height: 5%;
    background-color: #6b6b53;
     z-index: 3;
}
.img{
  position:relative;
  height: 55%;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;;
    background-image: url("../../../public/trees.jpeg");
  background-position: center;
  background-size: cover;
  transition: all .5s;
}
.img:hover{
  background-color: rgba(52, 73, 94, 0.75);
   transform: scale(1.2);
}
.info{
   position: absolute;
   width: 30%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  padding: 10px;
  border: 2px solid whitesmoke;
  display:none;
  cursor: pointer;
}
.info:hover{
  border-color: white;
}
.img:hover .info{
  display:block;
}

.area{
  position: relative;
  width: 100%;
  height: 50px;
  background-color: rgb(100,100,100, 0.8);
  top: 18px;
  z-index: 3;
}

</style>