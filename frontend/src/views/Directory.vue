<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <hr />
        <br />
        <br />
        <alert v-if="this.MessageState.showMessage"></alert>
        <search-box @updatedSearchResultsSignal="updatedSearchResultsParent"></search-box>
        <br />
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
                <router-link :to="`${link.keyword}`" v-else>
                  <span class="tag is-medium is-primary">/{{ link.keyword }}</span>
                </router-link>
              </td>
              <td>{{ link.destination_url }}</td>
              <td>{{ link.description }}</td>
              <td>{{ link.views }}</td>
              <td>
                <div class="btn-group" role="group">
                  <b-button class="button is-warning is-small" @click="onEditLinkClick(link)">Update</b-button>
                  <remove-link-button :link="link" @removeLinkSignal="removeLinkParent"></remove-link-button>
                  <b-button
                    class="button is-light is-small"
                    v-clipboard:copy="currentUrl + '/' + link.keyword"
                    v-clipboard:success="onCopy"
                    v-clipboard:error="onError"
                  >Copy</b-button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "@/components/Alert.vue";
import AddLinkModal from "../components/AddLinkModal.vue";
import EditLinkModal from "../components/EditLinkModal.vue";
import RemoveLinkButton from "../components/RemoveLinkButton.vue";
import SearchBox from "../components/SearchBox.vue";
import MessageState from "../components/MessageState";

export default {
  metaInfo: {
    title: "Directory"
  },
  components: {
    Alert: Alert,
    AddLinkModal: AddLinkModal,
    EditLinkModal: EditLinkModal,
    RemoveLinkButton: RemoveLinkButton,
    SearchBox: SearchBox
  },
  data() {
    return {
      links: [],
      currentUrl: "",
      MessageState
    };
  },
  methods: {
    getLinks() {
      const path = process.env.VUE_APP_API_BASE_URL + "/api/links";
      const config = {
        crossdomain: true
      };
      axios
        .get(path, config)
        .then(res => {
          this.links = res.data.results;
        })
        .catch(error => {
          // eslint-disable-next-line
          this.$buefy.toast.open(
            "Something bad happened connecting to backend"
          );
          console.error(error);
        });
    },
    updatedSearchResultsParent(event) {
      if (event == "false") {
        this.getLinks();
      } else this.links = event;
    },
    removeLinkParent(event) {
      if (event == "true") {
        this.MessageState.message = "Link removed!";
        this.MessageState.showMessage = true;
        this.MessageState.alertType = "is-danger";
      }
      this.getLinks();
    },
    onEditLinkClick(link) {
      this.$buefy.modal.open({
        parent: this,
        component: EditLinkModal,
        props: {
          editLinkForm: link
        },
        events: {
          editLinkSignal: event => {
            if (event == "true") {
              this.MessageState.message = "Link updated!";
              this.MessageState.alertType = "is-success";
              this.MessageState.showMessage = true;
            }
            this.getLinks();
          }
        }
      });
    },
    onCopy(e) {
      this.MessageState.showMessage = true;
      this.MessageState.alertType = "is-success";
      this.MessageState.message = "Link copied to clipboard!";
    },
    onError(e) {},
    isProgrammaticKeyword(keyword) {
      return keyword.includes("%s");
    }
  },
  created() {
    this.currentUrl = window.location.protocol + "//" + window.location.host;
    this.getLinks();
  }
};
</script>
