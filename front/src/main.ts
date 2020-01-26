import Vue from 'vue';
import Toasted from 'vue-toasted';
import { ToastObject } from 'vue-toasted/types/index.d';

import App from './App.vue';
import router from './router';
import store from './store';

Vue.use(Toasted, {
  position: 'bottom-right',
  duration: 5000,
  keepOnHover: true,
  iconPack: 'fontawesome',
  action: {
    icon: 'fa-times',
    onClick(_: Event, toastObject: ToastObject) {
      toastObject.goAway(0);
    },
    class: 'emmental-toast-action',
  },
  className: 'emmental-toast',
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
