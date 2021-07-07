<template lang="html">
    <main class="ps-page ps-page--single-post">
        <template v-if="post !== null">
            <article-detail-with-hero :post="post" />
        </template>
        <p v-else>not found.</p>
    </main>
</template>

<script>
// import LayoutDefault from '~/layouts/layout-home-default';
import { getPostById } from '../services/getPostBySlug';
// import ArticleDetailWithHero from '~/components/elements/posts/ArticleDetailWithHero';
export default {
  //   components: { ArticleDetailWithHero, LayoutDefault },
  computed: {
    topic_id() {
      return this.$route.params.topic_id;
    },
    post_id() {
      return this.$route.params.post_id;
    },
  },
  data() {
    return {
      post: null,
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    async fetch() {
      console.log('topic', this.topic_id, 'post', this.post_id);
      const Post = await getPostById(this.topic_id, this.post_id);
      if (Post) {
        this.post = Post;
      }
    },
  },
  created() {
    this.$store.commit('app/toggleDrawer', false);
  },
};
</script>

<style lang="scss" scope></style>
