<template>
  <div class="container">
    <div>
      <b-button v-b-modal.MemberAddModal variant="success"
        >Nuevo Miembro</b-button
      >
    </div>
    <div>
      <b-modal ref="MemberAddModalRef" id="MemberAddModal" :hide-footer="true">
        <h1>Gestion Miembros</h1>
        <b-form id="MemberAddForm" @reset="onReset">
          <b-form-group class="my-2" id="input-group-1">
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
            class="my-4"
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
          <div v-if="editing">
            <b-button variant="success" @click="edit(this.id)">Editar</b-button>
          </div>
          <div if-else>
            <b-button variant="success" @click="add">Registrar</b-button>
          </div>
        </b-form>
      </b-modal>
    </div>
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
    </div>
    <div v-else>Cargando..</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      editing: false,
      loading: true,
      fields: [
        { key: "identification", label: "Identificacion" },
        { key: "name", label: "Nombre" },
        { key: "last_name", label: "Apellido" },
        { key: "born_place", label: "Lugar Nacimiento" },
        { key: "company", label: "Empresa" },
        { key: "action", label: "Action" },
      ],
      id: "",
      identification: "",
      name: "",
      last_name: "",
      born_place: "",
      company: "",
    };
  },
  methods: {
    add() {
      this.editing = false;
      this.$store.dispatch("addMember", {
        identification: this.identification,
        name: this.name,
        last_name: this.last_name,
        born_place: this.born_place,
        company: this.company,
      });
      this.onReset();
      this.hideModal();
    },
    remove(id) {
      this.$store.dispatch("removeMember", id);
    },
    editMember(id) {
      this.editing = true;
      const member = this.$store.getters.getMember(id);
      if (member) {
        this.id = member.id;
        this.identification = member.identification;
        this.name = member.name;
        this.last_name = member.last_name;
        this.born_place = member.born_place;
        this.company = member.company;
        this.showModal();
      }
    },
    edit(id) {
      this.$store.dispatch("editMemeber", id, {
        identification: this.identification,
        name: this.name,
        last_name: this.last_name,
        born_place: this.born_place,
        company: this.company,
      });
      this.editing = false;
      this.onReset();
      this.hideModal();
    },
    hideModal() {
      this.$refs["MemberAddModalRef"].hide();
    },
    showModal() {
      this.$refs["MemberAddModalRef"].show();
    },
    onReset() {
      this.identification = "";
      this.name = "";
      this.last_name = "";
      this.born_place = "";
      this.company = "";
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

<style>
</style>