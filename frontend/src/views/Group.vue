<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h3 class="title is-3">Group</h3>
        <hr />
        <br />

        <table class="table is-striped is-hoverable is-fullwidth">
          <thead>
            <tr>
              <th scope="col">Keyword</th>
              <th scope="col">Destination</th>
              <th scope="col">Description</th>
              <th scope="col">Views</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(link, index) in links" :key="index">
              <td>
                <!-- <router-link :to="'/' + link.keyword"> -->
                <span class="tag is-medium is-primary">/{{ link.keyword }}</span>
              </td>
              <td>{{ link.destination_url }}</td>
              <td>{{ link.description }}</td>
              <td>{{ link.views }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      links: [],
      prefix: ""
    };
  },
  methods: {
    getGroupLinks() {
      const path =
        process.env.VUE_APP_API_BASE_URL + "/api/group/" + this.prefix;
      axios
        .get(path)
        .then(res => {
          this.links = res.data.results;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          // no group results found so push back to home
          this.$router.push({ name: "home" });
        });
    }
  },
  created() {
    this.prefix = this.$route.params.prefix;
    this.getGroupLinks();
  }
};
</script>
