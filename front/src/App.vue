<template>
  <div id="app">
    <emmental-navbar />
    <emmental-sidebar />
    <router-view class="main" />
  </div>
</template>

<script lang="ts">
import { Vue, Component, Watch } from 'vue-property-decorator';
import { Action, State } from 'vuex-class';
import EmmentalNavbar from '@/components/EmmentalNavbar.vue';
import EmmentalSidebar from '@/components/EmmentalSidebar.vue';

@Component({
  components: {
    EmmentalNavbar,
    EmmentalSidebar,
  },
})
export default class App extends Vue {
  @Action('getConfig')
  public getConfig!: CallableFunction;

  @Action('challenges/getCurrentuserChallengeParticipations')
  public getCurrentuserChallengeParticipations!: CallableFunction;

  @State('isAuthenticated')
  public isAuthenticated!: boolean;

  @Watch('isAuthenticated')
  onIsAuthenticated(value: boolean) {
    if (value) {
      this.getCurrentuserChallengeParticipations();
    }
  }

  public created() {
    this.getConfig();
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Orbitron&display=swap');
@import "vue-select/src/scss/vue-select.scss";
@import '@/bulma-theme.scss';
#app {
  font-family: 'Orbitron', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
  background-color: #e0e0e0;

  .button {
    font-family: 'Orbitron', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
}
.main {
  margin-left: 18vw;
  padding: 1rem;
  padding-top: 8vh;
}
*::-webkit-scrollbar-track
{
  border-radius: 10px;
  background-color: #EEE;
}

*::-webkit-scrollbar
{
  width: 12px;
  border-radius: 10px;
  background-color: #F5F5F5;
}

*::-webkit-scrollbar-thumb
{
  border-radius: 10px;
  background-color: #2c3e50;
}

.toasted-primary.emmental-toast {
  background-color: #2c3e50;
  border-radius: 5px;
  font-family: 'Orbitron', Helvetica, Arial, sans-serif;
  line-height: 1.5rem;

  .emmental-toast-action {
    color: white;
  }
}

.toasted-primary.emmental-toast.error {
  background-color: #d14a38;
}
</style>
