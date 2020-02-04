<template>
  <div
    v-if="challenge"
    class="challenge-details"
  >
    <emmental-box
      :actions="actions"
      class="header-box"
      @edit="editMode=true"
      @delete="confirmDeleteMode=true"
    >
      <template v-slot:header>
        <h1 class="title level-item">
          {{ challenge.title }}
        </h1>
      </template>
      <template v-slot:content>
        <p class="subtitle is-4">
          {{ points }}/{{ challenge.total_points }} points
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
            class="content"
            v-html="challenge.description"
          />
          <hr>
          <div>
            <h2 class="title is-4">
              Hints
            </h2>
            <div v-if="challenge.hints">
              <div
                v-for="(hint, index) in challenge.hints"
                :key="hint.text"
                class="hint"
              >
                <p v-if="activeHints.includes(index)">
                  Hint n° {{ index+1 }}: {{ hint.text }}
                </p>
                <button
                  v-else
                  class="button button-hint"
                  @click="activeHints.push(index)"
                >
                  Show hint n°{{ index+1 }} for {{ hint.cost*challenge.total_points }} points
                </button>
              </div>
            </div>
            <div v-else>
              There is no hints for this challenge.
            </div>
          </div>
        </div>
      </div>
      <div class="column">
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
            </div>
          </template>
        </div>
        <div class="box">
          <h2 class="title is-4">
            Challenge rating
          </h2>
          <p class="rating">
            <span
              v-for="n in 5"
              :key="n"
              class="icon is-large rating-icon"
              @click="onRating(n)"
            >
              <i
                v-if="rating>=n"
                class="fas fa-star"
              />
              <i
                v-else
                class="far fa-star"
              />
            </span>
          </p>
          <p
            class="has-text-centered"
          >
            {{ ratingMessage }}
          </p>
        </div>
      </div>
    </div>
    <emmental-modal :is-active="editMode">
      <challenge-edit-card
        :challenge="challenge"
        @quit="editMode=false"
        @save="save"
      />
    </emmental-modal>
    <confirm-modal
      title="Reset Challenge"
      message="Are you sure you want to reset your challenge instance ?
               (all current progress will be lost)"
      :toggle="resetMode"
      @confirm="onResetChallenge"
      @exit="resetMode=false"
    />
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
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter, Action } from 'vuex-class';
import { Challenge, ChallengeParticipation } from '../store/challenges/types';
import { slug } from '../store/utils';

import EmmentalBox from '@/components/EmmentalBox.vue';
import EmmentalCard from '@/components/EmmentalCard.vue';
import EmmentalModal from '@/components/EmmentalModal.vue';
import ConfirmModal from '@/components/ConfirmModal.vue';
import ChallengeEditCard from '@/components/ChallengeEditCard.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengeDetails',
  components: {
    EmmentalBox,
    EmmentalCard,
    EmmentalModal,
    ConfirmModal,
    ChallengeEditCard,
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

  @Getter('getChallengeFromSlug', { namespace })
  public getChallengeFromSlug!: CallableFunction;

  get challenge(): Challenge {
    return this.getChallengeFromSlug(this.challengeSlug);
  }

  // Challenge Edit

  public editMode = false;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getCategoryById', { namespace })
  public getCategoryById!: CallableFunction;

  @Action('postChallenge', { namespace })
  public postChallenge!: CallableFunction;

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

  public save(edited: Challenge) {
    this.postChallenge(edited).then(() => {
      this.editMode = false;
      if (edited.title !== this.challenge.title
        || edited.category_id !== this.challenge.category_id) {
        const catSlug = slug(this.getCategoryById(edited.category_id).title);
        const challSlug = slug(edited.title);
        this.$router.push(`/challenges/${catSlug}/${challSlug}`);
      }
    });
  }

  // Challenge Delete

  @Action('deleteChallenge', { namespace })
  public deleteChallenge!: CallableFunction;

  public onDelete() {
    const catSlug = slug(this.getCategoryById(this.challenge.category_id).title);
    this.deleteChallenge(this.challenge.challenge_id).then(() => {
      this.$router.push(`/challenges/${catSlug}`);
    });
  }

  public confirmDeleteMode = false;

  // Challenge Participation

  @Getter('getParticipationByChallengeId', { namespace })
  public getParticipationByChallengeId!: CallableFunction;

  @Action('startChallengeParticipation', { namespace })
  public startChallengeParticipation!: CallableFunction;

  @Action('postParticipation', { namespace })
  public postParticipation!: CallableFunction;

  get participation(): ChallengeParticipation|undefined {
    const challengeId = this.challenge && this.challenge.challenge_id;
    return this.getParticipationByChallengeId(challengeId);
  }

  get points() {
    const progress = this.participation ? this.participation.progress : 0;
    const totalPoints = this.challenge ? this.challenge.total_points : 0;
    return progress * totalPoints;
  }

  get rating() {
    return this.participation ? this.participation.rating : null;
  }

  get ratingMessage() {
    if (this.participation) {
      return this.participation.rating
        ? `You rated this challenge ${this.participation.rating}.0`
        : 'Rate this challenge !';
    }
    return 'Start this challenge before rating.';
  }

  get activeHints() {
    return this.participation ? this.participation.used_hints : [];
  }

  public onStartChallenge() {
    this.startChallengeParticipation(this.challenge.challenge_id);
  }

  public onRating(n: number) {
    if (this.participation) {
      this.postParticipation({ ...this.participation, rating: n }).then(() => {
        this.$toasted.show(`You rated this challenge ${n}.0`);
      });
    } else {
      this.$toasted.show('Start this challenge before rating it');
    }
  }

  public resetMode = false;

  public onResetChallenge() {
    this.resetMode = false;
  }
}
</script>

<style lang="scss" scoped>
.columns {
    margin-top: 1rem;
}
.is-4 {
  font-size: 1.75rem;
}
.rating {
  text-align: center;
}
.rating-icon {
  color: rgb(211, 166, 82);
  cursor: pointer;
}
.rating-icon:hover {
  color: #2c3e50;
  cursor: pointer;
}
.hint {
  padding-bottom: .5rem;
}
.challenge-buttons {
  margin-bottom: 1rem;
}
.description-box {
  height: 63vh;
  overflow-y: auto;
}
.button-hint {
  min-width:30%;
}
</style>
