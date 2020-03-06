<template>
  <div
    class="card"
    tabindex="0"
    @keyup.enter="$emit('save', challengesCategoryEdit)"
    @keyup.esc="$emit('quit')"
  >
    <header class="card-header">
      <p class="card-header-title">
        Edit Category
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
            v-model="challengesCategoryEdit.title"
            class="input"
            type="text"
          >
        </div>
      </div>
      <div class="field">
        <label class="label">Description</label>
        <div class="control">
          <input
            v-model="challengesCategoryEdit.description"
            class="input"
            type="text"
          >
        </div>
      </div>
      <div class="field">
        <label class="label">Icon</label>
        <div class="control">
          <input
            v-model="challengesCategoryEdit.icon"
            class="input"
            type="text"
          >
          <label class="label">Check name on fontawesome.com</label>
        </div>
      </div>
    </div>
    <footer class="card-footer">
      <a
        class="card-footer-item"
        @click="$emit('quit')"
      >Cancel</a>
      <a
        class="card-footer-item"
        @click="$emit('save', challengesCategoryEdit)"
      >Save</a>
    </footer>
  </div>
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';

import vSelect from 'vue-select';
import EmmentalRichTextEditor from '@/components/EmmentalRichTextEditor.vue';

import { ChallengeCategory } from '../store/challengeCategories/types';


@Component({
  name: 'challengesCategoryEdit',
  components: {
    EmmentalRichTextEditor,
    vSelect,
  },
})
export default class ChallengesCategoryEdit extends Vue {
  @Prop({
    type: Object as () => ChallengeCategory,
    required: false,
  })
  public challengeCategory: ChallengeCategory|undefined;

  public challengesCategoryEdit: ChallengeCategory = {
    category_id: '',
    title: '',
    title_slug: '',
    description: '',
    icon: '',
  };

  public created() {
    if (this.challengeCategory) {
      this.challengesCategoryEdit = { ...this.challengeCategory };
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
.card {
  border-radius: 5px;
  width: 60vw;
  margin: auto;
}
.card-content {
  height: 80vh;
  overflow-x: auto;
}
.field-body .field.cost-field {
  width: 10%;
  flex-grow: 0;
}
</style>
