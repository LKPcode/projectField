import Vue from 'vue'
import App from './App.vue'
import router from './router'
//import store from './store'
import 'leaflet/dist/leaflet.css';

import testStore from './newStore'

Vue.config.productionTip = false


Vue.prototype.$testStore = testStore

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
