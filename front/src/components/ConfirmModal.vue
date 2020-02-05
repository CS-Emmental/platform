<template>
  <emmental-modal :is-active="toggle">
    <div
      class="card confirm-card"
      tabindex="0"
      @keyup.enter="$emit('confirm')"
      @keyup.esc="$emit('exit')"
    >
      <header class="card-header">
        <p class="card-header-title">
          {{ title }}
        </p>
        <div class="card-header-icon">
          <button
            class="delete"
            @click="$emit('exit')"
          />
        </div>
      </header>
      <div class="card-content">
        <p>
          {{ message }}
        </p>
      </div>
      <footer class="card-footer">
        <a
          class="card-footer-item"
          @click="$emit('exit')"
        >Cancel</a>
        <a
          class="card-footer-item"
          @click="$emit('confirm')"
        >Confirm</a>
      </footer>
    </div>
  </emmental-modal>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

import EmmentalModal from '@/components/EmmentalModal.vue';

@Component({
  name: 'ConfirmModal',
  components: {
    EmmentalModal,
  },
})
export default class ConfirmModal extends Vue {
  // Challenge

  @Prop({
    type: Boolean,
    required: true,
  })
  public toggle!: boolean;

  @Prop({
    type: String,
    required: true,
  })
  public title!: string;

  @Prop({
    type: String,
    required: true,
  })
  public message!: string;
}
</script>

<style lang="scss" scoped>
.confirm-card {
  width: 30vw;
  margin: auto;
  border-radius: 5px;
}
</style>
