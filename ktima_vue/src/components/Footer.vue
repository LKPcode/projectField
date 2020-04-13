<template>
  <div class="footer">
      <div class="logo"> LOGO </div>

      <div class="email" ><h3>Email: example@email.com</h3></div>

      <a class="topPage" href="#"><img src="../../public/TopPage.png"></a>
    
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
    position: relative;
    display:flex;
    width: 100%;
    height: auto;
    background-color: #000;
    justify-content: flex-end;
    align-items: stretch;
    z-index: 10;
    
}

.topPage:after {
    transition: 5ms;
}

.topPage  img{
    height: 60px;
    background-color: #000;
    border-radius: 30%;
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
