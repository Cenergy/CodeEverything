<template>
    <div class="paper">
        <header-tab backTo='Menu'></header-tab>
         <div class="item">
            <div class="menu-item">
                <img src="@/assets/btn5.png" alt="" class="item" @click="paperHandle">
                <img src="@/assets/btn6.png" alt="" class="item" @click="tableHandle">
            </div>
        </div>
        <div class="dialog" v-show="dialogShow" @click="(!messageShow) && dialogHandle()">
            <div class="paperShow" v-if="paperShow" @click.stop>
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
      isTables: false,
      isPaper: false
    }
  },
  methods: {
    paperHandle () {
      this.messageShow = false
      this.isPaper = true
      this.dialogShow = true
      this.dialogMessage = '请将纸质版文档放入指定位置，然后点击确认放纸进行下一步'
      this.paperShow = true
    },
    tableHandle () {
      this.messageShow = false
      this.isPaper = false
      this.dialogShow = true
      this.dialogMessage = '请将纸质版文档放入指定位置，然后点击确认放纸进行下一步'
      this.paperShow = true
    },
    paperConfirm () {
      this.isTables ? this.tables() : this.isPaper ? this.precheck(this.paper) : this.precheck(this.tables)
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
  .paper
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
        .item:hover
          opacity .7
    .dialog
      position absolute
      top 0
      left 0
      width 100%
      height 100%
      background-color rgba(0, 0, 0, .79)
      .paperShow
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
          display inline-block
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
