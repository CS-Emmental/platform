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
.new-box {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
  text-align: center;
  min-height: 10.625rem;
}
</style>
