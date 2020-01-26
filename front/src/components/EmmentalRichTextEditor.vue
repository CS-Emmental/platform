<template>
  <div
    class="control"
    @keyup.enter.stop=""
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
</template>

<script lang="ts">
import { Prop, Component, Vue } from 'vue-property-decorator';
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

@Component({
  name: 'EmmentalRichTextEditor',
  components: {
    EditorMenuBar,
    EditorContent,
  },
})
export default class EmmentalRichTextEditor extends Vue {
  @Prop({
    type: String,
    required: true,
  })
  public content!: string;

  public editor = new Editor();

  public created() {
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
      content: this.content,
      onUpdate: ({ getHTML }: { getHTML: CallableFunction }) => {
        this.$emit('update', getHTML());
      },
    });
  }

  public beforeDestroy() {
    this.editor.destroy();
  }
}
</script>

<style lang="scss" scoped>
.editor-content{
  padding: .5rem;
  border: solid 1px #dbdbdb;
  border-radius: 4px;
  height: 30vh;
  overflow-y: auto;
}
::v-deep .ProseMirror:focus {
  outline: none;
}
.buttons {
  margin-bottom: 0;
}
</style>
