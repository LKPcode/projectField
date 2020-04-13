<template>
  <div class="fields">
    <Field v-for="field in store.fields.state.fields" :key="field.id" :field="field" />
  </div>
</template>

<script>
//import { mapGetters, mapActions } from "vuex";
import Field from "@/components/home/Field.vue";

export default {
  name: "Fields",
  data(){
    return{
      store: this.$testStore
    }
  },
  components: {
    Field
  },
  methods:{
    getFields(){
      this.$testStore.fields.getFields().then((response) => {
        if(response==200){
           this.$EventBus.$emit('notify', "Loaded Fields Successfully", "green");
        }else{
           this.$EventBus.$emit('notify', "Could not load fields", "red");
        }
      }).catch(() => {
        this.$EventBus.$emit('notify', "Something wierd happened", "yellow");
      });
    }
  },
  created(){
    this.getFields();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.fields {
  display: grid;
  grid-template-columns: 400px 400px 400px 400px;
  grid-template-rows: 300px 300px 300px;
  grid-gap: 20px;
  background-color: #fff;
  color: #444;
}

@media only screen and (max-width: 600px) {
  .fields {
    display: block;
    width: 100%;
    background-color: #ffff;
    color: #444;
  }
}
</style>