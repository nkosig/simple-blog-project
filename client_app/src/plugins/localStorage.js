import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

const store = createStore({
  // ...
  plugins: [createPersistedState({
      paths: []
  })],
});

export default ({ store, isHMR }) => {
    if (isHMR) return;

    process.client &&
        window.whenReady(() => {
            createPersistedState({
                paths: []
            })(store);
        });
};
