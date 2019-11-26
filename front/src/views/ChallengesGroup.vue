<template>
  <div class="challenges-group">
    <h1>Challenges Group</h1>
    <p>{{group}}</p>
  </div>
</template>

<script  lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

@Component
export default class ChallengesGroup extends Vue {
  public name: string = 'ChallengesGroup';
  @Prop()
  public group: string;
}
</script>
