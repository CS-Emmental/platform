<template>
<aside class="menu">
  <p class="menu-label has-text-primary">
    Categories
  </p>
  <ul class="menu-list">
    <li
      v-for='categoryGroup in menuModel.categoryGroups'
      :key='categoryGroup.id'>
      <a>{{categoryGroup.title}}</a>
      <ul v-if="categoryGroup.id == menuActive.group">
        <li
          v-for="category in categoryGroup.categories"
          :key="category.id">
          <a class="menu-item" :class="{'is-active': category.id == menuActive.category}">
            {{category.title}}
            <span class="tag is-rounded is-small">
            <b>{{category.count}}</b>
          </span>
          </a>
        </li>
      </ul>
    </li>
  </ul>
</aside>
</template>

<script>
import menuMock from '@/mocks/menuMock';

export default {
  name: 'EmmentalSidebar',
  data: () => ({
    menuModel: {},
    menuActive: {
      group: null,
      category: null,
    },
  }),
  created() {
    this.menuModel = menuMock;
    this.menuActive.group = this.menuModel.categoryGroups[0].id;
    this.menuActive.category = this.menuModel.categoryGroups[0].categories[0].id;
  },
};
</script>

<style lang="scss" scoped>
aside {
  height: 100%;
  width: 18vw;
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
.menu-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between
}
.menu-item.is-active {
  background-color: whitesmoke;
  color: #334557;
}
</style>
