<template>
  <div class="challenges">
    <div class="box">
      <h1 class="title is-1">
      <i class="fas fa-shield-alt title-icon"></i>
      Challenges
    </h1>
    <p class="subtitle is-4">
      Un nombre incroyable de 1 challenge super compliqué !
    </p>
    <p>
      Cliquez sur une des catégories suivantes afin d'explorer les nombreux challenges proposés sur CS Emmental.
    </p>
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
</style>
