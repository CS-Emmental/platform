<template>
  <div
    v-if="challenge"
    class="challenge-details"
  >
    <emmental-box
      :title="challenge.title"
      :subtitle="`${points}/${challenge.total_points} points`"
      :content="challenge.summary"
      :actions="actions"
      class="header-box"
      @edit="editMode=true"
      @delete="confirmDeleteMode=true"
    />
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
            <div
              v-for="(hint, index) in hints"
              :key="hint.text"
              class="hint"
            >
              <p v-if="activeHints.includes(index)">
                Hint n° {{ index }}: {{ hint.text }}
              </p>
              <button
                v-else
                class="button"
                @click="activeHints.push(index)"
              >
                Show hint n°{{ index }}
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="column">
        <div class="start">
          <button class="button is-primary is-large is-fullwidth">
            Start challenge
          </button>
        </div>
        <div class="box">
          <h2 class="title is-4">
            Rate this challenge
          </h2>
          <p class="rating">
            <span
              v-for="n in 5"
              :key="n"
              class="icon is-large rating-icon"
              @click="rating=n"
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
          <hr>
          <h2 class="title is-4">
            Recent Activity
          </h2>
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
    <emmental-modal :is-active="confirmDeleteMode">
      <div
        class="card confirm-delete-card"
        tabindex="0"
        @keyup.enter="onDelete"
        @keyup.esc="confirmDeleteMode=false"
      >
        <header class="card-header">
          <p class="card-header-title">
            Delete Challenge
          </p>
          <div class="card-header-icon">
            <button
              class="delete"
              @click="confirmDeleteMode=false"
            />
          </div>
        </header>
        <div class="card-content">
          <p>
            Are you sure you want to delete this challenge ?
          </p>
        </div>
        <footer class="card-footer">
          <a
            class="card-footer-item"
            @click="onDelete"
          >Confirm</a>
          <a
            class="card-footer-item"
            @click="confirmDeleteMode=false"
          >Cancel</a>
        </footer>
      </div>
    </emmental-modal>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter, Action } from 'vuex-class';
import { Challenge } from '../store/challenges/types';
import { slug } from '../store/utils';

import EmmentalBox from '@/components/EmmentalBox.vue';
import EmmentalCard from '@/components/EmmentalCard.vue';
import EmmentalModal from '@/components/EmmentalModal.vue';
import ChallengeEditCard from '@/components/ChallengeEditCard.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengesCategory',
  components: {
    EmmentalBox,
    EmmentalCard,
    EmmentalModal,
    ChallengeEditCard,
  },
})
export default class ChallengesCategory extends Vue {
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

  public editMode = false;

  public confirmDeleteMode = false;

  // todo
  public points = 0;

  public rating = 3;

  public activeHints: number[] = [];

  public hints = [
    {
      text: 'Bonjour 1',
    },
    {
      text: 'Bonjour 2',
    },
    {
      text: 'Bonjour 3',
    },
    {
      text: 'Bonjour 4',
    },
  ];

  @Getter('getChallengeFromSlug', { namespace })
  public getChallengeFromSlug!: CallableFunction;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  @Getter('getCategoryById', { namespace })
  public getCategoryById!: CallableFunction;

  @Action('postChallenge', { namespace })
  public postChallenge!: CallableFunction;

  @Action('deleteChallenge', { namespace })
  public deleteChallenge!: CallableFunction;

  get challenge(): Challenge {
    return this.getChallengeFromSlug(this.challengeSlug);
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

  public onDelete() {
    const catSlug = slug(this.getCategoryById(this.challenge.category_id).title);
    this.deleteChallenge(this.challenge.challenge_id).then(() => {
      this.$router.push(`/challenges/${catSlug}`);
    });
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
.start {
  margin-bottom: 1rem;
}
.description-box {
  height: 65vh;
  overflow-y: auto;
}
.confirm-delete-card {
  width: 30vw;
  margin: auto;
}
</style>
