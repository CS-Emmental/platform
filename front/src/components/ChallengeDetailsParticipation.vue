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
        <div class="level">
          <div class="level-left">
            <h2 class="level-item">
              Your participation
            </h2>
            <emmental-status-tag
              class="level-item"
              :status="participation.status"
            />
          </div>
        </div>
        <div
          v-for="(flag, index) in challenge.flags"
          :key="index"
          class="flag-input"
        >
          <label class="label">
            {{ flag.text }}
            <i
              v-if="participation.found_flags.includes(index)"
              class="fas fa-check has-text-success"
            />
          </label>
          <div
            v-if="!participation.found_flags.includes(index)"
            class="field is-grouped"
          >
            <p class="control is-expanded">
              <input
                v-model="flagInputs[index]"
                class="input"
                type="text"
                placeholder="Flag Secret"
              >
            </p>
            <p class="control">
              <a
                class="button is-primary"
                @click="onSubmitFlag(index, flagInputs[index])"
              >
                Submit
              </a>
            </p>
          </div>
        </div>
        <hr>
        <template v-if="participation.status==='ongoing'">
          <a
            :href="`http://172.17.7.77:${participation.port}`"
            target="_blank"
            class="button is-dark is-fullwidth reset-button"
          >
            Go to challenge
          </a>
          <button
            class="button is-light is-fullwidth reset-button"
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
        </template>
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

import EmmentalStatusTag from '@/components/EmmentalStatusTag.vue';
import ConfirmModal from '@/components/ConfirmModal.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengeDetailsParticipation',
  components: {
    EmmentalStatusTag,
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

  public flagInputs: {[index: number]: string[]} = {};

  @Action('submitFlag', { namespace })
  public submitFlag!: CallableFunction;

  public onSubmitFlag(index: number, value: string) {
    if (this.participation) {
      this.submitFlag({
        participationId: this.participation.participation_id,
        index,
        value,
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.challenge-buttons {
  margin-bottom: 1rem;
}
.level {
  margin-bottom: .5rem;
  .tag {
    margin-bottom: 1rem;
  }
}
.flag-input {
  margin-bottom: .5rem;
}
.button {
  margin-top: .5rem;
}
</style>
