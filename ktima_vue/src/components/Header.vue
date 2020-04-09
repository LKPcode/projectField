<template>
  <div class="header">
      <div class="logo" > L O G O </div>

    <router-link class="router-link" to="/">Home</router-link> 
    <router-link class="router-link" to="/register">Register</router-link>
  </div>
</template>

<script>
export default {
  name: 'Header',
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header{
    position: fixed;
    top:0px;
    left: 0px;
    display:flex;
    width: 100%;
    height: 50px;
    background-color: #77753a;
    justify-content: flex-end;
    align-items: stretch;
    z-index: 10;
    
}
.router-link{
  color: white;
  font-weight: bold;
  padding: 15px 20px;
  text-align: center;

}
.router-link:hover{
  background-color: rgba(100,100,100, 0.2);
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
