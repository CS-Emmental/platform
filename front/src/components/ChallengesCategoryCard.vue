<template>
  <emmental-card
    :title="category.title"
    :link="`/challenges/${category.kebab}`"
    :icon="category.icon"
    :subtitle="`${categoryCount} Challenge${categoryCount == 1 ? '' : 's'}`"
    :content="category.description"
    :actions="actions"
  />
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { ChallengeCategory } from '../store/challenges/types';

const namespace = 'challenges';

@Component({
  name: 'ChallengesCategoryCard',
  components: {
    EmmentalCard,
  },
})
export default class ChallengesCategoryCard extends Vue {
  @Prop({
    type: Object as () => ChallengeCategory,
    required: true,
  })
  public category!: ChallengeCategory;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getChallengesCountByCategory', { namespace })
  public getChallengesCountByCategory!: CallableFunction;

  get categoryCount() {
    return this.category && this.getChallengesCountByCategory(this.category.category_id);
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
</style>
