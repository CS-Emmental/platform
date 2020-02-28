<template>
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
</template>

<script  lang="ts">
import {
  Prop,
  Component,
  Vue,
} from 'vue-property-decorator';
import { Action } from 'vuex-class';
import { Challenge, ChallengeParticipation } from '../store/challenges/types';

@Component({
  name: 'ChallengeDetailsRating',
})
export default class ChallengeDetailsRating extends Vue {
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

  @Action('postParticipation', { namespace: 'challenges' })
  public postParticipation!: CallableFunction;

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

  public onRating(n: number) {
    if (this.participation) {
      this.postParticipation({ ...this.participation, rating: n }).then(() => {
        this.$toasted.show(`You rated this challenge ${n}.0`);
      });
    } else {
      this.$toasted.show('Start this challenge before rating it');
    }
  }
}
</script>

<style lang="scss" scoped>
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
</style>
