<template>
  <div class="challenge-buttons">
    <button
      v-if="!participation"
      class="button is-primary is-large is-fullwidth"
      @click="onStartChallenge"
    >
      Start challenge
    </button>
    <template v-else>
      <div class="box content">
        <h2>Your participation</h2>
        <button
          class="button is-dark is-fullwidth"
          @click="resetMode=true"
        >
          Reset challenge
        </button>
        <confirm-modal
          title="Reset Challenge"
          message="Are you sure you want to reset your challenge instance ?
                  (all current progress will be lost)"
          :toggle="resetMode"
          @confirm="onResetChallenge"
          @exit="resetMode=false"
        />
      </div>
    </template>
  </div>
</template>

<script  lang="ts">
import {
  Prop,
  Component,
  Vue,
} from 'vue-property-decorator';
import { Action } from 'vuex-class';
import { Challenge, ChallengeParticipation } from '../store/challenges/types';

import ConfirmModal from '@/components/ConfirmModal.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengeDetailsParticipation',
  components: {
    ConfirmModal,
  },
})
export default class ChallengeDetailsParticipation extends Vue {
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

  @Action('startChallengeParticipation', { namespace })
  public startChallengeParticipation!: CallableFunction;

  public onStartChallenge() {
    this.startChallengeParticipation(this.challenge.challenge_id);
  }

  public resetMode = false;

  public onResetChallenge() {
    this.resetMode = false;
  }
}
</script>

<style lang="scss" scoped>
.challenge-buttons {
  margin-bottom: 1rem;
}
</style>
