import Vue from 'vue';
import VueRouter from 'vue-router';
import Challenges from '../views/Challenges.vue';
import ChallengesCategory from '../views/ChallengesCategory.vue';
import Login from '../views/Login.vue';
import Signup from '../views/Signup.vue';

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
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
