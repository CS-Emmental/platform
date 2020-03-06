<template>
  <aside class="menu">
    <router-link
      to="/"
      class="menu-label has-text-primary"
    >
      Home
    </router-link>
    <router-link
      to="/challenges"
      class="menu-label has-text-primary"
    >
      Challenges
    </router-link>
    <ul class="menu-list">
      <li
        v-for="category in challengeCategories"
        :key="category.category_id"
      >
        <router-link
          :to="`/challenges/${category.title_slug}`"
          class="menu-item"
          :class="{
            'is-active': category.title_slug == menuActive.category
          }"
        >
          {{ category.title }}
          <span class="tag is-rounded is-small">
            <b>{{ getChallengesCountByCategory(category.category_id) }}</b>
          </span>
        </router-link>
      </li>
    </ul>
    <router-link
      to="/articles"
      class="menu-label has-text-primary"
    >
      Articles
    </router-link>
    <router-link
      to="/Leaderboard"
      class="menu-label has-text-primary"
    >
      Leaderboard
    </router-link>
  </aside>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Action, Getter } from 'vuex-class';
import { ChallengeCategory } from '../store/challengeCategories/types';

@Component({
  name: 'EmmentalSidebar',
})
export default class EmmentalSidebar extends Vue {
  @State('challengeCategories', { namespace: 'challengeCategories' }) public challengeCategories: ChallengeCategory[]|undefined;

  @Action('getChallengeCategories', { namespace: 'challengeCategories' })
  public getChallengeCategories!: CallableFunction;

  @Action('getChallenges', { namespace: 'challenges' })
  public getChallenges!: CallableFunction;

  @Getter('getChallengesCountByCategory', { namespace: 'challenges' })
  public getChallengesCountByCategory!: CallableFunction;

  get menuActive() {
    const route = this.$route;
    return {
      category: route.path.split('/')[2],
    };
  }

  public created() {
    this.getChallengeCategories();
    this.getChallenges();
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
.menu-label {
  display: block;
}
.tag {
  min-width: 2rem;
}
</style>
