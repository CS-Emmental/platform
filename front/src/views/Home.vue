<template>
  <div class="home">
    <emmental-box
      class="header-box"
      :box-props="boxContent"
    />
  </div>
</template>

<script  lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import EmmentalBox from '@/components/EmmentalBox.vue';

@Component({
  name: 'Home',
  components: {
    EmmentalBox,
  },
})
export default class Home extends Vue {
  public boxContent = {
    title: 'Welcome Home',
    subtitle: 'To come : Last subscribe - last challenge solved - last article',
  }
}
</script>

<style lang="scss" scoped>
.header-box {
  padding-top: 3rem;
  padding-bottom: 3rem;
}
</style>
