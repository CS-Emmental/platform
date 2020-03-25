<template>
  <div class="challenge-create">
    <challenge-edit-card
      :challenge="challengeCreate"
      @save="save"
    />
  </div>
</template>

<script lang="ts">
import {
  Prop, Component, Vue, Watch,
} from 'vue-property-decorator';
import { Action, Getter } from 'vuex-class';

import { Challenge } from '../store/challenges/types';
import { ChallengeCategory } from '../store/challengeCategories/types';

import ChallengeEditCard from '@/components/ChallengeEditCard.vue';

@Component({
  name: 'ChallengeCreate',
  components: {
    ChallengeEditCard,
  },
})
export default class ChallengeCreate extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public categorySlug!: string;

  @Getter('getCategoryFromSlug', { namespace: 'challengeCategories' })
  public getCategoryFromSlug!: CallableFunction;

  get category(): ChallengeCategory {
    return this.getCategoryFromSlug(this.categorySlug);
  }

  public challengeCreate: Challenge = {
    challenge_id: '',
    title: '',
    title_slug: '',
    summary: '',
    description: '',
    category_id: '',
    total_points: 100,
    flags: [
      {
        reward: 1,
        secret: '',
        text: '',
      },
    ],
    hints: [],
    containers: {
      containers: {
        dns_name: {
          image: 'image_name',
          env: {
            ENV_VAR: 'value',
          },
          ports: [80],
          open: [
            {
              container: 'other_container_name',
              ports: [80],
            },
            {
              container: 'container_with_all_ports_accessible',
            },
          ],
        },
      },
      exposed: {
        container: 'dns_name',
        port: 80,
      },
    },
    challenge_type: 'web',
    created_at: 0,
    updated_at: 0,
  };

  @Watch('category', { immediate: true, deep: true })
  onCategoryChanged() {
    this.challengeCreate.category_id = this.category && this.category.category_id;
  }

  @Action('insertChallenge', { namespace: 'challenges' })
  public insertChallenge!: CallableFunction;

  public save(insertChallenge: Challenge) {
    const inserted = { ...insertChallenge };
    delete inserted.challenge_id;
    this.insertChallenge(inserted).then(() => {
      this.$toasted.show(`New challenge '${inserted.title}' created`);
    });
  }
}
</script>

<style lang="scss" scoped>
</style>
