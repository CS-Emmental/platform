import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Signup from '../views/Signup.vue';
import Challenges from '../views/Challenges.vue';
import ChallengesCategory from '../views/ChallengesCategory.vue';
import ChallengeDetails from '../views/ChallengeDetails.vue';
import ChallengeEdit from '../views/ChallengeEdit.vue';
import ChallengeCreate from '../views/ChallengeCreate.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
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
  {
    path: '/challenges',
    name: 'Challenges',
    component: Challenges,
  },
  {
    path: '/challenges/:categorySlug',
    name: 'ChallengesCategory',
    component: ChallengesCategory,
    props: true,
  },
  {
    path: '/challenges/:categorySlug/create',
    name: 'ChallengeCreate',
    component: ChallengeCreate,
    props: true,
  },
  {
    path: '/challenges/:categorySlug/:challengeSlug',
    name: 'ChallengeDetails',
    component: ChallengeDetails,
    props: true,
  },
  {
    path: '/challenges/:categorySlug/:challengeSlug/edit',
    name: 'ChallengeEdit',
    component: ChallengeEdit,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
