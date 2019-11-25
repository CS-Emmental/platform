<template>
  <div id="app">
    <emmental-navbar/>
    <emmental-sidebar/>
    <router-view class="main"/>
  </div>
</template>

<script>
import EmmentalNavbar from '@/views/EmmentalNavbar.vue';
import EmmentalSidebar from '@/views/EmmentalSidebar.vue';

export default {
  components: {
    EmmentalNavbar,
    EmmentalSidebar,
  },
};
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
}
.main {
  margin-left: 18vw;
}
</style>
