<template>
<nav class="navbar is-dark" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <router-link to="/" class="navbar-item">
      <img src="../assets/cheese.png" width="35" height="60">
    </router-link>

    <a role="button"
       class="navbar-burger burger"
       :class="{'is-active': isActive}"
       aria-label="menu"
       aria-expanded="false"
       data-target="navbarBasicExample"
       @click="isActive = !isActive">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarEmmental" class="navbar-menu" :class="{'is-active': isActive}">
    <div class="navbar-start">
      <a class="navbar-item is-active">
        Challenges
      </a>

      <a class="navbar-item">
        Leaderboard
      </a>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light">
            Log in
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
@Component({})
export default class EmmentalNavbar extends Vue {
  public name: string = 'EmmentalNavbar';
  private isActive: boolean = false;
}
</script>

<style lang="scss" scoped>
</style>
