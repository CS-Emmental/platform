<template>
<aside class="menu">
  <router-link to="/challenges" class="menu-label has-text-primary">
    Challenges
  </router-link>
  <ul class="menu-list">
    <li
      v-for="category in categories"
      :key="category.id">
      <router-link :to="`/challenges/${category.title.toLowerCase().replace(' ', '-')}`"
        class="menu-item"
        :class="{'is-active': category.title.toLowerCase().replace(' ', '-') == menuActive.category}">
        {{category.title}}
        <span class="tag is-rounded is-small">
          <b>{{category.challengesCount ? category.challengesCount : 0}}</b>
        </span>
      </router-link>
    </li>
  </ul>
  <router-link to="/community" class="menu-label has-text-primary">
    Community
  </router-link>
</aside>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class EmmentalSidebar extends Vue {
  public name: string = 'EmmentalSidebar';
  get menuActive() {
    const route = this.$route;
    return {
      category: route.path.split('/')[2],
    };
  }
  get categories() {
    return this.$store.state.challengeCategories;
  }
  public created() {
    this.$store.dispatch('getChallengeCategories');
  }
}
</script>

<style lang="scss" scoped>
aside {
  height: 100%;
  width: 18vw;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  overflow-x: hidden;
  padding: .5rem;
  padding-top: 7vh;
  background-color: #253341;
  a {
    color: white;
  }
}
.menu-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between
}
</style>
