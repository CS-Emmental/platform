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
      <div
        v-if="hasPermission('admin')"
        class="card-header-icon"
      >
        <div
          v-on-clickaway="away"
          class="dropdown"
          :class="{'is-active': dropdownActive}"
        >
          <div
            class="dropdown-trigger"
            @click="dropdownActive = !dropdownActive"
          >
            <span class="icon">
              <i class="fas fa-ellipsis-h" />
            </span>
          </div>
          <div
            id="dropdown-menu"
            class="dropdown-menu"
            role="menu"
          >
            <div class="dropdown-content">
              <a class="dropdown-item">
                Edit
              </a>
              <a class="dropdown-item">
                Delete
              </a>
            </div>
          </div>
        </div>
      </div>
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
import { Getter } from 'vuex-class';
import { mixin as clickaway } from 'vue-clickaway';

interface CardPropsInterface {
  title: string;
  link?: string;
  icon?: string;
  subtitle?: string;
  content?: string;
}

@Component({
  name: 'EmmentalCard',
  mixins: [clickaway],
})
export default class EmmentalCard extends Vue implements clickaway {
  @Prop({
    type: Object as () => CardPropsInterface,
    required: true,
  })
  public cardProps;

  @Getter('hasPermission') public hasPermission;

  public dropdownActive = false;

  public away() {
    this.dropdownActive = false;
  }
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
