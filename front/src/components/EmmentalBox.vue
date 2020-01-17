<template>
  <div class="box emmental-box">
    <div class="box-header level">
      <div class="level-left">
        <h1 class="title is- level-item">
          <i :class="icon" />
          {{ title }}
        </h1>
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
    <p class="subtitle is-4">
      {{ subtitle }}
    </p>
    <p>
      {{ content }}
    </p>
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
    type: String,
    required: true,
  })
  public title!: string;

  @Prop({
    type: String,
    required: false,
  })
  public subtitle: string|undefined;

  @Prop({
    type: String,
    required: false,
  })
  public icon: string|undefined;

  @Prop({
    type: String,
    required: false,
  })
  public content: string|undefined;

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
.card-header-title {
  margin-bottom: 0;
}
.emmental-box:not(:last-child) {
  margin-bottom: 0;
}
.emmental-box {
  border-radius: 5px;
}
.title-icon {
  margin-right: .5rem;
}
.dropdown-trigger {
  cursor: pointer;
}
</style>
