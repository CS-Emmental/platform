<template>
  <div class="box emmental-box">
    <div class="box-header level">
      <div class="level-left">
        <slot name="header" />
      </div>
      <div class="level-right">
        <div
          v-if="actions"
          v-on-clickaway="away"
          class="dropdown is-right"
          :class="{'is-active': dropdownActive}"
        >
          <div
            class="dropdown-trigger"
            @click="dropdownActive = !dropdownActive"
          >
            <span class="icon is-large">
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
    </div>
    <slot name="content" />
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
  name: 'EmmentalBox',
  mixins: [clickaway],
})
export default class EmmentalBox extends Vue {
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
.emmental-box {
  border-radius: 5px;
}
.dropdown-trigger {
  cursor: pointer;
}
</style>
