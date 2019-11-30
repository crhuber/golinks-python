<template>
  <div id="app" class="container">
    <b-navbar>
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img src="./assets/logo.png" alt="Lightweight UI components for Vue.js based on Bulma" />
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">Home</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/directory' }">Directory</b-navbar-item>
        <b-navbar-dropdown>
          <b-navbar-item tag="router-link" :to="{ path: '/help' }">Help</b-navbar-item>
        </b-navbar-dropdown>
      </template>

      <template slot="end">
        <b-navbar-item tag="div">
          <div class="buttons">
            <b-button class="button is-primary is-outlined" @click="onAddLinkClick">New Link</b-button>
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>
    <router-view />
  </div>
</template>

<script>
import AddLinkModal from "./components/AddLinkModal.vue";
export default {
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "Golinks",
    // all titles will be injected into this template
    titleTemplate: "Golinks | %s"
  },
  components: {
    AddLinkModal: AddLinkModal
  },
  methods: {
    onAddLinkClick() {
      this.$buefy.modal.open({
        parent: this,
        component: AddLinkModal,
        events: {
          addLinkSignal: event => {
            console.log("addLinkSignal signal received ");
            if (event == "true") {
              this.message = "Link added!";
              this.alertType = "is-success";
              this.showMessage = true;
            }
            this.$router.go();
          }
        }
      });
    }
  }
};
</script>
<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#nav {
}

#nav a {
}

#nav a.router-link-exact-active {
  color: #00d1b2;
}
</style>
