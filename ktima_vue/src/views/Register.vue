<template>
  <div class="register">
    <Header />
    <div class="space" />

    <div class="content">
      <div class="left login-side-image">
        <div class="login-side-image-2"></div>
      </div>

      <div class="right">
          <div class="login-header">
              <div class="login-logo"></div>
              <div class="login-text-header">Welcome to LOGO</div>
            </div>
          
          <div class="login-form" v-if="state_login == true">
          
<div class="wrap-inputs">
            <div class="email-input">
              <i class="fas fa-envelope login-icon" aria-hidden="true"></i>
              <input
                v-model="login.email"
                type="text"
                placeholder="Enter Email or Username"
                name="email"
                class="text-email"
                required
              />
            </div>
            <div class="email-input">
              <i class="fas fa-key login-icon" aria-hidden="true"></i>
              <input
                v-model="login.password"
                type="password"
                placeholder="Enter Password"
                name="psw"
                class="text-email"
                required
              />
            </div>

            <div class="login-options">
              <div class="signup-referal" @click="toggle()">Create an account</div>
              <button class="join-sugestion-btn" @click="sign_in()">LOG IN</button>
            </div>
</div>
           
          </div>

          <div class="login-form" v-else>
         
<div class="wrap-inputs">
            <div class="email-input">
              <i class="fas fa-envelope login-icon" aria-hidden="true"></i>
              <input
                v-model="register.email"
                type="text"
                placeholder="Enter Email or Username"
                name="email"
                class="text-email"
                required
              />
            </div>
            <div class="email-input">
              <i class="fas fa-key login-icon" aria-hidden="true"></i>
              <input
                v-model="register.password_1"
                type="password"
                placeholder="Enter Password"
                name="psw"
                class="text-email"
                required
              />
            </div>
            <div class="email-input">
              <i class="fas fa-envelope login-icon" aria-hidden="true"></i>
              <input
                v-model="register.password_2"
                type="text"
                placeholder="Enter Password again"
                name="email"
                class="text-email"
                required
              />
            </div>

            <div class="login-options">
              <div class="signup-referal" @click="toggle()">Log In</div>
              <button class="join-sugestion-btn" >Create Account</button>
            </div>
</div>
           
          </div>
        
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import Header from "@/components/Header.vue";
import axios from 'axios'

export default {
  name: "Register",
  components: {
    Header
  },
  data() {
    return {
      state_login: true,
      register:{
        email:"",
        password_1: "",
        password_2: ""
      },
      login:{
        email:"",
        password: ""
      }
    };
  },
  methods: {
    toggle() {
      this.state_login = !this.state_login;
    },

  sign_in(){
    //var data = JSON.stringify({ username:this.login.email , password:this.login.password })
    axios.post("http://localhost:9000/api/api-token-auth/", {username: this.login.email , password: this.login.password })
    .then(function(response){
      console.log(response.data.token);
      document.cookie = "token=" + response.data.token;
      
    }).catch(error => {
      console.log(error.response)
    });




  },
  sign_up(){

  }
    },
};
</script>

<style scoped>
.space {
  height: 50px;
}
.register {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.content {
  flex-grow: 2;
  display: flex;
  width: 100%;
  background-color: whitesmoke;
}

.left {
  height: 100%;
  width: 30%;
  background-color: #433a77;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.right {
  background-color: whitesmoke;
  width: 100%;
  height: 100%;
  padding-left: 50px;
}



.wrap-inputs{
    width: 40%;
}


.join-sugestion-btn {
    width: 50%;
  background-color: gainsboro;
  
  color: black;
  border-radius: 5px;
  font-size: 0.8rem;
}
.join-sugestion-btn:hover {
  background-color: white;
}

.login-side-image {
  width: 20%;
  background-color: #77753a;
  
  border-bottom-right-radius: 0px;
  border: 2px solid black;
  background-image: url("../../public/trees2.jpg");
}
.login-form {
  width: 100%;
  border-radius: 0px 5px 5px 0px;
}

.email-input {
  padding: 10px;
  margin: auto;
  display: flex;
}
.text-email {
  padding: 6px;
  padding-left: 5px;
  padding-right: 40px;
  margin: 0px;
  border-radius: 5px;
  width: 100%;
 
}
.text-email:focus {
  border: 2px solid white;
}
.login-side-image-2 {
  position: relative;
  display: none;
  top: 100px;
  left: 25px;
  width: 55%;
  height: 55%;
  background-color: aqua;
  border-radius: 80% 10%;
  border: 2px solid black;
}
.login-header {
  padding: 30px;
  display: flex;
}
.login-icon {
  margin: 5px;
  margin-right: 10px;
  color: dodgerblue;
}
.login-logo {
  width: 60px;
  height: 60px;
  margin: 15px;
  background-color: #77753a;
  border: 2px solid black;
  border-radius: 50%;
  -webkit-transition: width 2s;
  transition: transform 2s, width 2s, height 2s;
}
.right:hover .login-logo {
  transform: rotateY(360deg);
  height: 80px;
  width: 80px;
}
.login-text-header {
  color: black;
  text-align: center;
  margin: auto;
  font-size: 1.4rem;
  margin-left: 0px;
}
#login-btn {
  width: 100px;
  text-align: center;
  margin-right: 115px;
  margin-top: 5px;
}
.fa-times-circle {
  float: right;
  margin: 10px 10px;
  font-size: 1.5rem;
  color: gray;
}
.fa-times-circle:hover {
  color: white;
}
#login-popup-id {
  display: none;
}
#login-message {
  position: relative;
  top: 80px;
  left: 10px;
  width: 80%;
  margin: 10px 20px;
  background-color: red;
}
.login-options {
  display: flex;
  padding:10px;


}
.signup-referal {
  font-size: 0.8rem;
  text-align: left;
  margin: 10px ;
  margin-left: 20px;
  color: dodgerblue; 
  width: 50%;
  cursor: pointer;
}
.signup-referal:hover {
  text-decoration: underline;
 
}







@media only screen and (max-width: 600px) {
  .content {
    display: block;
  }
  .left {
    width: 100%;
    display: none;
  }
  .right{
      padding-left: 0px;
  }
  .login-text-header {
      font-size: 1.5rem;
 
  }

.wrap-inputs{
    width: 95%;
}
}
</style>