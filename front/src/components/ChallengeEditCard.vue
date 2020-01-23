<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        Edit Challenge
      </p>
      <div class="card-header-icon">
        <button
          class="delete"
          @click="$emit('quit')"
        />
      </div>
    </header>
    <div class="card-content">
      <div class="field">
        <label class="label">Title</label>
        <div class="control">
          <input
            v-model="challengeEdit.title"
            class="input"
            type="text"
          >
        </div>
      </div>
      <div class="field">
        <label class="label">Summary</label>
        <div class="control">
          <input
            v-model="challengeEdit.summary"
            class="input"
            type="text"
          >
        </div>
      </div>
      <div class="field">
        <label class="label">Total Points</label>
        <div class="control">
          <input
            v-model="challengeEdit.total_points"
            class="input"
            type="number"
          >
        </div>
      </div>
      <div class="field">
        <label class="label">Description</label>
        <emmental-rich-text-editor
          v-if="challengeEdit"
          :content="challengeEdit.description"
          @update="(edited) => challengeEdit.description = edited"
        />
      </div>
    </div>
    <footer class="card-footer">
      <a
        class="card-footer-item"
        @click="$emit('save', challengeEdit)"
      >Save</a>
      <a
        class="card-footer-item"
        @click="$emit('quit')"
      >Cancel</a>
    </footer>
  </div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
import EmmentalRichTextEditor from '@/components/EmmentalRichTextEditor.vue';

import { Challenge } from '../store/challenges/types';

@Component({
  name: 'ChallengeEditCard',
  components: {
    EmmentalRichTextEditor,
  },
})
export default class ChallengeEditCard extends Vue {
  @Prop({
    type: Object as () => Challenge,
    required: false,
  })
  public challenge: Challenge|undefined;

  public challengeEdit: Challenge = {
    challenge_id: '',
    title: '',
    summary: '',
    description: '',
    category_id: '',
    icon: '',
    total_points: 0,
  };

  public created() {
    if (this.challenge) {
      this.challengeEdit = { ...this.challenge };
    }
  }
}
</script>

<style lang="scss" scoped>
.editor-content{
  padding: .5rem;
  border: solid 1px #dbdbdb;
  border-radius: 4px;
}
::v-deep .ProseMirror:focus {
  outline: none;
}
.buttons {
  margin-bottom: 0;
}
</style>
