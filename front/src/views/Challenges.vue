<template>
  <div class="challenges">
    <div class="box">
      <h1 class="title is-1">
      <i class="fas fa-shield-alt title-icon"></i>
      Challenges
    </h1>
    <p class="subtitle is-4">
      An incredible amount of 1 super hard challenge !
    </p>
    <p>
      Click on one of the following categories to explore numerous challenges proposed by CS Emmental team or others.
    </p>
    </div>
    <div class="categories">
      <div class="box category-box">
        <router-link to="/challenges/web" class="subtitle is-4">
          <i class="fas fa-globe category-icon"></i>
          Web
        </router-link>
        <p class="subtitle is-6">
          <b>6</b> Challenges
        </p>
        <p>
          Exploit common websites weaknesses, configuration mistakes and vulnerability patterns...
        </p>
      </div>
      <div class="box category-box">
        <router-link to ="/challenges/network" class="subtitle is-4">
          <i class="fas fa-network-wired category-icon"></i>
          Network
        </router-link>
        <p class="subtitle is-6">
          <b>2</b> Challenges
        </p>
        <p>
          Exploit common websites weaknesses, configuration mistakes and vulnerability patterns...
        </p>
      </div>
      <div class="box category-box">
        <router-link to="/challenges/cryptography" class="subtitle is-4">
          <i class="fas fa-unlock-alt category-icon"></i>
          Cryptography
        </router-link>
        <p class="subtitle is-6">
          <b>3</b> Challenges
        </p>
        <p>
          Exploit common websites weaknesses, configuration mistakes and vulnerability patterns...
        </p>
      </div>
    </div>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Challenges extends Vue {
  public name: string = 'Challenges';
}
</script>

<style lang="scss" scoped>
.title-icon {
  margin-right: .5rem;
}
.categories {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  height: auto;
  margin-top: 5rem;
}
.category-box:not(:last-child) {
  margin-bottom: 0;
  
}

.subtitle.is-6 {
  margin-top: 1rem;
}
</style>
