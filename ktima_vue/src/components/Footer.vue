<template>
  <div class="footer">
      <div class="logo"> LOGO </div>

      <div class="email" ><h3>Email: example@email.com</h3></div>

      <a class="topPage" href="#"><i class="fas fa-angle-up"></i></a>
    
  </div>
</template>

<script>
export default {
  name: 'Footer',

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.footer{
    margin: 0 0;
    padding: 0 0;
    position: relative;
    display:flex;
    width: 100%;
    height: auto;
    background-color: #000;
    justify-content: flex-end;
    align-items: stretch;
    z-index: 10;
}

.fas{
    color: #fff;
}

.email {
    margin-right: 40%;
}

h3 {
    color: #fff;
}

.logo{
    height: 100%;
    line-height: 50px;
    width: 200px;
    margin-right: auto;
    color: white;
    font-size: 1.8rem;
    font-weight: bold;
}
</style>
