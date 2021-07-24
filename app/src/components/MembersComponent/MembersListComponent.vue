<template>
  <div class="container text-center">
    <div class="d-flex justify-content-center">
      <h1 class="m-4 d-">Lista de Miembros</h1>
      <member-modal :member="member" />
    </div>
    <hr />
    <div v-if="loading">
      <b-table striped hover :items="members" :fields="fields">
        <template v-slot:cell(action)="members">
          <!-- <i
            variant="success"
            class="fa fa-pencil"
            aria-hidden="true"
            @click="editMember(members.item.id)"
          ></i> -->
          <div class="my-auto">
            <i
              style="cursor: pointer"
              class="fa fa-trash fa-lg"
              aria-hidden="true"
              @click="onDelete(members.item.id)"
            >
            </i>
          </div>
        </template>
      </b-table>
    </div>
    <div v-else>Cargando..</div>
  </div>
</template>

<script>
import MemberModal from "../MembersComponent/MemberModalComponent.vue";
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
    };
  },
  name: "MemberListComponent",
  components: { MemberModal },
  props: {
    member: {
      type: Object,
      default: () => ({
        name: "",
        last_name: "",
        identification: "",
        born_place: "",
        company: "",
      }),
    },
  },
  computed: {
    members() {
      return this.$store.getters.getMembers;
    },
  },
  mounted() {
    this.$store.dispatch("addMembers");
  },
  methods: {
    onDelete(id) {
      this.$store.dispatch("removeMember", id);
    },
  },
};
</script>

<style>
.fa-trash {
  color: #dc3545;
}
</style>