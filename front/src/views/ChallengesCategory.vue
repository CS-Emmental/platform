<template>
  <div class="challenges-category">
    <h1>Challenges Category</h1>
    <p>{{group}} > {{category}}</p>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

@Component
export default class ChallengesCategory extends Vue {
  public name: string = 'ChallengesCategory';
  @Prop()
  public category: string;
  @Prop()
  public group: string;
}
</script>
