<template>
  <members-list />
</template>

<script>
import MembersList from "../components/MembersComponent/MembersListComponent.vue";
export default {
  name: "Members",
  components: { MembersList },
  // props: {
  //   member: {
  //     type: Object,
  //     default: () => ({
  //       identification: "",
  //       name: "",
  //       last_name: "",
  //       born_place: "",
  //       company: "",
  //     }),
  //   },
  // },
};
</script>

<style>
</style>
