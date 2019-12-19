<template>
  <div class="challenges-category">
    <div class="box">
      <h1 class="title is-1">
      <i :class="category.icon"></i>
      {{category.title}}
    </h1>
    <p class="subtitle is-4">
      {{category.count ? category.count : 0}} Challenges
    </p>
    <p>
      {{category.description}}
    </p>
    </div>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import { ChallengeCategory } from '../store/challenges/types';

const namespace: string = 'challenges';

@Component({
  name: 'ChallengesCategory',
})
export default class ChallengesCategory extends Vue {
  @Prop() public categoryKebab: string;
  @Getter('getCategoryFromKebab', { namespace }) public getCategoryFromKebab;
  get category(): ChallengeCategory {
    return this.getCategoryFromKebab(this.categoryKebab);
  }
}
</script>
