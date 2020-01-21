<template>
  <emmental-card
    :title="challenge.title"
    :link="`/challenges/${categorySlug}/${challengeSlug}`"
    :content="challenge.summary"
    :subtitle="`todo/${challenge.total_points} points`"
    :actions="actions"
  />
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { Challenge } from '../store/challenges/types';
import { slug } from '../store/utils';

const namespace = 'challenges';

@Component({
  name: 'ChallengeCard',
  components: {
    EmmentalCard,
  },
})
export default class ChallengeCard extends Vue {
  @Prop({
    type: Object as () => Challenge,
    required: true,
  })
  public challenge!: Challenge;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getCategoryById', { namespace })
  public getCategoryById!: CallableFunction;

  get parentCategory() {
    return this.getCategoryById(this.challenge.category_id);
  }

  get categorySlug() {
    return this.parentCategory && slug(this.parentCategory.title);
  }

  get challengeSlug() {
    return this.challenge && slug(this.challenge.title);
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
