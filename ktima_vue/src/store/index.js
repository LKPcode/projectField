import Vue from 'vue'
import Vuex from 'vuex'
import fields from './modules/fields'
import fieldInfo from './modules/field-info'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    fields,
    fieldInfo
  }
})
