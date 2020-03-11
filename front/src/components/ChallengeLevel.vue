<template>
  <div class="level">
    <div class="level-left">
      <router-link
        :to="`/challenges/${parentCategory.title_slug}/${challenge.title_slug}`"
        tag="div"
        class="subtitle is-5 level-item challenge-link"
      >
        {{ challenge.title }}
      </router-link>
    </div>
    <div class="level-right">
      <div
        v-if="participation"
        class="level-item"
      >
        <div>
          <i
            class="fas fa-circle"
            :class="style"
          />
        </div>
      </div>
      <div class="level-item">
        <div class="subtitle is-6 points">
          {{ finalPoints }}/{{ challenge.total_points }}
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';

import { Challenge } from '../store/challenges/types';
import { ChallengeParticipation } from '../store/challengeParticipations/types';

import EmmentalStatusTag from '@/components/EmmentalStatusTag.vue';

@Component({
  name: 'ChallengeCard',
  components: {
    EmmentalStatusTag,
  },
})
export default class ChallengeCard extends Vue {
  @Prop({
    type: Object as () => Challenge,
    required: true,
  })
  public challenge!: Challenge;

  @Getter('getCategoryById', { namespace: 'challengeCategories' })
  public getCategoryById!: CallableFunction;

  get parentCategory() {
    return this.getCategoryById(this.challenge.category_id);
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

  public style_dict: {[id: string]: string} = {
    ongoing: 'has-text-primary',
    stopped: 'has-text-danger',
    finished: 'has-text-success',
  };

  get style(): string {
    if (this.participation) {
      return this.style_dict[this.participation.status] || '';
    }
    return '';
  }
}
</script>

<style lang="scss" scoped>
.challenge-link {
  cursor: pointer;
}
.level-item.subtitle {
  margin-bottom: 0;
}
.points {
  min-width: 5rem;
  text-align: right;
}
</style>
