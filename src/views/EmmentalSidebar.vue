<template>
<aside class="menu">
  <p class="menu-label has-text-primary">
    Categories
  </p>
  <ul class="menu-list">
    <li><a>Network</a></li>
    <li>
      <a class="is-active">Web</a>
      <ul>
        <li><a>SQL Injection</a></li>
        <li><a>XSS Injection</a></li>
        <li><a>Directory Traversal</a></li>
      </ul>
    </li>
    <li><a>Cryptography</a></li>
  </ul>
</aside>
</template>

<script>
export default {
  name: 'EmmentalSidebar',
};
</script>

<style lang="scss" scoped>
aside {
  height: 100%;
  width: 15vw;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  overflow-x: hidden;
  margin-top: 6vh;
  padding: .5rem;
  background-color: #334557;
  a {
    color: white;
  }
}
</style>
