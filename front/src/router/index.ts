import Vue from 'vue';
import VueRouter from 'vue-router';
import Challenges from '../views/Challenges.vue';
import ChallengesCategory from '../views/ChallengesCategory.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/challenges',
    name: 'Challenges',
    component: Challenges,
  },
  {
    path: '/challenges/:categoryKebab',
    name: 'ChallengesCategory',
    component: ChallengesCategory,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
