module.exports = {
  root: true,

  env: {
    node: true,
  },

  extends: [
    'plugin:vue/recommended',
    '@vue/airbnb',
    '@vue/typescript/recommended',
    'plugin:vue/essential',
    '@vue/typescript',
  ],

  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    '@typescript-eslint/camelcase': ['error', { properties: 'never' }],
    'import/no-named-as-default': 0,
  },

  parserOptions: {
    parser: '@typescript-eslint/parser',
  },
};
