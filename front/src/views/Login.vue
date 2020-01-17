<template>
  <div>
    <div class="box login-box">
      <div class="title">
        Log In
      </div>
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input
            v-model="emailInput"
            class="input"
            type="email"
            placeholder="Email"
          >
          <span class="icon is-small is-left">
            <i class="fas fa-envelope" />
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check" />
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="passwordInput"
            class="input"
            type="password"
            placeholder="Password"
          >
          <span class="icon is-small is-left">
            <i class="fas fa-lock" />
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control">
          <button
            class="button is-primary"
            @click="login({email: emailInput, password: passwordInput})"
          >
            Login
          </button>
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Action } from 'vuex-class';

@Component({
  name: 'Login',
})
export default class Login extends Vue {
  public emailInput = '';

  public passwordInput = '';

  @Action('login')
  public login!: CallableFunction;
}
</script>

<style lang="scss" scoped>
.login-box {
  max-width: 50vw;
  margin: auto;
  text-align: center;
  margin-top: 2rem;
  .control {
    text-align: center;
  }
  .button {
    margin-top: 1rem;
    width: 80%;
  }
}
</style>
