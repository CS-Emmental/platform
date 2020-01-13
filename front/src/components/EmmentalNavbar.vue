<template>
  <nav
    class="navbar is-dark"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <router-link
        to="/"
        class="navbar-item brand-item"
      >
        <img
          src="../assets/cheese.png"
          class="emmental-logo"
        >
        <p class="subtitle is-4 has-text-white">
          CS Emmental
        </p>
      </router-link>
      <a
        role="button"
        class="navbar-burger burger"
        :class="{'is-active': isActive}"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
        @click="isActive = !isActive"
      >
        <span aria-hidden="true" />
        <span aria-hidden="true" />
        <span aria-hidden="true" />
      </a>
    </div>

    <div
      id="navbarEmmental"
      class="navbar-menu"
      :class="{'is-active': isActive}"
    >
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link
              v-if="!isAuthenticated"
              to="/signup"
              class="button is-primary"
            >
              <strong>Sign up</strong>
            </router-link>
            <router-link
              v-if="!isAuthenticated"
              to="/login"
              class="button is-light"
            >
              Log in
            </router-link>
            <div v-else>
              <a
                class="button is-light"
                @click="logout"
              >
                Log out
              </a>
              <span>{{ currentUser.username }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { State, Action } from 'vuex-class';
import { User } from '../store/types';
@Component({})
export default class EmmentalNavbar extends Vue {
  public name = 'EmmentalNavbar';

  private isActive = false;

  @State('currentUser') public currentUser: User;

  @State('isAuthenticated') public isAuthenticated: User;

  @Action('logout')
  public logout: CallableFunction;
}
</script>

<style lang="scss" scoped>
.emmental-logo {
  width: 35px;
  height: 60px;
  margin-right: 1rem;
}
.brand-item {
  width: 18vw;
  text-align: center;
  padding-left: 2rem;
}
</style>
