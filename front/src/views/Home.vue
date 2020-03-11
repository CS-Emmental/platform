<template>
  <div class="challenges">
    <emmental-box class="header-box">
      <template v-slot:header>
        <h1 class="title level-item">
          <i class="title-icon fas fa-cheese" />
          CentraleSupélec Emmental
        </h1>
      </template>
      <template v-slot:content>
        <p class="subtitle is-4">
          A digital platform with numerous challenges and articles.
        </p>
      </template>
    </emmental-box>
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-8">
        <div class="tile is-parent">
          <article class="tile is-child notification is-primary">
            <p class="title">
              Solve numerous challenges
            </p>
            <br>
            <p class="has-text-centered">
              <span class="icon is-large">
                <i class="fas fa-trophy fa-5x" />
              </span>
            </p>
            <br>
            <p>
              CS Emmental proposes various challenge categories to train
              multiple skills such as reverse engineering, hacking, forensic, etc ...
            </p>
            <p>
              You only need to <a href="/signup">create an account</a> on the platform
              and start a challenge wich is hosted on our side.
            </p>
            <p />
          </article>
        </div>
        <div class="tile">
          <div class="tile is-parent">
            <article class="tile is-child notification is-info">
              <p class="title is-4">
                Create your own challenges
              </p>
              <br>
              <p class="has-text-centered">
                <span class="icon is-large">
                  <i class="fab fa-docker fa-5x" />
                </span>
              </p>
              <br>
              <p>
                Follow our
                <a
                  href="https://github.com/CS-Emmental/documentation"
                  target="_blank"
                >documentation</a> to create your own dockerized challenges
                and propose them to the community.
              </p>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-dark">
              <p class="title is-4">
                A social platform
              </p>
              <br>
              <p class="has-text-centered">
                <span class="icon is-large">
                  <i class="fas fa-users fa-5x" />
                </span>
              </p>
              <br>
              <p>
                Share your knowledge through <a href="/articles">articles</a>,
                helping forums and compare your results in the
                <a href="/leaderboard">leaderboards</a>.
              </p>
            </article>
          </div>
        </div>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child notification box">
          <div class="content">
            <p class="title">
              Last challenges
            </p>
            <div
              v-for="challenge in lastChallenges"
              :key="challenge.challenge_id"
            >
              <challenge-level :challenge="challenge" />
              <hr>
            </div>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Getter } from 'vuex-class';

import { Challenge } from '../store/challenges/types';

import EmmentalBox from '@/components/EmmentalBox.vue';
import ChallengeLevel from '@/components/ChallengeLevel.vue';

@Component({
  name: 'Home',
  components: {
    EmmentalBox,
    ChallengeLevel,
  },
})
export default class Home extends Vue {
  @Getter('getLastChallenges', { namespace: 'challenges' })
  public lastChallenges!: Challenge[];
}
</script>

<style lang="scss" scoped>
hr {
  border: solid 1px #ddd;
}
.challenge-link {
  cursor: pointer;
}
.header-box {
  padding-top: 3rem;
  padding-bottom: 3rem;
  .title-icon {
    margin-right: 0.5rem;
  }
}
.tile.is-ancestor {
  margin-top: 3rem;
}
</style>
