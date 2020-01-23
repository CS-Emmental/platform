<template>
  <emmental-card
    :title="category.title"
    :link="`/challenges/${categorySlug}`"
    :icon="category.icon"
    :subtitle="`${categoryCount} Challenge${categoryCount == 1 ? '' : 's'}`"
    :content="category.description"
  />
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { ChallengeCategory } from '../store/challenges/types';
import { slug } from '../store/utils';

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

  @Getter('getChallengesCountByCategory', { namespace })
  public getChallengesCountByCategory!: CallableFunction;

  get categoryCount() {
    return this.category && this.getChallengesCountByCategory(this.category.category_id);
  }

  get categorySlug() {
    return this.category && slug(this.category.title);
  }
}
</script>

<style lang="scss" scoped>
</style>
