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
          <a
            class="menu-item" 
            :class="{'is-active': category.id == menuActive.category}">
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

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

interface ChallengeCategory {
  title: string;
  kebab: string;
  id: string;
  count: number;
}

interface ChallengeCategoryGroup {
  title: string;
  id: string;
  categories: ChallengeCategory[];
}

interface ChallengeSidebarProps {
  categoryGroups: ChallengeCategoryGroup[];
}

@Component({})
export default class EmmentalSidebar extends Vue {
  public name: string = 'EmmentalSidebar';
  private menuModel: ChallengeSidebarProps = {
    categoryGroups: [
    {
      title: 'Web',
      id: 'd2d82047-3411-4787-9e0e-4f893af2bc77',
      categories: [
        {
          title: 'SQL Injection',
          kebab: 'sql-injection',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846734',
          count: 5,
        },
        {
          title: 'XSS Injection',
          kebab: 'xss-injection',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846735',
          count: 2,
        },
        {
          title: 'Directory Traversal',
          kebab: 'directory-traversal',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846736',
          count: 3,
        },
      ],
    },
    {
      title: 'Network',
      id: 'd2d82047-3411-4787-9e0e-4f893af2bc78',
      categories: [
        {
          title: 'SQL Injection',
          kebab: 'sql-injection',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846737',
          count: 5,
        },
        {
          title: 'XSS Injection',
          kebab: 'xss-injection',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846738',
          count: 2,
        },
        {
          title: 'Directory Traversal',
          kebab: 'directory-traversal',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846739',
          count: 3,
        },
      ],
    },
    {
      title: 'Cryptography',
      id: 'd2d82047-3411-4787-9e0e-4f893af2bc79',
      categories: [
        {
          title: 'SQL Injection',
          kebab: 'sql-injection',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846740',
          count: 5,
        },
        {
          title: 'XSS Injection',
          kebab: 'xss-injection',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846741',
          count: 2,
        },
        {
          title: 'Directory Traversal',
          kebab: 'directory-traversal',
          id: 'd3f9f26f-7c3b-4a96-a52d-efd50d846742',
          count: 3,
        },
      ],
    },
  ]};
  private menuActive: object = {
    group: 'd2d82047-3411-4787-9e0e-4f893af2bc77',
    category: 'd3f9f26f-7c3b-4a96-a52d-efd50d846735',
  };
}
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
