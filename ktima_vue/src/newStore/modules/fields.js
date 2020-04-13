import axios from 'axios'
    
const fields = {
    state: {
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
        }],

        field:{}

    },
    async getField(id){
        try{
            const response = await axios.get("http://localhost:9000/api/fields/" + id);
            console.log(response.data)
            this.state.field = response.data[0];
            return response.status;
        }catch(error){
            console.log("Could not get field info with id:" + id);
            return error.response.status;
        }

    },
    async getFields(){
        try{
            const response = await axios.get("http://localhost:9000/api/fields/");
            console.log(response.data)
            this.state.fields = response.data;
            return response.status;
        }catch(error){
            console.log("Could not get fields: " + error.response.status);
            return error.response.status;
        }

    }

    /* Change the structure type of coordinates.
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
    */
    
  };
  
  export default fields