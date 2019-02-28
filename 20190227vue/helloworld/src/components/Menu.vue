<template>
  <div class="menu">
    <header-tab></header-tab>
    <div class="item">
      <div class="menu-item">
        <!-- <img src="@/assets/btn1.png" alt="" class="item" @click="paperHandle"> -->
        <router-link to="Paper">
          <img src="@/assets/btn1.png" alt="" class="item">
        </router-link>
        <div class="file">
          <img src="@/assets/btn3.png" alt="" class="item" :class="{'opacity':mouseOpacity}">
          <input type="file" ref="file" class="upload" @change="elecHandle" @mouseenter="mouseOpacity=true" @mouseleave="mouseOpacity=false">
        </div>
      </div>
      <div class="menu-item">
        <img src="@/assets/btn4.png" alt="" class="item" @click="historyHandle">
        <img src="@/assets/btn2.png" alt="" class="item" @click="moreHandle">
      </div>
    </div>
    <div class="dialog" v-show="dialogShow" @click="(!messageShow) && dialogHandle()">
      <div class="paper" v-if="paperShow" @click.stop>
        <p class="text">{{dialogMessage}}</p>
        <div class="btn" @click="paperConfirm">确认</div>
        <div class="btn" @click="(!messageShow) && dialogHandle()">取消</div>
      </div>
      <div class="message" v-if="messageShow">{{message}}</div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      dialogShow: false,
      paperShow: false,
      messageShow: false,
      message: '',
      dialogMessage: '',
      precheckNum: 0,
      mouseOpacity: false,
      isTables: false
    }
  },
  methods: {
    // paperHandle () {
    //   this.messageShow = false
    //   this.dialogShow = true
    //   this.dialogMessage = '请将纸质版文档放入指定位置，然后点击确认放纸进行下一步'
    //   this.paperShow = true
    // },
    paperConfirm () {
      this.isTables ? this.tables() : this.precheck(this.paper)
    },
    paper () {
      this.paperShow = false
      this.message = '获取纸张信息，请稍候...'
      this.messageShow = true
      this.$axios({
        method: 'get',
        url: '/stamp/paper/'
      }).then(res => {
        console.log(res)
        if (res.status === 200 && res.data.code === 200) {
          let data = JSON.stringify(res.data.data)
          this.$router.push({
            path: 'preview',
            query: {
              data: data
            }
          })
        } else if (res.status === 200 && res.data.code === 294) {
          this.messageShow = false
          this.dialogMessage = res.data.message
          this.isTables = this.paperShow = true
        } else {
          this.message = res.data.message
          setTimeout(() => {
            this.dialogShow = this.messageShow = false
          }, 3000)
        }
      }).catch(err => {
        // 错误提示
        this.message = '服务器错误，请稍后重试'
        setTimeout(() => {
          this.dialogShow = this.messageShow = false
        }, 3000)
        console.log(err)
      })
    },
    tables () {
      this.paperShow = false
      this.message = '获取纸张信息，请稍候...'
      this.messageShow = true
      this.$axios({
        method: 'get',
        url: '/stamp/tables/'
      }).then(res => {
        console.log(res)
        if (res.status === 200 && res.data.code === 200) {
          res.data.data.Img_contract = res.data.data.Img_draw = res.data.data.Img
          let data = JSON.stringify(res.data.data)
          this.$router.push({
            path: 'preview',
            query: {
              data: data
            }
          })
        } else {
          this.message = res.data.message
          setTimeout(() => {
            this.dialogShow = this.messageShow = this.isTables = false
          }, 3000)
        }
      }).catch(err => {
        // 错误提示
        this.message = '服务器错误，请稍后重试'
        setTimeout(() => {
          this.dialogShow = this.messageShow = false
        }, 3000)
        console.log(err)
      })
    },
    elecHandle (upload) {
      this.paperShow = false
      this.message = '上传中，请稍候...'
      this.dialogShow = this.messageShow = true
      let formData = new FormData()
      formData.append('file', upload.target.files[0])
      // 文件上传
      this.$axios.post('/stamp/electron/', formData)
        .then(res => {
          console.log(res)
          if (res.status === 200 && res.data.code === 200) {
            this.precheck(this.paper)
          } else {
            this.message = res.data.message
            setTimeout(() => {
              this.dialogShow = this.messageShow = false
            }, 7000)
          }
        })
        .catch(err => {
          // 错误提示
          this.message = '服务器错误，请稍后重试'
          setTimeout(() => {
            this.dialogShow = this.messageShow = false
          }, 3000)
          console.log(err)
        })
    },
    precheck (obj) {
      this.paperShow = false
      this.message = '入纸中，请稍候...'
      this.messageShow = true
      this.$axios({
        method: 'get',
        url: '/stamp/precheck/'
      }).then(res => {
        console.log(res)
        if (res.status === 200 && res.data.code === 200) {
          obj()
        } else if (this.precheckNum > 5) {
          this.message = '入纸失败，请稍后重试'
          this.precheckNum = 0
          setTimeout(() => {
            this.dialogShow = this.messageShow = false
          }, 7000)
        } else {
          this.message = res.data.message
          this.precheckNum++
          setTimeout(() => {
            this.precheck(obj)
          }, 3000)
        }
      }).catch(err => {
        // 错误提示
        this.message = '服务器错误，请稍后重试'
        setTimeout(() => {
          this.dialogShow = this.messageShow = false
        }, 3000)
        console.log(err)
      })
    },
    historyHandle () {
      this.$router.push('/history')
    },
    moreHandle () {
      this.$router.push('/Control')
    },
    dialogHandle () {
      if (this.isTables) {
        this.paper()
      } else {
        this.dialogShow = this.paperShow = this.messageShow = this.isTables = false
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .menu
    position relative
    width 100%
    height 100%
    background url(../assets/bg.png) no-repeat center center
    background-size 100% 100%
    display flex
    align-items center
    flex-direction column
    .item
      display flex
      flex-direction column
      align-items center
      justify-content center
      flex 1
      .menu-item
        display flex
        align-items center
        justify-content center
        .item
          width 233px
          height 233px
          margin 0 30px 30px 0
          cursor pointer
          &.opacity
            opacity .7
        .item:hover
          opacity .7
        .file
          position relative
          .upload
            position absolute
            top 0
            left 0
            width 233px
            height 233px
            margin 0 30px 30px 0
            opacity 0
            cursor pointer
    .dialog
      position absolute
      top 0
      left 0
      width 100%
      height 100%
      background-color rgba(0, 0, 0, .79)
      .paper
        position absolute
        top 50%
        left 50%
        transform translate(-50%, -50%)
        width 370px
        height 305px
        background url(../assets/paperBorder.png) no-repeat center center
        background-size 100% 100%
        .text
          margin-top 70px
          padding 0 50px
          font-size 24px
          font-weight bold
          color rgb(253,252,252)
          line-height 40px
          text-align center
        .btn
          float left;
          width 50%;
          margin 15px auto
          height 82px
          cursor pointer
          background url(../assets/paperbtn.png) no-repeat center center
          background-size 100% 100%
          font-size 18px
          font-weight bold
          color rgb(123,123,123)
          line-height 80px
          text-align center
      .message
        position absolute
        top 50%
        left 50%
        transform translate(-50%, -50%)
        width 442px
        height 140px
        background url(../assets/menuMs.png) no-repeat
        background-size 100% 100%
        font-size 36px
        font-weight 400
        color rgba(255,255,255,1)
        line-height 140px
        text-align center
</style>
