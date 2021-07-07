import { createWebHistory, createRouter } from "vue-router";
import Home from "@/pages/Home.vue";
import Post from "@/pages/Post.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/posts",
    name: "AllPosts",
    component: Home,
  },
  {
    path: "/topics/:topic_id",
    name: "Post",
    component: Post,
  },
  {
    path: "/topics/:topic_id/posts/:post_id",
    name: "Post",
    component: Post,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;