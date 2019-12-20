<template>
  <div id="app">
    <emmental-navbar />
    <emmental-sidebar />
    <router-view class="main" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import EmmentalNavbar from '@/components/EmmentalNavbar.vue';
import EmmentalSidebar from '@/components/EmmentalSidebar.vue';

@Component({
  components: {
    EmmentalNavbar,
    EmmentalSidebar,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Orbitron&display=swap');
@import '@/bulma-theme.scss';
#app {
  font-family: 'Orbitron', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
  background-color: #e0e0e0;
}
.main {
  margin-left: 18vw;
  padding: 1rem;
}
</style>
