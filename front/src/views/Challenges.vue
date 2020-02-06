<template>
  <div class="challenges">
    <emmental-box class="header-box">
      <template v-slot:header>
        <h1 class="title level-item">
          <i class="title-icon fas fa-shield-alt" />
          Challenges
        </h1>
      </template>
      <template v-slot:content>
        <p class="subtitle is-4">
          Many challenges to train various skills, from server attack to cryptography.
        </p>
        <p>
          Click on one of the following categories to
          explore numerous challenges proposed by CS Emmental team or others.
        </p>
      </template>
    </emmental-box>
    <div class="categories">
      <challenges-category-card
        v-for="category in categories"
        :key="category.category_id"
        :category="category"
      />
      <new-box
        v-if="hasPermission('admin')"
        collection="challenge-category"
        @click.native="createMode=true"
      />
    </div>
    <emmental-modal :is-active="createMode">
      <challenges-category-edit-card
        v-if="createMode"
        :challengeCategory="newChallengeCategory"
        @quit="createMode=false"
        @save="insert"
      />
    </emmental-modal>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Getter, Action } from 'vuex-class';
import { ChallengesState, ChallengeCategory } from '../store/challenges/types';
import ChallengesCategoryEditCard from '@/components/ChallengesCategoryEditCard.vue';

import EmmentalModal from '@/components/EmmentalModal.vue';
import ChallengesCategoryCard from '@/components/ChallengesCategoryCard.vue';
import EmmentalBox from '@/components/EmmentalBox.vue';
import NewBox from '@/components/NewBox.vue';

const namespace = 'challenges';

@Component({
  name: 'Challenges',
  components: {
    ChallengesCategoryCard,
    EmmentalBox,
    NewBox,
    EmmentalModal,
    ChallengesCategoryEditCard,
  },
})
export default class Challenges extends Vue {
  @State('challenges') public challenges: ChallengesState|undefined;

  @Action('getChallengeCategories', { namespace })
  public getChallengeCategories!: CallableFunction;

  public createMode = false;

  get categories() {
    const categories = this.challenges && this.challenges.challengeCategories;
    return categories || [];
  }

  get newChallengeCategory(): ChallengeCategory {
    return this.challenges.challengeCategories && {
      category_id: '',
      title: '',
      description: '',
      icon: '',
    };
  }

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Action('insertChallengeCategory', { namespace })
  public insertChallengeCategory!: CallableFunction;

  public created() {
    this.getChallengeCategories();
  }

  public insert(insertChallengeCategory: ChallengeCategory) {
    const inserted = { ...insertChallengeCategory };
    delete inserted.category_id;
    this.insertChallengeCategory(inserted).then(() => {
      this.createMode = false;
    });
  }
}
</script>

<style lang="scss" scoped>
.categories {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  height: auto;
  margin-top: 3rem;
}
.header-box {
  padding-top: 3rem;
  padding-bottom: 3rem;
  .title-icon {
    margin-right: .5rem;
  }
}
</style>
