import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Redirect from './views/Redirect.vue';
import Directory from './views/Directory.vue';
import Group from './views/Group.vue';
import Health from './views/Health.vue';
import Help from './views/Help.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/help',
      name: 'help',
      component: Help,
    },
    {
      path: '/directory',
      name: 'directory',
      component: Directory,
    },
    {
      path: '/healthz',
      name: 'health',
      component: Health,
    },
    {
      path: '/group/:prefix',
      name: 'group',
      component: Group,
    },
    {
      path: '/:keyword(.*)',
      name: 'redirect',
      component: Redirect,
    },

  ],
});
