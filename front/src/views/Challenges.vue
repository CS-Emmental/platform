<template>
  <div class="challenges">
    <emmental-box
      title="Challenges"
      icon="fas fa-shield-alt"
      subtitle="Many challenges to train various skills, from server attack to cryptography."
      content="Click on one of the following categories to
        explore numerous challenges proposed by CS Emmental team or others."
      class="header-box"
    />
    <div class="categories">
      <challenges-category-card
        v-for="category in categories"
        :key="category.id"
        :category="category"
      />
    </div>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Action } from 'vuex-class';
import { ChallengesState } from '../store/challenges/types';

import ChallengesCategoryCard from '@/components/ChallengesCategoryCard.vue';
import EmmentalBox from '@/components/EmmentalBox.vue';

const namespace = 'challenges';

@Component({
  name: 'Challenges',
  components: {
    ChallengesCategoryCard,
    EmmentalBox,
  },
})
export default class Challenges extends Vue {
  @State('challenges') public challenges: ChallengesState;

  @Action('getChallengeCategories', { namespace })
  public getChallengeCategories: CallableFunction;

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
  margin-top: 3rem;
}
.header-box {
  padding-top: 3rem;
  padding-bottom: 3rem;
}
</style>
