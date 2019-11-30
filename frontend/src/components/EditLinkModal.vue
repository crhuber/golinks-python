<template>
  <div class="modal-card" style="width: auto">
    <header class="modal-card-head">
      <p class="modal-card-title">Update Link</p>
    </header>
    <section class="modal-card-body">
      <b-field label="Destination URL">
        <b-input
          type="url"
          v-model="editLinkFormInternal.destination_url"
          placeholder="Enter a url to shorten"
          icon-pack="fas"
          icon="link"
          required
        ></b-input>
      </b-field>
      <b-field label="Description">
        <b-input
          type="text"
          v-model="editLinkFormInternal.description"
          minlength="2"
          maxlength="100"
          placeholder="Enter description"
          icon-pack="fas"
          icon="comment"
          required
        ></b-input>
      </b-field>
    </section>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="onReset()">Reset</button>
      <button class="button is-primary" @click="onSubmitUpdate()">Update</button>
    </footer>
    <alertdanger :message="message" v-if="showMessage"></alertdanger>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    editLinkForm: {
      type: Object,
      default: null
    }
  },
  components: {},
  data() {
    return {
      message: "",
      showMessage: false,
      editLinkFormInternal: this.editLinkForm
    };
  },
  methods: {
    updateLink(payload, keyword) {
      const path = process.env.VUE_APP_API_BASE_URL + "/api/links/" + keyword;
      const config = {
          crossdomain: true
      }
      axios
        .put(path, payload, config)
        .then(() => {
          this.$parent.close();
          this.$emit("editLinkSignal", "true");
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.$emit("editLinkSignal", "false");
        });
    },
    onSubmitUpdate(evt) {
      const payload = {
        destination_url: this.editLinkFormInternal.destination_url,
        description: this.editLinkFormInternal.description
      };
      this.updateLink(payload, this.editLinkFormInternal.keyword);
    }
  }
};
</script>