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
    />
    <div class="columns">
      <div class="column is-two-thirds">
        <div class="box">
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
              <button v-else class="button" @click="activeHints.push(index)">
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
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';
import { Challenge } from '../store/challenges/types';

import EmmentalBox from '@/components/EmmentalBox.vue';

const namespace = 'challenges';

@Component({
  name: 'ChallengesCategory',
  components: {
    EmmentalBox,
  },
})
export default class ChallengesCategory extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public categoryKebab!: string;

  @Prop({
    type: String,
    required: true,
  })
  public challengeKebab!: string;


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
  ];

  @Getter('getChallengeFromKebab', { namespace })
  public getChallengeFromKebab!: CallableFunction;

  @Getter('hasPermission')
  public hasPermission!: CallableFunction;

  get challenge(): Challenge {
    return this.getChallengeFromKebab(this.challengeKebab);
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
</style>
