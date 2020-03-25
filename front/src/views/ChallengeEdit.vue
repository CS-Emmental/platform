<template>
  <div class="challenge-create">
    <challenge-edit-card
      :challenge="challenge"
      @save="save"
    />
  </div>
</template>

<script lang="ts">
import {
  Prop, Component, Vue,
} from 'vue-property-decorator';
import { Action, Getter } from 'vuex-class';

import { Challenge } from '../store/challenges/types';
import { slug } from '../store/utils';

import ChallengeEditCard from '@/components/ChallengeEditCard.vue';

@Component({
  name: 'ChallengeEdit',
  components: {
    ChallengeEditCard,
  },
})
export default class ChallengeEdit extends Vue {
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

  @Getter('getCategoryById', { namespace: 'challengeCategories' })
  public getCategoryById!: CallableFunction;

  @Action('postChallenge', { namespace: 'challenges' })
  public postChallenge!: CallableFunction;

  public save(edited: Challenge) {
    this.postChallenge(edited).then(() => {
      if (edited.title !== this.challenge.title
        || edited.category_id !== this.challenge.category_id) {
        const catSlug = this.getCategoryById(edited.category_id).title_slug;
        const challSlug = slug(edited.title);
        this.$router.push(`/challenges/${catSlug}/${challSlug}`);
      }
    });
  }
}
</script>

<style lang="scss" scoped>
</style>
