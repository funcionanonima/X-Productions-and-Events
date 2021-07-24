<template>
  <div class="mx-auto">
    <b-card
      :title="event.name"
      img-src="https://picsum.photos/600/300/?image=25"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem"
      class="m-4 text-center"
      border-variant="info"
      :header="'Dia: ' + event.date + '     ' + event.time"
    >
      <b-card-text>
        {{ event.body }}
      </b-card-text>
      <router-link
        style="text-decoration: none"
        class="m-2"
        :to="{ name: 'Event', params: { id: event.id } }"
      >
        <h2>Detalle</h2>
      </router-link>
      <div class="d-flex justify-content-center">
        <event-edit-modal :event="event" />
        <b-button
          class="m-1"
          variant="outline-danger"
          @click="onDelete(event.id)"
          >Eliminar</b-button
        >
      </div>
    </b-card>
  </div>
</template>

<script>
import EventEditModal from "../EventComponents/EventEditModalComponent.vue";
export default {
  name: "EventCardComponent",
  components: {
    EventEditModal,
  },
  props: ["event"],
  methods: {
    onDelete(id) {
      this.$store.dispatch("removeEvent", id);
    },
  },
};
</script>

<style>
</style>