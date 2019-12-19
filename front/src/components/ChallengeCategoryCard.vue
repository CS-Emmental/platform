<template>
  <emmental-card :card-props="cardProps" />
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import EmmentalCard from '@/components/EmmentalCard.vue';

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
    EmmentalCard,
  },
})
export default class ChallengeCategoryCard extends Vue {
  @Prop({
    type: Object as () => ChallengeCategoryInterface,
    required: true,
  })
  public category;

  private cardProps = {
    title: this.category.title,
    link: `/challenges/${this.category.kebab}`,
    icon: this.category.icon,
    subtitle: `${this.category.challengesCount ? this.category.challengesCount : 0} Challenges`,
    content: this.category.description,
  };
}
</script>

<style lang="scss" scoped>
</style>
