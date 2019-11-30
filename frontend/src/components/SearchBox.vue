<template>
  <section>
    <b-field>
      <b-autocomplete v-model="queryString" icon-pack="fas" icon="search" @keyup.native="preSearch"></b-autocomplete>
    </b-field>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      results: [],
      hasFetched: false,
      queryString: ""
    };
  },
  methods: {
    preSearch() {
      if (this.queryString.length == 0) {
        this.$emit("updatedSearchResultsSignal", "false");
      }
      if (this.queryString.length > 1) {
        this.search();
      }
    },
    search() {
      const path =
        process.env.VUE_APP_API_BASE_URL + "/api/search?q=" + this.queryString;
      axios
        .get(path)
        .then(res => {
          this.results = res.data.results;
          this.hasFetched = true;
          this.$emit("updatedSearchResultsSignal", this.results);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.$buefy.toast.open(
            "Something bad happened connecting to backend"
          );
          this.hasFetched = false;
        });
    }
  },
  mounted() {}
};
</script>
