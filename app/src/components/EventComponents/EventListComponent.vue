<template>
  <div class="container">
    <div class="d-flex justify-content-center">
      <h1 class="m-4 d-">Lista de Eventos</h1>
      <event-modal :event="event" />
    </div>
    <hr />
    <b-card-group>
      <event-card v-for="event in events" :key="event.id" :event="event" />
    </b-card-group>
  </div>
</template>

<script>
import EventCard from "../EventComponents/EventCardComponent";
import EventModal from "../EventComponents/EventModalComponent";
export default {
  components: {
    EventCard,
    EventModal,
  },
  props: {
    event: {
      type: Object,
      default: () => ({
        name: "",
        body: "",
        date: "",
        place: "",
        time: "",
        members: [],
      }),
    },
  },
  computed: {
    events() {
      return this.$store.getters.getEvents;
    },
  },
  mounted() {
    this.$store.dispatch("addEvents");
  },
};
</script>

<style>
</style>