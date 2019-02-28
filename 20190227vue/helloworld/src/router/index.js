import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

const router = new Router({
  routes: [{
    path: '/',
    name: 'Index',
    component: resolve => require(['@/components/Index'], resolve)
  }, {
    path: '/face',
    name: 'Face',
    component: resolve => require(['@/components/Face'], resolve)
  }, {
    path: '/menu',
    name: 'menu',
    component: resolve => require(['@/components/Menu'], resolve)
  }, {
    path: '/userManage',
    name: 'UserManage',
    component: resolve => require(['@/components/UserManage'], resolve)
  }, {
    path: '/control',
    name: 'control',
    component: resolve => require(['@/components/stampcontrol/Control'], resolve)
  }, {
    path: '/stamp',
    name: 'stamp',
    component: resolve => require(['@/components/stampcontrol/Stamp'], resolve)
  }, {
    path: '/preview',
    name: 'preview',
    component: resolve => require(['@/components/Preview'], resolve)
  }, {
    path: '/history',
    name: 'history',
    component: resolve => require(['@/components/History'], resolve)
  }, {
    path: '/paper',
    name: 'paper',
    component: resolve => require(['@/components/Paper'], resolve)
  }]
})

router.beforeEach((to, from, next) => {
  if (to.path === '/' || to.path === '/face') {
    next()
  } else {
    let Authorization = Vue.cookies.get('Authorization')
    if (Authorization === null || Authorization === '') {
      Vue.cookies.remove('Authorization')
      Vue.cookies.remove('username')
      next('/face')
    } else {
      next()
    }
  }
})

export default router
