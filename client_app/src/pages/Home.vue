<template lang="html">
    <main id="homepage-timeline">
        <div class="container">
            <section class="ps-page--minimalist">
                <div class="ps-page__header">
                    <p>Simple Blog</p>
                    <h3></h3>
                </div>
                <div class="ps-page__content">
                    <section class="ps-section--home-timeline">
                        <div class="ps-section__content">
                            <div v-if="postItems && postItems.length > 0" class="ps-post-items">
                                <PostSummary
                                    v-for="item in postItems"
                                    :post="item"
                                    :key="item.id"
                                />
                            </div>
                            <p v-else>No post found.</p>
                        </div>
                        <ViewAllPostsLink />
                    </section>
                </div>
            </section>
        </div>
    </main>
</template>

<script>
import ViewAllPostsLink from '../components/ViewAllPostsLink';
import { getPostBySlug } from '../services/getPostBySlug';
import PostSummary from '../components/PostSummary';

export default {
  name: 'Home',
  layout: 'layout-home-without-transparent',
  components: { PostSummary, ViewAllPostsLink },
  props: {
    collectionSlug: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      postItems: null,
      swiperOptions: {
        slidesPerView: 1,
        fadeEffect: true,
      },
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    async fetch() {
      const query = 'posts';
      console.log('Making request');
      const Posts = await getPostBySlug(query);
      if (Posts) {
        this.postItems = Posts;
      }
    },
  },
  // created() {
  //   this.$store.commit('app/toggleDrawer', false);
  // },
};
</script>

<style lang="scss" scoped></style>
