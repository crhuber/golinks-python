<template>
  <div>
    <b-message
      :type="this.MessageState.alertType"
      auto-close
      :duration="8000"
      @close="onClose"
    >{{ this.MessageState.message }}</b-message>
    <br />
  </div>
</template>

<script>
import MessageState from "../components/MessageState";

export default {
  data() {
    return {
      MessageState
    };
  },
  methods: {
    onClose(e) {
      console.log("closed!!!!");
      this.MessageState.showMessage = false;
    }
  },
  computed: {}
};
</script>
