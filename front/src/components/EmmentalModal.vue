<template>
  <div
    class="modal"
    :class="{'is-active': isActive}"
  >
    <div class="modal-background" />
    <div class="modal-content">
      <slot />
    </div>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

@Component({
  name: 'EmmentalModal',
})
export default class EmmentalModal extends Vue {
  @Prop({
    type: Boolean,
    required: true,
  })
  public isActive!: boolean;
}
</script>

<style lang="scss" scoped>
.modal-content {
  width: 100vw;
}
</style>
