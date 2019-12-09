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
                <span
                  class="tag is-medium is-primary"
                  v-if="isProgrammaticKeyword(link.keyword)"
                >/{{ link.keyword }}</span>
                <router-link
                  :to="{ name: 'redirect', params: { keyword: `${link.keyword}`}}"
                  v-else
                >
                  <span class="tag is-medium is-primary">/{{ link.keyword }}</span>
                </router-link>
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
  metaInfo: {
    title: "Group"
  },
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
    },
    isProgrammaticKeyword(keyword) {
      return keyword.includes("%s");
    }
  },
  created() {
    this.prefix = this.$route.params.prefix;
    this.getGroupLinks();
  }
};
</script>
