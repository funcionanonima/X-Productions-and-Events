<template>
  <div>
    <b-navbar
      class="container d-flex justify-content-between my-3"
      toggleable="sm"
      type="light"
      variant="light"
    >
      <b-navbar-nav>
        <b-navbar-brand>X Productions & Events</b-navbar-brand>
      </b-navbar-nav>
      <b-navbar-nav>
        <b-nav-item
          ><router-link
            style="text-decoration: none"
            to="/"
            exact
            exact-active-class="active"
            >Eventos</router-link
          ></b-nav-item
        >
        <b-nav-item
          ><router-link
            style="text-decoration: none"
            to="/members"
            exact
            exact-active-class="active"
            >Miembros</router-link
          ></b-nav-item
        >
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>
<script>
export default {
  computed: {
    currentRouteName() {
      return this.$router.history.current.path;
    },
  },
};
</script>
<style>
</style>