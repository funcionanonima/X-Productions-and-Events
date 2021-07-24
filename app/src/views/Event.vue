<template>
  <div class="container">
    <b-card
      class="text-center"
      :title="event.name"
      :sub-title="'lugar: ' + event.place + ' Fecha: ' + event.date"
    >
      <b-card-text>
        {{ event.category }}
      </b-card-text>

      <b-card-text>{{ event.body }}</b-card-text>
      <div v-if="event.members == ''">
        <h3>sin asitentes</h3>
      </div>
      <div v-else>
        <b-card
          border-variant="light"
          header="Miembros inscritos"
          class="text-center"
        >
          <b-card-text>
            <b-list-group>
              <b-list-group-item
                v-for="member in event.members"
                v-bind:key="member.id"
              >
                <div>
                  <h3>{{ member.name }} {{ member.last_name }}</h3>
                  <p>
                    {{
                      member.company ? "Trabaja para: " + member.company : ""
                    }}
                  </p>
                  <p>Desde: {{ member.born_place }}</p>
                </div>
              </b-list-group-item>
            </b-list-group>
          </b-card-text>
        </b-card>
      </div>
    </b-card>
  </div>
</template>

<script>
export default {
  props: ["id"],
  computed: {
    event() {
      return this.$store.state.event;
    },
  },
  mounted() {
    this.$store.dispatch("addEvent", this.id);
  },
};
</script>

<style>
</style>