<template>
  <div class="challenges">
    <div class="box">
      <h1 class="title is-1">
      <i class="fas fa-shield-alt title-icon"></i>
      Challenges
    </h1>
    <p class="subtitle is-4">
      Many challenges to train various skills, from server attack to cryptography.
    </p>
    <p>
      Click on one of the following categories to explore numerous challenges proposed by CS Emmental team or others.
    </p>
    </div>
    <div class="categories">
      <challenge-category-card v-for="category in categories" :key="category.id" :category="category"/>
    </div>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Action } from 'vuex-class';
import { ChallengesState } from '../store/challenges/types';

import ChallengeCategoryCard from '@/components/ChallengeCategoryCard.vue';

const namespace: string = 'challenges';

@Component({
  name: 'Challenges',
  components: {
    ChallengeCategoryCard,
  },
})
export default class Challenges extends Vue {
  @State('challenges') public challenges: ChallengesState;
  @Action('getChallengeCategories', { namespace }) public getChallengeCategories: any;

  get categories() {
    const categories = this.challenges && this.challenges.challengeCategories;
    return categories || [];
  }

  public created() {
    this.getChallengeCategories();
  }
}
</script>

<style lang="scss" scoped>
.categories {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  height: auto;
  margin-top: 5rem;
}
</style>
