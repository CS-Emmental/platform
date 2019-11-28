<template>
<emmental-box :box-props="boxProps"/>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import EmmentalBox from '@/components/EmmentalBox.vue';

interface ChallengeGroupInterface {
  title: string;
  kebab: string;
  id: string;
  icon: string;
  description: string;
  challengesCount: number;
}

@Component({
  name: 'ChallengeGroupBox',
  components: {
    EmmentalBox,
  },
})
export default class EmmentalGroupBox extends Vue {
  @Prop({
    type: Object as () => ChallengeGroupInterface,
    required: true,
  })
  public group;

  private boxProps = {
    title: this.group.title,
    link: `/challenges/${this.group.kebab}`,
    icon: this.group.icon,
    subtitle: `${this.group.challengesCount} Challenges`,
    content: this.group.description,
  };
}
</script>

<style lang="scss" scoped>
</style>