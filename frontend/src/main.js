import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import VueClipboard from 'vue-clipboard2'

Vue.use(Buefy);
Vue.use(VueClipboard);
Vue.config.productionTip = false;


new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
