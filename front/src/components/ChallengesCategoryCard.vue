<template>
  <emmental-card>
    <template v-slot:header>
      <router-link
        :to="`/challenges/${category.title_slug}`"
        class="subtitle is-4 card-header-title"
      >
        <i
          class="title-icon"
          :class="category.icon"
        />
        {{ category.title }}
      </router-link>
    </template>
    <template v-slot:content>
      <p class="subtitle is-6">
        {{ categoryCount }} Challenge{{ categoryCount === 1 ? '' : 's' }}
      </p>
      <p>
        {{ category.description }}
      </p>
    </template>
  </emmental-card>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { ChallengeCategory } from '../store/challengeCategories/types';

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

  @Getter('getChallengesCountByCategory', { namespace: 'challenges' })
  public getChallengesCountByCategory!: CallableFunction;

  get categoryCount() {
    return this.category && this.getChallengesCountByCategory(this.category.category_id);
  }
}
</script>

<style lang="scss" scoped>
.title-icon {
  margin-right: .5rem;
}
</style>
