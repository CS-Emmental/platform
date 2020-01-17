<template>
  <div class="challenge-category">
    <emmental-box
      v-if="category"
      :title="category.title"
      :icon="category.icon"
      :subtitle="`${categoryCount} Challenge${categoryCount == 1 ? '' : 's'}`"
      :content="category.description"
      :actions="actions"
      class="header-box"
    />
    <div class="challenges" v-if="category">
      <challenge-card
        v-for="challenge in getChallengesByCategory(category.category_id)"
        :key="challenge.challenge_id"
        :challenge="challenge"
      />
    </div>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import { ChallengeCategory } from '../store/challenges/types';

import EmmentalBox from '@/components/EmmentalBox.vue';
import ChallengeCard from '@/components/ChallengeCard.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengesCategory',
  components: {
    EmmentalBox,
    ChallengeCard,
  },
})
export default class ChallengesCategory extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public categoryKebab!: string;

  @Getter('getCategoryFromKebab', { namespace })
  public getCategoryFromKebab!: CallableFunction;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getChallengesCountByCategory', { namespace })
  public getChallengesCountByCategory!: CallableFunction;

  @Getter('getChallengesByCategory', { namespace })
  public getChallengesByCategory!: CallableFunction;

  get categoryCount() {
    return this.category && this.getChallengesCountByCategory(this.category.category_id);
  }

  get category(): ChallengeCategory {
    return this.getCategoryFromKebab(this.categoryKebab);
  }

  get actions() {
    let actions;
    if (this.hasPermission('admin')) {
      actions = [
        {
          text: 'Edit',
          signal: 'edit',
        },
        {
          text: 'Delete',
          signal: 'delete',
        },
      ];
    }
    return actions;
  }
}
</script>

<style lang="scss" scoped>
.challenges {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  height: auto;
  margin-top: 3rem;
}
</style>
