<template>
  <div class="container">
    <div v-if="loading">
      <b-table striped hover :items="members" :fields="fields">
        <template v-slot:cell(action)="members">
          <b-button
            size="sm"
            variant="primary"
            @click="editMember(members.item.id)"
            >Editar</b-button
          >
          <b-button size="sm" variant="danger" @click="remove(members.item.id)"
            >Eliminar</b-button
          >
        </template>
      </b-table>
      <div>
        <b-form id="MemberAddForm">
          <b-form-group id="input-group-1">
            <b-form-input
              v-model="identification"
              id="identification"
              placeholder="Identificacion"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2">
            <b-form-input
              v-model="name"
              id="name"
              placeholder="Ingrese Nombre"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3">
            <b-form-input
              v-model="last_name"
              id="last_name"
              placeholder="Ingrese Apellido"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4">
            <b-form-input
              v-model="company"
              id="company"
              placeholder="Empresa"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-5"
            label="Lugar Nacimiento:"
            label-for="born_place"
          >
            <b-form-select v-model="born_place" id="born_place" required>
              <b-form-select-option
                v-for="city in cities"
                v-bind:key="city.id"
                :value="city.id"
                >{{ city.name }}</b-form-select-option
              >
            </b-form-select>
          </b-form-group>
          <b-button variant="success">Editar</b-button>
        </b-form>
      </div>
    </div>
    <div v-else>Cargando..</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,
      fields: [
        { key: "identification", label: "Identificacion" },
        { key: "name", label: "Nombre" },
        { key: "last_name", label: "Apellido" },
        { key: "born_place", label: "Lugar Nacimiento" },
        { key: "company", label: "Empresa" },
        { key: "action", label: "Action" },
      ],
      identification: "",
      name: "",
      last_name: "",
      born_place: "",
      company: "",
    };
  },
  methods: {
    remove(id) {
      this.$store.dispatch("removeMember", id);
    },
    editMember(id) {
      const member = this.$store.getters.getMember(id);
      if (member) {
        console.log(member);
        this.identification = member.identification;
        this.name = member.name;
        this.last_name = member.last_name;
        this.born_place = member.born_place;
        this.company = member.company;
      }
    },
  },
  computed: {
    members() {
      return this.$store.getters.getMembers;
    },
    cities() {
      return this.$store.getters.getCities;
    },
  },
  mounted() {
    this.$store.dispatch("addMembers");
    this.$store.dispatch("addCities");
  },
};
</script>

<style scoped lang="scss">
</style>
