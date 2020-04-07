<template>
  <div class="fields">
    <Field v-for="field in allFields" :key="field.id" :field="field" />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Field from "@/components/home/Field.vue";

export default {
  name: "Fields",
  components: {
    Field
  },
  methods: {
    ...mapActions(["fetchFields"])
  },
  computed: mapGetters(["allFields"]),
  created() {
    this.fetchFields();
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