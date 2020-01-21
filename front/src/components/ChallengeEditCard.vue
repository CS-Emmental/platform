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
        <div
          v-if="editor"
          class="control"
        >
          <editor-menu-bar
            v-slot="{ commands, isActive }"
            :editor="editor"
          >
            <p class="buttons">
              <button
                class="button"
                :class="{ 'is-active': isActive.bold() }"
                @click="commands.bold"
              >
                <span class="icon is-small">
                  <i class="fas fa-bold" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.italic() }"
                @click="commands.italic"
              >
                <span class="icon is-small">
                  <i class="fas fa-italic" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.underline() }"
                @click="commands.underline"
              >
                <span class="icon is-small">
                  <i class="fas fa-underline" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.strike() }"
                @click="commands.strike"
              >
                <span class="icon is-small">
                  <i class="fas fa-strikethrough" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.heading({ level: 1 }) }"
                @click="commands.heading({ level: 1 })"
              >
                <span class="icon is-small">
                  H1
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.heading({ level: 2 }) }"
                @click="commands.heading({ level: 2 })"
              >
                <span class="icon is-small">
                  H2
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.heading({ level: 3 }) }"
                @click="commands.heading({ level: 3 })"
              >
                <span class="icon is-small">
                  H3
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.paragraph() }"
                @click="commands.paragraph"
              >
                <span class="icon is-small">
                  <i class="fas fa-paragraph" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.bullet_list() }"
                @click="commands.bullet_list"
              >
                <span class="icon is-small">
                  <i class="fas fa-list-ul" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.ordered_list() }"
                @click="commands.ordered_list"
              >
                <span class="icon is-small">
                  <i class="fas fa-list-ol" />
                </span>
              </button>
              <button
                class="button"
                :class="{ 'is-active': isActive.code() }"
                @click="commands.code"
              >
                <span class="icon is-small">
                  <i class="fas fa-code" />
                </span>
              </button>
            </p>
          </editor-menu-bar>
          <editor-content
            class="editor-content content"
            :editor="editor"
          />
        </div>
      </div>
    </div>
    <footer class="card-footer">
      <a
        class="card-footer-item"
        @click="save"
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
import { Action } from 'vuex-class';
import { Editor, EditorContent, EditorMenuBar } from 'tiptap';
import {
  Heading,
  OrderedList,
  BulletList,
  ListItem,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History,
} from 'tiptap-extensions';

import { Challenge } from '../store/challenges/types';

const namespace = 'challenges';

@Component({
  name: 'ChallengeEditCard',
  components: {
    EditorMenuBar,
    EditorContent,
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

  @Action('postChallenge', { namespace })
  public postChallenge!: CallableFunction;

  public editor = new Editor({
    extensions: [
      new Heading({ levels: [1, 2, 3] }),
      new BulletList(),
      new OrderedList(),
      new ListItem(),
      new Bold(),
      new Code(),
      new Italic(),
      new Link(),
      new Strike(),
      new Underline(),
      new History(),
    ],
  });

  public created() {
    if (this.challenge) {
      this.challengeEdit = { ...this.challenge };
      this.editor = new Editor({
        extensions: [
          new Heading({ levels: [1, 2, 3] }),
          new BulletList(),
          new OrderedList(),
          new ListItem(),
          new Bold(),
          new Code(),
          new Italic(),
          new Link(),
          new Strike(),
          new Underline(),
          new History(),
        ],
        content: this.challengeEdit.description,
        onUpdate: ({ getHTML }) => {
          this.challengeEdit.description = getHTML();
        },
      });
    }
  }

  public beforeDestroy() {
    this.editor.destroy();
  }

  public save() {
    this.postChallenge(this.challengeEdit);
    this.$emit('quit');
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
