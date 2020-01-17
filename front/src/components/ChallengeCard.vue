<template>
  <emmental-card
    :title="challenge.title"
    :link="`/challenges/${parentCategory.kebab}/${challenge.kebab}`"
    :subtitle="challenge.description"
    content="0/100 points"
    :actions="actions"
  />
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { Challenge } from '../store/challenges/types';

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
