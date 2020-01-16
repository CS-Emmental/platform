<template>
  <div>
    <emmental-box
      v-if="category"
      :title="category.title"
      :icon="category.icon"
      :subtitle="`${category.challengesCount ? category.challengesCount : 0} Challenges`"
      :content="category.description"
      :actions="actions"
      class="header-box"
    />
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import { ChallengeCategory } from '../store/challenges/types';

import EmmentalBox from '@/components/EmmentalBox.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengesCategory',
  components: {
    EmmentalBox,
  },
})
export default class ChallengesCategory extends Vue {
  @Prop() public categoryKebab: string;

  @Getter('getCategoryFromKebab', { namespace }) public getCategoryFromKebab;

  @Getter('hasPermission') public hasPermission: CallableFunction;

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
</style>
