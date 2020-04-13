<template>
  <div class="User">
      <div class="UserInfo">
          <img class="profile-image" src="../../../public/profile.jpg">
          <em><h2 class="name"> Name: Stelios Zaoudis</h2></em>
          <em><h2 class="name"> Fields Registered: 2</h2></em>
      </div>
  </div>
</template>

<script>
export default {
    name: "ProfileInfo"
}
</script>

<style scoped>
    .User{
        background-color: rgb(216, 216, 216);
    }

    h2{
        margin: 0;
        transition: font-size 0.5s, color 0.2s;
    }

    h2:hover{
        font-size: 200%;
        color: rgb(0, 0, 0);
    }

    .name {
        display: flexbox;
        align-content: left;
        color: rgb(46, 46, 46);
    }
    

    .profile-image{
        border-radius: 20%;
        width: 10%;
        padding-top: 0.3%;
        transition: width 0.5s;
    }

    .profile-image:hover{
        width: 11%;
        
    }
</style>