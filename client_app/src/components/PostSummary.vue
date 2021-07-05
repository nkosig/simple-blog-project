<template lang="html">
    <article class="ps-post ps-post--classic">
        <div class="ps-post__thumbnail">
            <router-link :to="`/post/${post.slug}`" class="ps-post__overlay" />
            <!-- <module-post-thumbnail-image :post="post" :wide="true" /> -->
        </div>
        <div class="ps-post__content">
            <div class="ps-post__categories">
                <router-link to="/blog" v-for="item in post.categories" :key="item.id">
                    {{ item.name }}
                </router-link>
            </div>
            <h4 class="ps-post__title">
                <router-link :to="`/post/${post.id}`">
                    {{ post.title }}
                </router-link>
            </h4>
            <div class="ps-post__meta">
                <span class="ps-post__posted">Jul 12, 2020</span>
            </div>
            <div class="ps-post__short-desc">
                <p>{{ postShortDesc }}</p>
            </div>
            <div class="ps-post__footer">
                <router-link :to="`/post/${post.id}`" class="ps-post__morelink effect--underline">
                    Continue Reading
                </router-link>
            </div>
        </div>
    </article>
</template>

<script>
// import ModulePostThumbnailImage from '~/components/elements/posts/modules/ModulePostThumbnailImage';
// import ModulePostAuthorSmall from '~/components/elements/posts/modules/ModulePostAuthorSmall';
export default {
  name: 'PostSummary',
  //   components: { ModulePostAuthorSmall, ModulePostThumbnailImage },
  computed: {
    postShortDesc() {
      if (this.post && this.post.description) {
        return this.post.description.slice(0, 100) + '...';
      } else {
        return 'No description found...';
      }
    },
  },
  props: {
    post: {
      //   type: Object,
      default: {},
    },
  },
};
</script>

<style lang="scss" scoped></style>
