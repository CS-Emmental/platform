<template>
  <a
    class="box new-box"
    @click="$emit(`new-${collection}`)"
  >
    <div>
      <i class="fas fa-plus-circle" />
      Create new {{ collection }}
    </div>
  </a>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

interface Action {
  text: string;
  signal: string;
}

@Component({
  name: 'NewBox',
})
export default class NewBox extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public collection!: string;
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
