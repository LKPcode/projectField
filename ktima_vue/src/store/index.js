import Vue from 'vue'
import Vuex from 'vuex'
import fields from './modules/fields'
import fieldInfo from './modules/field-info'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    token: "",
    isLoggedIn: false
  },
  mutations: {
    toggleStatus(state){
      state.isLoggedIn = !state.isLoggedIn;
    }
  },
  actions: {
  },
  modules: {
    fields,
    fieldInfo
  }
})
