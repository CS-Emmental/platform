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
              >Submit</a>
            </p>
          </div>
        </div>
        <hr>
        <template v-if="participation.status==='ongoing'">
          <a
            :href="`http://${kubernetesHost}:${participation.port}`"
            target="_blank"
            class="button is-dark is-fullwidth stop-button"
          >Go to challenge</a>
          <button
            class="button is-light is-fullwidth stop-button"
            @click="stopMode=true"
          >
            Stop challenge
          </button>
          <confirm-modal
            title="Stop Challenge"
            message="Are you sure you want to shut down your challenge instance ?
                    (The state of your instance will be lost
                    but you will keep your points, flags and hints)"
            :toggle="stopMode"
            @confirm="onStopChallenge"
            @exit="stopMode=false"
          />
        </template>
        <template v-else-if="participation.status==='stopped'">
          <button
            class="button is-light is-fullwidth restart-button"
            @click="stopMode=true"
          >
            Restart challenge
          </button>
        </template>
      </div>
    </template>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
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
  public participation: ChallengeParticipation | undefined;

  public kubernetesHost: string = process.env.VUE_APP_KUBERNETES_HOST;

  @Action('startChallengeParticipation', { namespace })
  public startChallengeParticipation!: CallableFunction;

  public onStartChallenge() {
    this.startChallengeParticipation(this.challenge.challenge_id);
  }

  public stopMode = false;

  @Action('stopChallengeParticipation', { namespace })
  public stopChallengeParticipation!: CallableFunction;

  public onStopChallenge() {
    this.stopChallengeParticipation(this.participation.participation_id);
    this.stopMode = false;
  }

  public flagInputs: { [index: number]: string[] } = {};

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
  margin-bottom: 0.5rem;
  .tag {
    margin-bottom: 1rem;
  }
}
.flag-input {
  margin-bottom: 0.5rem;
}
.button {
  margin-top: 0.5rem;
}
</style>
