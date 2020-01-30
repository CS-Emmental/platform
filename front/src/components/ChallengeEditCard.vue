<template>
  <div
    class="card"
    tabindex="0"
    @keyup.enter="$emit('save', challengeEdit)"
    @keyup.esc="$emit('quit')"
  >
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
        <label class="label">Category</label>
        <div class="control">
          <v-select
            :options="challengeCategories"
            :value="getCategoryById(challengeEdit.category_id)"
            label="title"
            @input="setCategory"
          />
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
import { State, Getter } from 'vuex-class';

import vSelect from 'vue-select';
import EmmentalRichTextEditor from '@/components/EmmentalRichTextEditor.vue';

import { Challenge, ChallengeCategory } from '../store/challenges/types';

const namespace = 'challenges';

@Component({
  name: 'ChallengeEditCard',
  components: {
    EmmentalRichTextEditor,
    vSelect,
  },
})
export default class ChallengeEditCard extends Vue {
  @Prop({
    type: Object as () => Challenge,
    required: false,
  })
  public challenge: Challenge|undefined;

  @State('challengeCategories', { namespace })
  public challengeCategories: ChallengeCategory[]|undefined;

  @Getter('getCategoryById', { namespace })
  public getCategoryById!: CallableFunction;

  public challengeEdit: Challenge = {
    challenge_id: '',
    title: '',
    summary: '',
    description: '',
    category_id: '',
    total_points: 0,
  };

  public created() {
    if (this.challenge) {
      this.challengeEdit = { ...this.challenge };
    }
  }

  public setCategory(value: ChallengeCategory) {
    this.challengeEdit.category_id = value.category_id;
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
.card {
  border-radius: 5px;
  width: 60vw;
  margin: auto;
}
</style>
