<template>
  <div class="challenges">
    <div class="box">
      <h1 class="title is-1">
      <i class="fas fa-shield-alt title-icon"></i>
      Challenges
    </h1>
    <p class="subtitle is-4">
      An incredible amount of 1 super hard challenge !
    </p>
    <p>
      Click on one of the following categories to explore numerous challenges proposed by CS Emmental team or others.
    </p>
    </div>
    <div class="categories">
      <challenge-category-box v-for="category in categories" :key="category.id" :category="category"/>
    </div>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ChallengeCategoryBox from '@/components/ChallengeCategoryBox.vue';

@Component({
  name: 'Challenges',
  components: {
    ChallengeCategoryBox,
  },
})
export default class Challenges extends Vue {
  get categories() {
    return this.$store.state.challengeCategories;
  }
  public created() {
    this.$store.dispatch('getChallengeCategories');
  }
}
</script>

<style lang="scss" scoped>
.title-icon {
  margin-right: .5rem;
}
.categories {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  height: auto;
  margin-top: 5rem;
}
</style>
