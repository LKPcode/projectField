import axios from "axios";


const state = {

    field : 0,
    coordinates: 0

};


const getters = {
    getField: (state) => state.field,
    getCoordinates: (state) => state.coordinates
};


const actions = {
    async fetchField({commit} , id){
        const response  = await axios.get("http://localhost:9000/api/fields/" + id );
        //console.log(response.data)
        commit("setField" , response.data);
    },
    async fetchCoordinates({commit} , id){
        const response  = await axios.post("http://localhost:9000/api/field_xy", {id: id});
        console.log(response.data)

        var list = []
        var coo = []
        var coordinates = response.data
        console.log(response.data)
        for(var i=0; i< coordinates.length; i++ ){
          coo.push(parseFloat(coordinates[i]["world_x"]))
          coo.push(parseFloat(coordinates[i]["world_y"]))
          list.push(coo)
         
          console.log(coo)
           coo = []
        }
        console.log(list)


        commit("setCoordinates" , list);
    }
};


const mutations = {
    setField: (state, field) => (state.field = field),
    setCoordinates: (state, coordinates) => (state.coordinates = coordinates)
};


export default {
    state,
    getters,
    actions,
    mutations
};