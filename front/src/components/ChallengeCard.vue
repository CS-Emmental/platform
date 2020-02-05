<template>
  <emmental-card>
    <template v-slot:header>
      <router-link
        :to="`/challenges/${categorySlug}/${challengeSlug}`"
        class="subtitle is-4 card-header-title"
      >
        {{ challenge.title }}
      </router-link>
    </template>
    <template v-slot:content>
      <p class="subtitle is-6">
        {{ finalPoints }}/{{ challenge.total_points }} points
      </p>
      <p>
        {{ challenge.summary }}
      </p>
    </template>
  </emmental-card>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import EmmentalCard from '@/components/EmmentalCard.vue';
import { Challenge, ChallengeParticipation } from '../store/challenges/types';
import { slug } from '../store/utils';

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

  @Getter('getCategoryById', { namespace })
  public getCategoryById!: CallableFunction;

  get parentCategory() {
    return this.getCategoryById(this.challenge.category_id);
  }

  get categorySlug() {
    return this.parentCategory && slug(this.parentCategory.title);
  }

  get challengeSlug() {
    return this.challenge && slug(this.challenge.title);
  }

  // Challenge Participation

  @Getter('getParticipationByChallengeId', { namespace })
  public getParticipationByChallengeId!: CallableFunction;

  get participation(): ChallengeParticipation|undefined {
    const challengeId = this.challenge && this.challenge.challenge_id;
    return this.getParticipationByChallengeId(challengeId);
  }

  @Getter('getParticipationFinalScore', { namespace })
  public getParticipationFinalScore!: CallableFunction

  get finalPoints() {
    return this.participation
      ? this.getParticipationFinalScore(this.participation.participation_id) : 0;
  }
}
</script>

<style lang="scss" scoped>
</style>
