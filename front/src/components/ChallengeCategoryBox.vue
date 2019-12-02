<template>
<emmental-box :box-props="boxProps"/>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import EmmentalBox from '@/components/EmmentalBox.vue';

interface ChallengeCategoryInterface {
  title: string;
  kebab: string;
  id: string;
  icon: string;
  description: string;
  challengesCount: number;
}

@Component({
  name: 'ChallengeCategoryBox',
  components: {
    EmmentalBox,
  },
})
export default class ChallengeCategoryBox extends Vue {
  @Prop({
    type: Object as () => ChallengeCategoryInterface,
    required: true,
  })
  public category;

  private boxProps = {
    title: this.category.title,
    link: `/challenges/${this.category.kebab}`,
    icon: this.category.icon,
    subtitle: `${this.category.challengesCount} Challenges`,
    content: this.category.description,
  };
}
</script>

<style lang="scss" scoped>
</style>