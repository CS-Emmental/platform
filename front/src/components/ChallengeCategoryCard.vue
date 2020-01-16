<template>
  <emmental-card
    :title="category.title"
    :link="`/challenges/${category.kebab}`"
    :icon="category.icon"
    :subtitle="`${category.challengesCount ? category.challengesCount : 0} Challenges`"
    :content="category.description"
    :actions="actions"
  />
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { ChallengeCategory } from '../store/challenges/types';

@Component({
  name: 'ChallengeCategoryBox',
  components: {
    EmmentalCard,
  },
})
export default class ChallengeCategoryCard extends Vue {
  @Prop({
    type: Object as () => ChallengeCategory,
    required: true,
  })
  public category;

  @Getter('hasPermission') public hasPermission: CallableFunction;

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
