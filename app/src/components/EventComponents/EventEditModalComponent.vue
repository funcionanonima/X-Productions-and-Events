<template>
  <div>
    <b-button class="m-1" v-b-modal.event variant="outline-success"
      >Editar</b-button
    >
    <b-modal
      id="event"
      title="Eventos"
      :hide-footer="true"
      ref="MemberEditModalRef"
    >
      <div>
        <b-form>
          <b-form-group class="m-2" id="nameGroup" label-for="name">
            <b-form-input
              v-model="event.name"
              id="name"
              class="d-block"
              type="text"
              placeholder="Nombre Evento"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group class="m-2">
            <b-form-datepicker v-model="event.date" locale="es" />
          </b-form-group>
          <b-form-group class="m-2">
            <div>
              <b-form-timepicker v-model="event.time" locale="es" />
            </div>
          </b-form-group>
          <b-form-textarea
            class="m-2"
            id="textarea"
            v-model="event.body"
            placeholder="Breve Descripción"
            rows="3"
            max-rows="6"
          ></b-form-textarea>
          <b-form-group
            class="m-2"
            id="categoryGroup"
            label="Categoria:"
            label-for="category"
          >
            <b-form-select id="category" v-model="event.category" required>
              <b-form-select-option
                v-for="category in categories"
                v-bind:key="category.id"
                :value="category.id"
                >{{ category.name }}</b-form-select-option
              >
            </b-form-select>
          </b-form-group>
          <b-form-group
            class="m-2"
            id="placeGroup"
            label="Lúgar:"
            label-for="place"
          >
            <b-form-select id="place" v-model="event.place" required>
              <b-form-select-option
                v-for="city in cities"
                v-bind:key="city.id"
                :value="city.id"
                >{{ city.name }}</b-form-select-option
              >
            </b-form-select>
          </b-form-group>
          <b-form-group class="m-2">
            <b-form-select v-model="event.members" multiple :select-size="4">
              <b-form-select-option
                v-for="member in members"
                v-bind:key="member.id"
                :value="member.id"
                >{{ member.name }}</b-form-select-option
              >
            </b-form-select>
          </b-form-group>
          <div>
            <b-button
              class="m-2"
              variant="outline-primary"
              @click="onUpdate(event.id)"
              >Guardar</b-button
            >
          </div>
        </b-form>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  props: ["event"],
  computed: {
    categories() {
      return this.$store.getters.getCategories;
    },
    cities() {
      return this.$store.getters.getCities;
    },
    members() {
      return this.$store.getters.getMembers;
    },
  },
  methods: {
    hideModal() {
      this.$refs["MemberEditModalRef"].hide();
    },
    showModal() {
      this.$refs["MemberAddModalRef"].show();
    },
    onUpdate() {
      this.$store.dispatch("updateEvent", this.event);
      this.$refs["MemberEditModalRef"].hide();
    },
  },
  mounted() {
    this.$store.dispatch("addCategories");
    this.$store.dispatch("addCities");
    this.$store.dispatch("addMembers");
  },
};
</script>

<style>
</style>