<template>
  <div
    v-if="challenge"
    class="challenge-details"
  >
    <emmental-box
      :actions="actions"
      class="header-box"
      @edit="$router.push(`/challenges/${categorySlug}/${challengeSlug}/edit`)"
      @delete="confirmDeleteMode=true"
    >
      <template v-slot:header>
        <h1 class="title level-item">
          {{ challenge.title }}
        </h1>
      </template>
      <template v-slot:content>
        <p class="subtitle is-4">
          {{ finalPoints }}/{{ challenge.total_points }} points
        </p>
        <p>
          {{ challenge.summary }}
        </p>
      </template>
    </emmental-box>
    <div class="columns">
      <div class="column is-two-thirds">
        <div class="box description-box">
          <div
            class="content description-content"
            v-html="challenge.description"
          />
          <hr>
          <challenge-details-hints
            :challenge="challenge"
            :participation="participation"
          />
        </div>
      </div>
      <div class="column">
        <challenge-details-participation
          v-if="isAuthenticated"
          :challenge="challenge"
          :participation="participation"
        />
        <challenge-details-rating
          :challenge="challenge"
          :participation="participation"
        />
      </div>
    </div>
    <confirm-modal
      title="Delete Challenge"
      message="Are you sure you want to delete this challenge ?"
      :toggle="confirmDeleteMode"
      @confirm="onDelete"
      @exit="confirmDeleteMode=false"
    />
  </div>
</template>

<script  lang="ts">
import {
  Prop,
  Component,
  Vue,
} from 'vue-property-decorator';
import { State, Getter, Action } from 'vuex-class';
import { Challenge } from '../store/challenges/types';
import { ChallengeParticipation } from '../store/challengeParticipations/types';

import EmmentalBox from '@/components/EmmentalBox.vue';
import EmmentalCard from '@/components/EmmentalCard.vue';
import EmmentalModal from '@/components/EmmentalModal.vue';
import ConfirmModal from '@/components/ConfirmModal.vue';
import ChallengeEditCard from '@/components/ChallengeEditCard.vue';
import ChallengeDetailsHints from '@/components/ChallengeDetailsHints.vue';
import ChallengeDetailsRating from '@/components/ChallengeDetailsRating.vue';
import ChallengeDetailsParticipation from '@/components/ChallengeDetailsParticipation.vue';

@Component({
  name: 'ChallengeDetails',
  components: {
    EmmentalBox,
    EmmentalCard,
    EmmentalModal,
    ConfirmModal,
    ChallengeEditCard,
    ChallengeDetailsHints,
    ChallengeDetailsRating,
    ChallengeDetailsParticipation,
  },
})
export default class ChallengeDetails extends Vue {
  // Challenge

  @Prop({
    type: String,
    required: true,
  })
  public categorySlug!: string;

  @Prop({
    type: String,
    required: true,
  })
  public challengeSlug!: string;

  @Getter('getChallengeFromSlug', { namespace: 'challenges' })
  public getChallengeFromSlug!: CallableFunction;

  get challenge(): Challenge {
    return this.getChallengeFromSlug(this.challengeSlug);
  }

  // Admin actions

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

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

  // Challenge Delete

  public confirmDeleteMode = false;

  @Action('deleteChallenge', { namespace: 'challenges' })
  public deleteChallenge!: CallableFunction;

  @Getter('getCategoryById', { namespace: 'challengeCategories' })
  public getCategoryById!: CallableFunction;

  public onDelete() {
    const catSlug = this.getCategoryById(this.challenge.category_id).title_slug;
    this.deleteChallenge(this.challenge.challenge_id).then(() => {
      this.$router.push(`/challenges/${catSlug}`);
    });
  }

  // Challenge Participation

  @Getter('getParticipationByChallengeId', { namespace: 'challengeParticipations' })
  public getParticipationByChallengeId!: CallableFunction;

  get participation(): ChallengeParticipation|undefined {
    const challengeId = this.challenge && this.challenge.challenge_id;
    return this.getParticipationByChallengeId(challengeId);
  }

  @Getter('getParticipationFinalScore', { namespace: 'challengeParticipations' })
  public getParticipationFinalScore!: CallableFunction

  get finalPoints() {
    return this.participation
      ? this.getParticipationFinalScore(this.participation.participation_id) : 0;
  }

  @State('isAuthenticated')
  public isAuthenticated!: boolean;
}
</script>

<style lang="scss" scoped>
.columns {
    margin-top: 1rem;
}
.is-4 {
  font-size: 1.75rem;
}
.description-box {
  height: 63vh;
  overflow-y: auto;
}
.button-hint {
  min-width:30%;
}
.description-content {
  min-height: 60%;
}
</style>
