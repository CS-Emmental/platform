<template>
  <div>
    <div class="box signup-box">
      <div class="title">
        Sign up
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input
            v-model="inputs.username"
            class="input"
            type="text"
            placeholder="Username"
          >
          <span class="icon is-small is-left">
            <i class="fas fa-user" />
          </span>
        </p>
      </div>
      <div class="field is-horizontal">
        <div class="field-body">
          <div class="field">
            <p class="control is-expanded">
              <input
                v-model="inputs.firstname"
                class="input"
                type="text"
                placeholder="First Name"
              >
            </p>
          </div>
          <div class="field">
            <p class="control is-expanded">
              <input
                v-model="inputs.lastname"
                class="input"
                type="text"
                placeholder="Last Name"
              >
            </p>
          </div>
        </div>
      </div>
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input
            v-model="inputs.email"
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
            v-model="inputs.password"
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
            @click="signup(inputs)"
          >
            Sign Up
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
  name: 'Signup',
})
export default class Signup extends Vue {
  public inputs = {
    username: '',
    email: '',
    firstname: '',
    lastname: '',
    password: '',
  };

  @Action('signup')
  public signup: CallableFunction;
}
</script>

<style lang="scss" scoped>
.signup-box {
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
