<template>
  <div>
    <h2 class="title">{{ keyword }}</h2>
    <p>Redirects to {{response.destination_url}}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Redirect",
  data() {
    return {
      keyword: "",
      response: "",
      safeMode: false
    };
  },
  methods: {
    getLink() {
      const path =
        process.env.VUE_APP_API_BASE_URL + "/api/links/" + this.keyword;
      axios
        .get(path)
        .then(res => {
          this.response = res.data;
          if (this.safeMode == false) {
            window.location.href = res.data.destination_url;
          }
        })
        .catch(error => {
          // eslint-disable-next-line
          // console.error(error);
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data);
            console.log(
              "did not find " + this.keyword + " trying to get groups"
            );
            // console.log(error.response.status);
            // console.log(error.response.headers);
            if (error.response.status == 404) {
              this.$router.push({
                name: "group",
                params: { prefix: this.keyword }
              });
            }
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
            this.$buefy.toast.open(
              "Something bad happened connecting to backend"
            );
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message);
            this.$buefy.toast.open(
              "Something bad happened connecting to backend"
            );
          }
          console.log(error.config);
        });
    }
  },
  created() {
    var kw = this.$route.params.keyword;
    console.log(kw);
    if (kw == "directory") {
      console.log("pushing to directory");
      this.$router.push({ name: "directory" });
    }
    if (kw.endsWith("+")) {
      this.safeMode = true;
      console.log("Safe url mode on");
      var kw = this.$route.params.keyword.split("+");
      this.keyword = kw[0];
    } else {
      this.keyword = this.$route.params.keyword;
    }
    console.log(this.keyword);
    this.getLink();
  },
  mounted() {}
};
</script>
