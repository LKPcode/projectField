<template>
<div>



 <transition name="slide-fade">
  <div  v-if="display" 
        :class="{   red: color=='red',
                    green: color=='green',
                    yellow: color=='yellow'}"
                    class="notification">
      <div class="icon">  </div>
      <div class="text"> {{text}}</div>
  </div>
 </transition>
</div>
</template>

<script>
export default {
  name: 'Notification',
  data(){
      return{
        display: false,
        text:"something",
        color: "yellow"
      }
  },
  methods:{
    sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
    }
  },
  created(){
    this.$EventBus.$on('notify', (text , color) => { 
          this.display = true;
          console.log("notification triggered:" + text + color);
          this.sleep(2000).then(() => { this.display = false;  });
          
          this.text = text;
          this.color = color; 
    });
  }
}
</script>

<style scoped>

.notification{
    display: flex;
    justify-content: center;
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 10000;
    border-radius: 10px;
}

.text{
  
    padding: 20px;
}

.red{
    background-color: rgba(226, 79, 79, 0.9);
}
.green{
    background-color: rgba(150, 226, 79, 0.9);
}
.yellow{
    background-color:  rgba(255, 245, 102, 0.9);
}



/* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-fade-enter-active {
  transition: all .5s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(20px);
  opacity: 0;
}
</style>
