import axios from "axios";


const state = {

    field : 0

};


const getters = {
    getField: (state) => state.field
};


const actions = {
    async fetchField({commit} , id){
        const response  = await axios.get("http://localhost:9000/api/fields/" + id );
        console.log(response.data)
        commit("setField" , response.data);
    }
};


const mutations = {
    setField: (state, field) => (state.field = field)
};


export default {
    state,
    getters,
    actions,
    mutations
};