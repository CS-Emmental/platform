<template>
  <div class="card emmental-card">
    <header class="card-header">
      <slot name="header" />
      <div
        v-if="actions"
        class="card-header-icon"
      >
        <div
          v-on-clickaway="away"
          class="dropdown is-right"
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
              <a
                v-for="action in actions"
                :key="action.text"
                class="dropdown-item"
                @click="$emit(action.signal)"
              >
                {{ action.text }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="card-content">
      <slot name="content" />
    </div>
  </div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import { mixin as clickaway } from 'vue-clickaway';


interface Action {
  text: string;
  signal: string;
}

@Component({
  name: 'EmmentalCard',
  mixins: [clickaway],
})
export default class EmmentalCard extends Vue {
  @Prop({
    type: Array as () => Action[],
    required: false,
  })
  public actions: Action[]|undefined;

  public dropdownActive = false;

  public away() {
    this.dropdownActive = false;
  }
}
</script>

<style lang="scss" scoped>
.emmental-card:not(:last-child) {
  margin-bottom: 0;
}
.emmental-card {
  border-radius: 5px;
}
.dropdown-trigger {
  cursor: pointer;
}
</style>
