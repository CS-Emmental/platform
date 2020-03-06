<template>
  <emmental-card>
    <template v-slot:header>
      <div class="level">
        <div class="level-left">
          <router-link
            :to="`/challenges/${parentCategory.title_slug}/${challengeSlug}`"
            class="subtitle is-4 level-item card-header-title"
          >
            {{ challenge.title }}
          </router-link>
          <emmental-status-tag
            v-if="participation"
            class="level-item"
            :status="participation.status"
          />
        </div>
      </div>
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

import { Challenge } from '../store/challenges/types';
import { ChallengeParticipation } from '../store/challengeParticipations/types';
import { slug } from '../store/utils';

import EmmentalStatusTag from '@/components/EmmentalStatusTag.vue';
import EmmentalCard from '@/components/EmmentalCard.vue';

@Component({
  name: 'ChallengeCard',
  components: {
    EmmentalStatusTag,
    EmmentalCard,
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

  get challengeSlug() {
    return this.challenge && slug(this.challenge.title);
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
}
</script>

<style lang="scss" scoped>
.level-item.subtitle {
  margin-bottom: 0;
}
</style>
