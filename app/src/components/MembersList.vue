<template>
  <div class="container">
    <b-table striped hover :items="members" :fields="fields"></b-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      fields: [
        { key: "name", label: "Nombre" },
        { key: "last_name", label: "Apellido" },
      ],
      members: [],
    };
  },
  methods: {
    getBooks() {},
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
