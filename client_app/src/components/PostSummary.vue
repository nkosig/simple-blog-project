<template lang="html">
    <article class="ps-post ps-post--classic">
        <div class="ps-post__thumbnail">
            <router-link :to="`/topics/${post.topic_id}/posts/${post.id}`" class="ps-post__overlay" />
            <!-- <module-post-thumbnail-image :post="post" :wide="true" /> -->
        </div>
        <div class="ps-post__content">
            <div class="ps-post__categories">
                <router-link :to="`/topics/${post.topic_id}`" :key="post.topic_id">
                    {{ post.topic_id }}
                </router-link>
            </div>
            <h4 class="ps-post__title">
                <router-link :to="`/topics/${post.topic_id}/posts/${post.id}`">
                    {{ post.title }}
                </router-link>
            </h4>
            <div class="ps-post__meta">
                <span class="ps-post__posted">{{ dateMoment }}</span>
            </div>
            <div class="ps-post__short-desc">
                <p>{{ postShortDesc }}</p>
            </div>
            <div class="ps-post__footer">
                <router-link :to="`/topics/${post.topic_id}/posts/${post.id}`" class="ps-post__morelink effect--underline">
                    Continue Reading
                </router-link>
            </div>
        </div>
    </article>
</template>

<script>
import * as moment from 'moment';

export default {
  name: 'PostSummary',

  computed: {
    postShortDesc() {
      if (this.post && this.post.post) {
        return this.post.post.slice(0, 100) + '...';
      } else {
        return 'No description...';
      }
    },
    dateMoment() {
      return moment(this.post.created_at).fromNow();
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
