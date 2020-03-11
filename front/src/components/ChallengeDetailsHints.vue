<template>
  <div>
    <h2 class="title is-4">
      Hints
    </h2>
    <div v-if="challenge.hints">
      <div
        v-for="(hint, index) in challenge.hints"
        :key="index"
        class="hint"
      >
        <p v-if="activeHints.includes(index)">
          Hint n° {{ index+1 }}: {{ hint.text }}
        </p>
        <button
          v-else
          class="button button-hint"
          @click="onUseHint(index)"
        >
          Show hint n°{{ index+1 }} for {{ hint.cost*challenge.total_points }} points
        </button>
      </div>
    </div>
    <div v-else>
      There is no hints for this challenge.
    </div>
  </div>
</template>

<script  lang="ts">
import {
  Prop,
  Component,
  Vue,
  Watch,
} from 'vue-property-decorator';
import { Action } from 'vuex-class';
import { Challenge } from '../store/challenges/types';
import { ChallengeParticipation } from '../store/challengeParticipations/types';

@Component({
  name: 'ChallengeDetailsHints',
})
export default class ChallengeDetailsHints extends Vue {
  // Challenge

  @Prop({
    type: Object as () => Challenge,
    required: true,
  })
  public challenge!: Challenge;

  @Prop({
    type: Object as () => ChallengeParticipation,
    required: false,
  })
  public participation: ChallengeParticipation|undefined;

  @Action('useHints', { namespace: 'challengeParticipations' })
  public useHints!: CallableFunction;


  // Init with already used hints when participation is loaded
  @Watch('participation', { immediate: true })
  onParticipationChange(val: ChallengeParticipation, old: ChallengeParticipation) {
    if (val && val.used_hints && val.used_hints.length > 0 && old === undefined) {
      this.useHints(val);
    }
  }

  onUseHint(index: number) {
    if (this.participation && ['ongoing', 'stopped'].includes(this.participation.status)) {
      const updated = { ...this.participation };
      updated.used_hints.push(index);
      this.useHints(updated);
    } else {
      this.$toasted.show('Start this challenge before cheating');
    }
  }

  get activeHints() {
    return this.participation ? this.participation.used_hints : [];
  }
}
</script>

<style lang="scss" scoped>
.hint {
  padding-bottom: .5rem;
}
</style>
