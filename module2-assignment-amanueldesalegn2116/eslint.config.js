// ESLint 9 flat config — checks vanilla JS (Days 16-22 content)
export default [
  {
    ignores: ["node_modules/**", "dist/**", ".github/**"]
  },
  {
    files: ["tests/**/*.js"],
    languageOptions: {
      globals: {
        test: "readonly",
        expect: "readonly",
        describe: "readonly",
        it: "readonly",
        beforeEach: "readonly",
        afterEach: "readonly",
        beforeAll: "readonly",
        afterAll: "readonly"
      }
    }
  },
  {
    files: ["**/*.js"],
    ignores: ["tests/**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: {
        window: "readonly",
        document: "readonly",
        console: "readonly",
        fetch: "readonly",
        localStorage: "readonly",
        sessionStorage: "readonly",
        setTimeout: "readonly",
        module: "readonly",
        require: "readonly"
      }
    },
    rules: {
      "no-unused-vars": "warn",
      "no-undef": "error",
      "no-console": "off",
      "eqeqeq": "warn",
      "no-var": "warn",
      "prefer-const": "warn"
    }
  }
];
