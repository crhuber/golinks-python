<template>
  <b-button type="is-danger" size="is-small" @click="onDeleteLink(link)">Delete</b-button>
</template>
<script>
import axios from "axios";

export default {
  props: ["link"],
  data() {
    return {};
  },
  methods: {
    removeLink(keyword) {
      const path = process.env.VUE_APP_API_BASE_URL + "/api/links/" + keyword;
      const config = {
        crossdomain: true
      };
      axios
        .delete(path, config)
        .then(() => {
          this.$emit("removeLinkSignal", "true");
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.$emit("removeLinkSignal", "false");
        });
    },
    onDeleteLink(link) {
      this.removeLink(link.keyword);
    }
  }
};
</script>