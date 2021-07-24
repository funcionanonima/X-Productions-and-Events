<template>
  <div class="d-flex align-items-center">
    <b-button v-b-modal.memberAddModal variant="primary">Nuevo</b-button>
    <div>
      <b-modal
        ref="memberAddModalRef"
        id="memberAddModal"
        title="Nuevo Miembro"
        :hide-footer="true"
      >
        <b-form id="MemberAddForm">
          <b-form-group class="m-2" id="input-group-1">
            <b-form-input
              v-model="member.identification"
              id="identification"
              placeholder="Identificacion"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group class="m-2" id="input-group-2">
            <b-form-input
              v-model="member.name"
              id="name"
              placeholder="Ingrese Nombre"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group class="m-2" id="input-group-3">
            <b-form-input
              v-model="member.last_name"
              id="last_name"
              placeholder="Ingrese Apellido"
            ></b-form-input>
          </b-form-group>

          <b-form-group class="m-2" id="input-group-4">
            <b-form-input
              v-model="member.company"
              id="company"
              placeholder="Empresa"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            class="m-2"
            id="input-group-5"
            label="Lugar Nacimiento:"
            label-for="born_place"
          >
            <b-form-select v-model="member.born_place" id="born_place" required>
              <b-form-select-option
                v-for="city in cities"
                v-bind:key="city.id"
                :value="city.id"
                >{{ city.name }}</b-form-select-option
              >
            </b-form-select>
          </b-form-group>
          <b-button class="m-2" variant="outline-primary" @click="add"
            >Registrar</b-button
          >
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
export default {
  props: ["member"],
  methods: {
    add() {
      this.$store.dispatch("addMember", this.member);
      this.$refs["memberAddModalRef"].hide();
    },
    hideModal() {
      this.$refs["memberAddModalRef"].hide();
    },
    showModal() {
      this.$refs["memberAddModalRef"].show();
    },
  },
  computed: {
    cities() {
      return this.$store.getters.getCities;
    },
  },
  mounted() {
    this.$store.dispatch("addCities");
  },
};
</script>

<style>
</style>