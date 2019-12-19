<template>
  <div class="card emmental-card">
    <header class="card-header">
      <router-link
        :to="cardProps.link"
        class="subtitle is-4 card-header-title"
      >
        <i
          class="title-icon"
          :class="cardProps.icon"
        />
        {{ cardProps.title }}
      </router-link>
      <p class="card-header-icon">
        <span class="icon">
          <i class="fas fa-ellipsis-h" />
        </span>
      </p>
    </header>
    <div class="card-content">
      <p class="subtitle is-6">
        {{ cardProps.subtitle }}
      </p>
      <slot name="content">
        <p>
          {{ cardProps.content }}
        </p>
      </slot>
    </div>
  </div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

interface CardPropsInterface {
  title: string;
  link?: string;
  icon?: string;
  subtitle?: string;
  content?: string;
}

@Component({
  name: 'EmmentalBox',
})
export default class EmmentalCard extends Vue {
  @Prop({
    type: Object as () => CardPropsInterface,
    required: true,
  })
  public cardProps;
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
