<template>
  <div class="modal-card" style="width: auto">
    <header class="modal-card-head">
      <p class="modal-card-title">New Link</p>
    </header>
    <section class="modal-card-body">
      <alert v-if="this.MessageState.showMessage"></alert>
      <b-field horizontal label="Keyword">
        <b-input
          type="text"
          v-model="addLinkForm.keyword"
          minlength="2"
          maxlength="100"
          placeholder="Enter keyword"
          icon-pack="fas"
          icon="share"
          required
        ></b-input>
      </b-field>
      <b-field horizontal label="Destination URL">
        <b-input
          type="url"
          v-model="addLinkForm.destination_url"
          placeholder="Enter a url to shorten"
          icon-pack="fas"
          icon="link"
          required
        ></b-input>
      </b-field>
      <b-field horizontal label="Description">
        <b-input
          type="text"
          v-model="addLinkForm.description"
          minlength="2"
          maxlength="100"
          placeholder="Enter description"
          icon-pack="fas"
          icon="comment"
        ></b-input>
      </b-field>
    </section>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="onReset">Reset</button>
      <button class="button is-primary" @click="onSubmit">Submit</button>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";
import MessageState from "../components/MessageState";

export default {
  components: { Alert },
  data() {
    return {
      MessageState,
      addLinkForm: {
        keyword: "",
        destination_url: "",
        description: ""
      }
    };
  },
  methods: {
    addLink(payload) {
      const path = process.env.VUE_APP_API_BASE_URL + "/api/links";
      axios
        .post(path, payload)
        .then(() => {
          this.$emit("addLinkSignal", "true");
          console.log("addLinkSignal emitted");
          MessageState.message = "Link Added!";
          MessageState.alertType = "is-success";
          MessageState.showMessage = true;
          this.$parent.close();
        })
        .catch(error => {
          if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
            MessageState.message = error.response.data.message;
            MessageState.alertType = "is-danger";
            MessageState.showMessage = true;
          } else if (error.request) {
            // The request was made but no response was received
            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            // http.ClientRequest in node.js
            console.log(error.request);
          } else {
            // Something happened in setting up the request that triggered an Error
            console.log("Error", error.message);
          }
          console.log(error.config);
        });
    },
    initForm() {
      this.addLinkForm.keyword = "";
      this.addLinkForm.destination_url = "";
      this.addLinkForm.description = "";
    },
    onSubmit(event) {
      if (
        this.addLinkForm.keyword == "" ||
        this.addLinkForm.destination_url == "" ||
        this.addLinkForm.description == ""
      ) {
        event.preventDefault();
        this.showMessage = true;
        this.message = "Fields cannot be empty";
        this.alertType = "is-danger";
        return false;
      } else {
      }
      const payload = {
        keyword: this.addLinkForm.keyword,
        destination_url: this.addLinkForm.destination_url,
        description: this.addLinkForm.description
      };
      this.addLink(payload);
      this.initForm();
    },
    onReset(evt) {
      //this.$parent.close()
      this.initForm();
    }
  }
};
</script>
