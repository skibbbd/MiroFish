import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MainView from '../views/MainView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/process/:projectId',
    name: 'Process',
    component: MainView,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
