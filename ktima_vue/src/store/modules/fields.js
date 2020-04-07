import axios from "axios";


const state = {
    fields : [{
        id: 1,
        location: "Corfu"
    },{
        id: 2,
        location: "Xios"
    },{
        id: 3,
        location: "Corfu"
    },{
        id: 4,
        location: "Corfu"
    },{
        id: 5,
        location: "Corfu"
    },{
        id: 6,
        location: "Corfu"
    },{
        id: 7,
        location: "Corfu"
    }]
};


const getters = {
    allFields: (state) => state.fields
};


const actions = {
    async fetchFields({commit}){
        const response  = await axios.get('http://localhost:9000/api/fields');
        console.log(response.data)
        commit("setFields" , response.data);
    }
};


const mutations = {
    setFields: (state, fields) => (state.fields = fields)
};


export default {
    state,
    getters,
    actions,
    mutations
};