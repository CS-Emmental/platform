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
      <challenge-group-box v-for="group in groups" :key="group.id" :group="group"/>
    </div>
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ChallengeGroupBox from '@/components/ChallengeGroupBox.vue';

@Component({
  name: 'Challenges',
  components: {
    ChallengeGroupBox,
  },
})
export default class Challenges extends Vue {
  public groups = [
    {
      title: 'Web',
      kebab: 'web',
      id: 'aefdcjnevfptrhfmvdcs',
      icon: 'fas fa-globe',
      description: 'Exploit common websites weaknesses, configuration mistakes and vulnerability patterns...',
      challengesCount: 6,
    },
    {
      title: 'Network',
      kebab: 'network',
      id: 'aefdcjnevfdjkdskdscs',
      icon: 'fas fa-network-wired',
      description: 'Exploit common websites weaknesses, configuration mistakes and vulnerability patterns...',
      challengesCount: 2,
    },
    {
      title: 'Cryptography',
      kebab: 'cryptography',
      id: 'aefdcjnevfredfdcs',
      icon: 'fas fa-unlock-alt',
      description: 'Exploit common websites weaknesses, configuration mistakes and vulnerability patterns...',
      challengesCount: 3,
    },
  ];
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
</style>
