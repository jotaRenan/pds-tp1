import { defineConfig } from "cypress";

export default defineConfig({
  chromeWebSecurity: false,
  pageLoadTimeout: 60_00,
  defaultCommandTimeout: 60_00,
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
