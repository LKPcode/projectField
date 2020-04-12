<template>
  <div class="home">
    <Header />

    <HomeSearch/>

    <div class="main-column">
        <Fields/>
    </div>

    <Footer />
  </div>
  



</template>

<script>
// @ is an alias to /src

import Header from '@/components/Header.vue'
import Fields from '@/components/home/Fields.vue'
import HomeSearch from '@/components/home/HomeSearch.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Fields,
    HomeSearch,
    Footer
  }
}
</script>

<style scoped>
.main-column{
  align-items: center;
  width: 100%;
  margin-top: 2%;
}



@media only screen and (max-width: 600px) {
  .main-column{
  width: 100%;
  margin: 20px auto;
  background-color: cadetblue;
}
}


</style>