<template>
<div class="box emmental-box">
  <router-link :to="boxProps.link" class="subtitle is-4">
    <i :class="boxProps.icon"></i>
    {{ boxProps.title }}
  </router-link>
  <p class="subtitle is-6">
    {{ boxProps.subtitle }}
  </p>
  <slot name="content">
    <p>
      {{ boxProps.content }}
    </p>
  </slot>
</div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

interface BoxPropsInterface {
  title: string;
  link?: string;
  icon?: string;
  subtitle?: string;
  content?: string;
}

@Component({
  name: 'EmmentalBox',
})
export default class EmmentalBox extends Vue {
  @Prop({
    type: Object as () => BoxPropsInterface,
    required: true,
  })
  public boxProps;
}
</script>

<style lang="scss" scoped>
.subtitle.is-6 {
  margin-top: 1rem;
}
.emmental-box:not(:last-child) {
  margin-bottom: 0;
  
}
</style>
