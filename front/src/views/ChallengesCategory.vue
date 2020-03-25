<template>
  <div class="challenge-category">
    <emmental-box
      v-if="category"
      :actions="actions"
      class="header-box"
      @edit="editMode=true"
      @delete="confirmDeleteMode=true"
    >
      <template v-slot:header>
        <h1 class="title level-item">
          <i
            :class="category.icon"
            class="title-icon"
          />
          {{ category.title }}
        </h1>
      </template>
      <template v-slot:content>
        <p class="subtitle is-4">
          {{ categoryCount }} Challenge{{ categoryCount === 1 ? '': 's' }}
        </p>
        <p>
          {{ category.description }}
        </p>
      </template>
    </emmental-box>
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
    <emmental-modal :is-active="createMode">
      <challenge-edit-card
        v-if="createMode"
        :challenge="newChallenge"
        @quit="createMode=false"
        @save="insert"
      />
    </emmental-modal>
    <emmental-modal :is-active="editMode">
      <challenges-category-edit-card
        v-if="editMode"
        :challenge-category="category"
        @quit="editMode=false"
        @save="save"
      />
    </emmental-modal>
    <confirm-modal
      title="Delete Challenge Category"
      :message="deleteCategory"
      :toggle="confirmDeleteMode"
      @confirm="onDelete"
      @exit="confirmDeleteMode=false"
    />
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter, Action } from 'vuex-class';
import { ChallengeCategory } from '../store/challengeCategories/types';
import { Challenge } from '../store/challenges/types';
import { slug } from '../store/utils';

import ChallengesCategoryEditCard from '@/components/ChallengesCategoryEditCard.vue';
import EmmentalBox from '@/components/EmmentalBox.vue';
import EmmentalModal from '@/components/EmmentalModal.vue';
import NewBox from '@/components/NewBox.vue';
import ConfirmModal from '@/components/ConfirmModal.vue';
import ChallengeCard from '@/components/ChallengeCard.vue';
import ChallengeEditCard from '@/components/ChallengeEditCard.vue';

@Component({
  name: 'ChallengesCategory',
  components: {
    EmmentalBox,
    EmmentalModal,
    NewBox,
    ConfirmModal,
    ChallengeCard,
    ChallengeEditCard,
    ChallengesCategoryEditCard,
  },
})
export default class ChallengesCategory extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public categorySlug!: string;

  public editMode = false;

  public createMode = false;

  public confirmDeleteMode = false;

  public deleteCategory = `Are you sure you want to delete this challenge category ?
  If you do so the remaining challenges won't be accessible anymore`

  @Getter('getCategoryFromSlug', { namespace: 'challengeCategories' })
  public getCategoryFromSlug!: CallableFunction;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getChallengesCountByCategory', { namespace: 'challenges' })
  public getChallengesCountByCategory!: CallableFunction;

  @Getter('getChallengesByCategory', { namespace: 'challenges' })
  public getChallengesByCategory!: CallableFunction;

  @Action('insertChallenge', { namespace: 'challenges' })
  public insertChallenge!: CallableFunction;

  @Action('postChallengeCategory', { namespace: 'challengeCategories' })
  public postChallengeCategory!: CallableFunction;


  public insert(insertChallenge: Challenge) {
    const inserted = { ...insertChallenge };
    delete inserted.challenge_id;
    this.insertChallenge(inserted).then(() => {
      this.createMode = false;
      this.$toasted.show(`New challenge '${inserted.title}' created`);
    });
  }

  public save(edited: ChallengeCategory) {
    this.postChallengeCategory(edited).then(() => {
      this.editMode = false;
      const catSlug = slug(edited.title);
      this.$router.push(`/challenges/${catSlug}`);
    });
  }

  get newChallenge(): Challenge {
    return this.category && {
      challenge_id: '',
      title: '',
      title_slug: '',
      summary: '',
      description: '',
      category_id: this.category.category_id,
      total_points: 100,
      flags: [
        {
          reward: 1,
          secret: '',
          text: '',
        },
      ],
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
      hints: [],
      challenge_type: 'web',
      created_at: 0,
      updated_at: 0,
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

  @Action('deleteChallengeCategory', { namespace: 'challengeCategories' })
  public deleteChallengeCategory!: CallableFunction;

  public onDelete() {
    this.deleteChallengeCategory(this.category.category_id).then(() => {
      this.$router.push('/challenges/');
    });
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
.modal-content {
  width: 60vw;
}
.title-icon {
  margin-right: .5rem;
}
</style>
