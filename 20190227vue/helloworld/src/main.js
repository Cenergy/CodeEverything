// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import header from '@/base/header/header'
import axios from './httpConfig/axios'
import qs from 'qs'
import VueCookies from 'vue-cookies'

// 初始化样式
import '../static/style/reset.css'

// swiper样式
import 'swiper/dist/css/swiper.css'

// 全局组件
Vue.component('header-tab', header)

// Axios
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs

// 获取cookie
Vue.use(VueCookies)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
