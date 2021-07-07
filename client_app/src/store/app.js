export const state = () => ({
    isDrawer: false,
    isSearch: false
});

export const mutations = {
    toggleDrawer(state, payload) {
        state.isDrawer = payload;
    },

    toggleSearch(state, payload) {
        state.isSearch = payload;
    }
};
