<template>
  <div class="login">
    <header-tab v-if="isShow"></header-tab>
    <img src="@/assets/title.png" alt="" class="title">
    <div class="face">
      <div class="content">
        <video ref="video" id="video" autoplay></video>
        <canvas ref="canvas" id="canvas" width="640" height="480"></canvas>
      </div>
      <p class="message" v-show="messageShow">{{message}}</p>
    </div>
    <input class="name" type="text" placeholder="请填写用户名" v-model="inputValue" v-show="isShow">
    <div class="begin" :class="{'bottom':!isShow}" @click="begin">
      <p class="text">开始识别</p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: '',
      messageShow: false,
      isShow: false,
      inputValue: '',
      stream: null,
      faceTime: 0
    }
  },
  methods: {
    getUserMediaToPhoto (constraints, success, error) {
      if (navigator.mediaDevices.getUserMedia) {
        // 最新标准API
        navigator.mediaDevices.getUserMedia(constraints).then(success).catch(error)
      } else if (navigator.webkitGetUserMedia) {
        // webkit核心浏览器
        navigator.webkitGetUserMedia(constraints, success, error)
      } else if (navigator.mozGetUserMedia) {
        // firefox浏览器
        navigator.mozGetUserMedia(constraints, success, error)
      } else if (navigator.getUserMedia) {
        // 旧版API
        navigator.getUserMedia(constraints, success, error)
      }
    },
    success (stream) {
      this.stream = stream
      // 将视频流转化为video的源
      const video = this.$refs.video
      try {
        video.srcObject = stream
      } catch (error) {
        let CompatibleURL = window.URL || window.webkitURL
        video.src = CompatibleURL.createObjectURL(stream)
      }
      // 播放视频
      this.$refs.video.play()
    },
    error (error) {
      console.log('访问用户媒体失败：', error.name, error.message)
    },
    getPhtot () {
      if (navigator.mediaDevices.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.getUserMedia) {
        this.getUserMediaToPhoto({ video: { width: 640, height: 640 } }, this.success, this.error)
      }
    },
    getBase64 () {
      let video = this.$refs.video
      let canvas = this.$refs.canvas
      canvas.getContext('2d').drawImage(video, 0, 0, 640, 480)
      let base64 = canvas.toDataURL('image/png')
      return base64
    },
    begin () {
      this.message = '正在识别,请稍后...'
      this.messageShow = true
      if (this.isShow) {
        if (this.inputValue === '') {
          this.message = '请您先填写用户名'
          return
        }
        let base64 = this.getBase64()
        // console.log(base64)
        this.$axios({
          method: 'post',
          url: '/user/register/',
          data: this.$qs.stringify({
            face_str: base64,
            face_name: this.inputValue
          })
        }).then(res => {
          console.log(res)
          if (res.status === 200 && res.data.code === 200) {
            this.$router.push('/userManage')
          } else if (this.faceTime < 10) {
            this.faceTime++
            // this.message = '请您面部正对摄像头'
            this.message = res.data.message
            setTimeout(() => {
              this.begin()
            }, 1500)
          } else {
            // this.message = '注册失败,请重新注册'
            this.message = res.data.message
            this.faceTime = 0
          }
        })
      } else {
        let base64 = this.getBase64()
        // console.log(base64)
        this.$axios({
          method: 'post',
          url: '/user/login/',
          data: this.$qs.stringify({
            face_str: base64
          })
        }).then(res => {
          console.log(res)
          if (res.status === 200 && res.data.code === 200) {
            this.$cookies.set('Authorization', res.data.Authorization)
            this.$cookies.set('username', res.data.username)
            this.$router.push('/menu')
          } else if (this.faceTime < 10) {
            this.faceTime++
            this.message = res.data.message
            setTimeout(() => {
              this.begin()
            }, 1500)
          } else {
            // this.message = '验证失败,请重新验证'
            this.message = res.data.message
            this.faceTime = 0
          }
        })
      }
    },
    isLogin () {
      this.$route.query.form ? this.isShow = true : this.isShow = false
    }
  },
  mounted () {
    this.getPhtot()
    this.isLogin()
  },
  beforeRouteLeave (to, from, next) {
    this.stream.getTracks()[0].stop()
    next()
  }
}
</script>

<style lang="stylus" scoped>
  .login
    position relative
    width 100%
    height 100%
    background url(../assets/bg.png) no-repeat
    background-size 100% 100%
    .title
      position absolute
      top 0
      left 50%
      transform translateX(-50%)
      width 207px
    .face
      position absolute
      top 177px
      left 50%
      transform translateX(-50%)
      width 440px
      height 425px
      background url(../assets/faceBorder.png) no-repeat
      background-size 100% 100%
      .content
        position absolute
        top 50%
        left 50%
        transform translate(-50%, -50%)
        width 70%
        height 75%
        border-radius 50%
        overflow hidden
        #video
          position absolute
          top 50%
          left 50%
          transform translate(-50%,-50%)
          height 100%
        #canvas
          position absolute
          top 0
          left 0
          z-index -10000
          visibility hidden
      .message
        box-sizing border-box
        position absolute
        top 50%
        left 50%
        transform translate(-50%, -50%)
        width 262px
        height 130px
        padding 20px 40px
        font-size 36px
        font-weight bold
        color rgba(253,252,252,1)
        line-height 50px
        text-align center
        background url(../assets/messageBorder.png) no-repeat
        background-size 100% 100%
        background-color rgba(0, 0, 0, .5)
    .name
      box-sizing border-box
      position absolute
      left 50%
      bottom 100px
      transform translateX(-50%)
      padding 0 25px
      width 310px
      height 60px
      font-size 24px
      font-weight 400
      color rgba(255,255,255,1)
      line-height 60px
      text-align center
      background url(../assets/faceName.png) no-repeat
      background-size 100% 100%
    .begin
      position absolute
      left 50%
      bottom 15px
      transform translateX(-50%)
      width 246px
      height 67px
      cursor pointer
      background url(../assets/beginBorder.png) no-repeat
      background-size 100% 100%
      .text
        font-size 36px
        font-weight bold
        color rgba(253,252,252,1)
        text-align center
        line-height 67px
      &.bottom
        bottom 65px
</style>
