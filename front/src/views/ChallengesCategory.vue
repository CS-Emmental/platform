<template>
  <div class="challenge-category">
    <emmental-box
      v-if="category"
      :title="category.title"
      :icon="category.icon"
      :subtitle="`${categoryCount} Challenge${categoryCount == 1 ? '' : 's'}`"
      :content="category.description"
      :actions="actions"
      class="header-box"
    />
    <div
      v-if="category"
      class="challenges"
    >
      <challenge-card
        v-for="challenge in getChallengesByCategory(category.category_id)"
        :key="challenge.challenge_id"
        :challenge="challenge"
      />
      <new-box
        v-if="hasPermission('admin')"
        collection="challenge"
        @click.native="createMode=true"
      />
    </div>
    <div
      class="modal"
      :class="{'is-active': createMode}"
      tabindex="0"
      @keyup.esc="createMode=false"
    >
      <div class="modal-background" />
      <div class="modal-content">
        <challenge-edit-card
          :challenge="newChallenge"
          @quit="createMode=false"
          @save="insert"
        />
      </div>
    </div>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter, Action } from 'vuex-class';
import { ChallengeCategory, Challenge } from '../store/challenges/types';

import EmmentalBox from '@/components/EmmentalBox.vue';
import NewBox from '@/components/NewBox.vue';
import ChallengeCard from '@/components/ChallengeCard.vue';
import ChallengeEditCard from '@/components/ChallengeEditCard.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengesCategory',
  components: {
    EmmentalBox,
    NewBox,
    ChallengeCard,
    ChallengeEditCard,
  },
})
export default class ChallengesCategory extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public categorySlug!: string;

  public createMode = false;

  @Getter('getCategoryFromSlug', { namespace })
  public getCategoryFromSlug!: CallableFunction;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getChallengesCountByCategory', { namespace })
  public getChallengesCountByCategory!: CallableFunction;

  @Getter('getChallengesByCategory', { namespace })
  public getChallengesByCategory!: CallableFunction;

  @Action('insertChallenge', { namespace })
  public insertChallenge!: CallableFunction;

  public insert(insertChallenge: Challenge) {
    const inserted = { ...insertChallenge };
    delete inserted.challenge_id;
    this.insertChallenge(inserted).then(() => {
      this.createMode = false;
    });
  }

  get newChallenge(): Challenge {
    return this.category && {
      challenge_id: '',
      title: '',
      summary: '',
      description: '',
      category_id: this.category.category_id,
      total_points: 100,
    };
  }

  get categoryCount() {
    return this.category && this.getChallengesCountByCategory(this.category.category_id);
  }

  get category(): ChallengeCategory {
    return this.getCategoryFromSlug(this.categorySlug);
  }

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
}
</script>

<style lang="scss" scoped>
.challenges {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  height: auto;
  margin-top: 3rem;
}
.new-box {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
  text-align: center;
}
.modal-content {
  width: 60vw;
}
</style>
