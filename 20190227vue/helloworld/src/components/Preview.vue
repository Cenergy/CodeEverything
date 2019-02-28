<template>
  <div class="preview">
    <div class="cancal" @click="handleCancal">取消盖章</div>
    <div class="confirm" @click="handleConfirm">确定盖章</div>
    <div class="remove" @click="handleRemove">移除印章</div>
    <div class="change" @click="handleChange">更换印章</div>
    <p class="pv-title">请选择盖章位置</p>
    <div class="doc" @mouseenter="handleMouseenter" @mouseleave="handleMouseleave">
      <img :src="imgSrc" alt="" class="imgSrc">
      <img src="@/assets/pvStamp.png" :style="{top:stampTop,left:stampLeft}" alt="" class="stamp" v-show="stampShow">
      <div class="move" @mousemove="canMove&&handleMousemove($event)" @click="canMove=false"></div>
    </div>
    <div class="btn-left"></div>
    <div class="btn-right"></div>
    <div class="dialog-box" v-if="dialogShow" @click="(!messageShow) && dialogHandle()">
    <div class="dialog" @click.stop v-show="!messageShow">
      <p class="title">{{dialogTitle}}</p>
      <div class="btn" @click="handleDialogConfirm">确定</div>
      <div class="btn" @click="dialogShow=false">取消</div>
    </div>
    <div class="message" v-if="messageShow">{{message}}</div>
    </div>
    <div class="stamp-list-dialog" v-if="stampListShow" @click="stampListShow=false">
    <ul class="stamp-list">
        <li class="list-item" v-for="item in stampList" :key="item.value" @click="handleStampList">
        <div class="stamp-img"></div>
        <span class="stamp-text">{{item.name}}</span>
        </li>
    </ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      stampTop: '-1000px',
      stampLeft: '-1000px',
      stampShow: false,
      canMove: false,
      dialogShow: false,
      dialogTitle: '',
      messageShow: false,
      message: '',
      stampListShow: false,
      stampList: [],
      imgSrc: ''
    }
  },
  methods: {
    handleCancal () {
      this.stampTop = this.stampLeft = '-1000px'
      this.dialogTitle = '是否取消盖章'
      this.dialogShow = true
    },
    handleDialogConfirm () {
      if (this.dialogTitle === '是否取消盖章') {
        this.$router.go(-1)
      } else {}
    },
    handleConfirm () {
      this.message = '执行盖章中'
      this.messageShow = true
      this.dialogShow = true
      setTimeout(() => {
        this.dialogTitle = '盖章成功，是否退出账号'
        this.messageShow = false
      }, 3000)
    },
    handleRemove () {
      this.canMove = true
      this.stampShow = false
      this.imgSrc = JSON.parse(this.$route.query.data).Img_contract
    },
    handleChange () {
      this.stampListShow = true
      this.imgSrc = JSON.parse(this.$route.query.data).Img_contract
    },
    handleMouseenter () {
      this.stampShow = true
    },
    handleMouseleave () {
      this.stampShow = !this.canMove
    },
    handleMousemove (event) {
      this.stampTop = event.offsetY + 'px'
      this.stampLeft = event.offsetX + 'px'
    },
    dialogHandle () {
      this.dialogShow = this.messageShow = false
    },
    handleStampList () {
      this.stampTop = this.stampLeft = '-1000px'
      this.canMove = true
      this.stampShow = this.stampListShow = false
    },
    getStampLists () {
      this.$axios({
        method: 'get',
        url: '/stamp/lists/'
      }).then(res => {
        console.log(res)
        if (res.status === 200 && res.data.code === 200) {
          let data = res.data.data
          for (let index = 0; index < data.length; index++) {
            this.stampList.push({
              name: (index + 1) + '. ' + data[index].stamper_name
            })
          }
        }
      }).catch(err => {
        console.log(err)
      })
    },
    getImgData () {
      if (!this.$route.query.data) {
        this.imgSrc = ''
      } else {
        this.imgSrc = JSON.parse(this.$route.query.data).Img_draw
      }
    }
  },
  mounted () {
    this.getImgData()
    this.getStampLists()
  }
}
</script>

<style lang="stylus" scoped>
  .preview
    position relative
    width 100%
    height 100%
    background url(../assets/bg.png) no-repeat
    background-size 100% 100%
    .cancal
    .confirm
    .remove
    .change
      position absolute
      top 25px
      width 146px
      height 47px
      background url(../assets/pvbtn.png) no-repeat
      background-size 100% 100%
      color #3E9FD2
      font-size 20px
      font-weight 500
      line-height 44px
      text-align center
      cursor pointer
    .cancal
      left 25px
    .confirm
      right 25px
    .remove
      top 560px
      right 25px
    .change
      top 618px
      right 25px
    .pv-title
      position absolute
      top 82px
      left 0
      width 100%
      color #fff
      font-size 29px
      font-weight 400
      text-align center
    .doc
      position absolute
      top 143px
      left 50%
      transform translateX(-50%)
      width 370px
      overflow hidden
      .imgSrc
        width 100%
      .stamp
        position absolute
        transform translate(-50%, -50%)
        opacity 0.7
        width 12%
      .move
        position absolute
        top 0
        left 0
        width 100%
        height 100%
    .btn-left
    .btn-right
      position absolute
      top 50%
      transform translateY(-50%)
      width 100px
      height 100px
      background-size 100% 100%
      cursor pointer
    .btn-left
      left 50px
      background url(../assets/btnL.png) no-repeat
    .btn-right
      right 50px
      background url(../assets/btnR.png) no-repeat
    .dialog-box
      position absolute
      top 0
      left 0
      width 100%
      height 100%
      background-color rgba(0, 0, 0, .79)
      .dialog
        position absolute
        top 50%
        left 50%
        transform translate(-50%, -50%)
        width 314px
        height 188px
        background url(../assets/umBorder.png) no-repeat
        background-size 100% 100%
        .title
          margin-top 45px
          width 100%
          font-size 24px
          font-weight bold
          color rgba(253,252,252,1)
          text-align center
        .btn
          float left
          margin 50px 7px 0
          width 140px
          height 45px
          font-size 18px
          font-weight bold
          color rgba(123,123,123,1)
          text-align center
          line-height 45px
          cursor pointer
          background url(../assets/umbtn1.png) no-repeat
          background-size 100% 100%
          &:nth-of-type(2)
            float right
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
    .stamp-list-dialog
      position absolute
      top 0
      left 0
      width 100%
      height 100%
      background-color rgba(0, 0, 0, .79)
      display flex
      flex-direction column
      align-items center
      justify-content center
      .stamp-list
        padding 40px
        max-height 600px
        overflow-y auto
        .list-item
          width 640px
          height 40px
          border 1px solid rgba(0,255,255,1)
          margin-bottom 3px
          font-size 24px
          font-weight 400
          color rgba(255,255,255,1)
          display flex
          align-items center
          cursor pointer
          &:hover
            box-shadow 0 0 30px rgba(0,255,255,1)
          .stamp-img
            background url(../assets/stampimg.png) no-repeat center center
            width 22px
            height 23px
            display inline-block
            margin-left 9px
            margin-right 20px
</style>
