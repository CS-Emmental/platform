<template>
  <div class="box emmental-box">
    <h1 class="title is-1">
      <i :class="boxProps.icon" />
      {{ boxProps.title }}
    </h1>
    <p class="subtitle is-4">
      {{ boxProps.subtitle }}
    </p>
    <p>
      {{ boxProps.content }}
    </p>
  </div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

interface BoxPropsInterface {
  title: string;
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
.card-header-title {
  margin-bottom: 0;
}
.emmental-card:not(:last-child) {
  margin-bottom: 0;
}
.emmental-card {
  border-radius: 5px;
}
.title-icon {
  margin-right: .5rem;
}
</style>
