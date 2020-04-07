<template>
  <div class="image-galery">
    <img class="image" src="../../public/trees.jpeg" />
    <img src="../../public/trees2.jpg" />
    <img src="../../public/trees.jpeg" />
    <img src="../../public/trees.jpeg" />
    <img src="../../public/trees.jpeg" />
  </div>
</template>

<script>
export default {
  name: "ImageGalery"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped >
.image-galery {
  margin: 30px;
  height: 200px;
  overflow: auto;
  border: 2px solid white;
  margin-top: auto;
}
img {
  width: 100%;
}
.header {
  top: 0px;
  left: 0px;
  text-align: center;
  opacity: 0.5;
}
</style>