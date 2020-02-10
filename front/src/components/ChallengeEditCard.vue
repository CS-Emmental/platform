<template>
  <div
    class="card"
    tabindex="0"
    @keyup.enter="onSave"
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
            :class="{'is-danger': !challengeEdit.title}"
            class="input"
            type="text"
          >
        </div>
        <p
          v-if="!challengeEdit.title"
          class="help is-danger"
        >
          Empty title
        </p>
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
      <label class="label">Flags</label>
      <div
        v-for="(flag, index) in challengeEdit.flags"
        :key="`flag-${index}`"
        class="field is-grouped"
      >
        <p class="control has-icons-left">
          <input
            class="input"
            type="number"
            placeholder="Cost"
            :class="{'is-danger': flagRewardSum !== 1}"
            :value="flag.reward*challengeEdit.total_points"
            @input="flag.reward = $event.target.value / challengeEdit.total_points"
          >
          <span class="icon is-small is-left">
            <i class="fas fa-dollar-sign" />
          </span>
        </p>
        <p class="control is-expanded">
          <input
            v-model="flag.value"
            class="input"
            type="text"
            placeholder="Secret"
          >
        </p>
        <p class="control is-expanded">
          <input
            v-model="flag.text"
            class="input"
            type="text"
            placeholder="Text"
          >
        </p>
        <p class="control">
          <a
            class="button is-light is-rounded"
            @click="challengeEdit.flags.splice(index, 1)"
          >
            <i class="fas fa-times" />
          </a>
        </p>
      </div>
      <div class="field">
        <p class="control">
          <a
            class="button is-light is-rounded"
            @click="onNewFlag"
          >
            <i class="fas fa-plus plus-icon" />Add flag
          </a>
        </p>
        <p
          v-if="flagRewardSum !== 1"
          class="help is-danger"
        >
          Total flag points don't match challenge points
        </p>
      </div>
      <div class="field">
        <label class="label">Description</label>
        <emmental-rich-text-editor
          v-if="challengeEdit"
          :content="challengeEdit.description"
          @update="(edited) => challengeEdit.description = edited"
        />
      </div>
      <label class="label">Hints</label>
      <div
        v-for="(hint, index) in challengeEdit.hints"
        :key="index"
        class="field is-grouped"
      >
        <p class="control has-icons-left">
          <input
            class="input"
            type="number"
            placeholder="Cost"
            :value="hint.cost*challengeEdit.total_points"
            @input="hint.cost = $event.target.value / challengeEdit.total_points"
          >
          <span class="icon is-small is-left">
            <i class="fas fa-dollar-sign" />
          </span>
        </p>
        <p class="control is-expanded">
          <input
            v-model="hint.text"
            class="input"
            type="text"
            placeholder="Hint"
          >
        </p>
        <p class="control">
          <a
            class="button is-light is-rounded"
            @click="challengeEdit.hints.splice(index, 1)"
          >
            <i class="fas fa-times" />
          </a>
        </p>
      </div>
      <div class="field">
        <p class="control">
          <a
            class="button is-light is-rounded"
            @click="onNewHint"
          >
            <i class="fas fa-plus plus-icon" />Add hint
          </a>
        </p>
      </div>
    </div>
    <footer class="card-footer">
      <a
        class="card-footer-item"
        @click="$emit('quit')"
      >Cancel</a>
      <a
        class="card-footer-item"
        @click="onSave"
      >Save</a>
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
    flags: [],
    hints: [],
  };

  public created() {
    if (this.challenge) {
      this.challengeEdit = { ...this.challenge };
      if (this.challengeEdit.hints) {
        this.challengeEdit.hints = [...this.challenge.hints];
      }
      if (this.challengeEdit.flags) {
        this.challengeEdit.flags = [...this.challenge.flags];
      }
    }
  }

  public onNewHint() {
    if (!this.challengeEdit.hints) {
      this.challengeEdit.hints = [];
    }
    this.challengeEdit.hints.push({ cost: 0, text: '' });
  }

  public onNewFlag() {
    if (!this.challengeEdit.flags) {
      this.challengeEdit.flags = [];
    }
    this.challengeEdit.flags.push({ reward: 0, value: '', text: '' });
  }

  get flagRewardSum() {
    return this.challengeEdit.flags.map(flag => flag.reward)
      .reduce((pv, vc) => pv + vc, 0);
  }

  get formIsValid() {
    return this.challengeEdit.title && this.flagRewardSum === 1;
  }

  public setCategory(value: ChallengeCategory) {
    this.challengeEdit.category_id = value.category_id;
  }

  public onSave() {
    if (this.formIsValid) {
      this.$emit('save', this.challengeEdit);
    } else {
      this.$toasted.show('Challenge form is invalid');
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
.plus-icon {
  margin-right: .2rem;
}
</style>
