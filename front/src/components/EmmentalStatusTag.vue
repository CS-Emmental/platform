<template>
  <span
    class="tag is-rounded is-medium is-light"
    :class="style"
  >
    {{ text }}
  </span>
</template>

<script  lang="ts">
import {
  Prop,
  Component,
  Vue,
} from 'vue-property-decorator';

@Component({
  name: 'EmmentalStatusTag',
})
export default class EmmentalStatusTag extends Vue {
  // Challenge

  @Prop({
    type: String,
    required: true,
  })
  public status!: string;

  public text_dict: {[id: string]: string} = {
    ongoing: 'Ongoing',
    stopped: 'Stopped',
    finished: 'Finished',
  };

  public style_dict: {[id: string]: string} = {
    ongoing: 'is-primary',
    stopped: 'is-danger',
    finished: 'is-success',
  };

  get text(): string {
    return this.text_dict[this.status] || '';
  }

  get style(): string {
    return this.style_dict[this.status] || '';
  }
}
</script>

<style lang="scss" scoped>
.tag {
  border: 1px solid;
}
</style>
