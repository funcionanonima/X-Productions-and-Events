import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Members from '../views/Members.vue'
import Event from '../views/Event.vue'

Vue.use(VueRouter)

const routes = [
  {
    // events
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    // events_details
    path: '/event/:id',
    name: 'Event',
    component: Event,
    props: true
  },
  {
    path: '/members',
    name: 'Members',
    component: Members
  },
  // {
  //   path: '/members',
  //   name: 'Members',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/Members.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
