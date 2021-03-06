import Vue from 'vue'
import App from './App.vue'
import router from './router'
//import store from './store'
import 'leaflet/dist/leaflet.css';
import * as VueGoogleMaps from "vue2-google-maps";

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyDeBnxUhnelwB7qeJGQ4BdghrGP-1pupeg",
    libraries: "places" // necessary for places input
  }
});

import testStore from './newStore'

Vue.config.productionTip = false

const EventBus = new Vue();
Vue.prototype.$EventBus = EventBus;

Vue.prototype.$testStore = testStore;

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
