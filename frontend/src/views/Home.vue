<template>
  <div class="container">
    <h3 class="title is-3">New Link</h3>
    <hr />
    <br />
    <br />
    <alert v-if="this.MessageState.showMessage"></alert>
    <add-link-form></add-link-form>
    <article class="message is-primary">
      <div class="message-body">Tip: {{tipMessage}}</div>
    </article>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "@/components/Alert.vue";
import AddLinkForm from "@/components/AddLinkForm.vue";
import MessageState from "@/components/MessageState";

export default {
  metaInfo: {
    title: "Home"
  },
  components: {
    Alert,
    AddLinkForm
  },
  data() {
    return {
      tipMessage: "",
      MessageState
    };
  },
  mounted() {
    var tipMessages = [
      "Create short links that inject variables by using %s.  For example: gh/%s to link to github.com/%s",
      "You can preview what lies behind a short link. Add a + at the end of your link to view more",
      "Nested keywords like 'eng/handbook' and 'eng/help' group together and get a landing page at 'eng'"
    ];
    var tipMessage =
      tipMessages[Math.floor(Math.random() * tipMessages.length)];
    this.tipMessage = tipMessage;
  },
  methods: {}
};
</script>
