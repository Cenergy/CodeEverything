import Vue from 'vue'
import axios from 'axios'

axios.defaults.withCredentials = false

// 请求拦截器
axios.interceptors.request.use(
  config => {
    if (Vue.cookies.get('Authorization')) {
      config.headers.Authorization = Vue.cookies.get('Authorization')
    }
    if (Vue.cookies.get('csrftoken')) {
      config.headers['X-Requested-With'] = 'XMLHttpRequest'
      config.headers['X-CSRFToken'] = Vue.cookies.get('csrftoken')
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

// 响应拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 返回 401 清除token信息
          Vue.cookies.remove('Authorization')
          Vue.cookies.remove('headername')
          // 跳转到登录页面
          Vue.router.replace({
            path: '/face'
          })
      }
    }
    // 返回错误信息
    return Promise.reject(error.response.data)
  }
)

export default axios
