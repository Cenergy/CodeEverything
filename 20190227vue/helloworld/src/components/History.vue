<template>
  <div class="history">
    <header-tab backTo='menu'></header-tab>
    <div class="history-box">
      <div class="history-item" v-for="item in historyList" :key="item.value" @click="handleHisItem(item)">
        <img :src="item.img" alt="" class="item-img">
        <p class="item-name">{{item.name}}</p>
      </div>
    </div>
    <div class="dialog" v-show="dialogShow">
      <p class="dialog-title">{{dialogTitle}}</p>
      <div class="item"></div>
      <div class="btn-left"></div>
      <div class="btn-right"></div>
      <div class="btn-print" @click="handerPrint">打印</div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      historyList: [],
      dialogShow: false,
      dialogTitle: ''
    }
  },
  methods: {
    handleHisItem (item) {
      this.dialogTitle = item.name
      this.dialogShow = true
    },
    handerPrint () {
      this.dialogShow = false
    },
    histories () {
      this.$axios({
        method: 'get',
        url: '/stamp/histories/'
      }).then(res => {
        if (res.status === 200 && res.data.code === 200) {
          console.log(res)
          let data = res.data.data.histories
          let list = []
          for (let index = 0; index < data.length; index++) {
            list.push({
              img: data[index].history_img_path,
              name: data[index].stamper_name
            })
          }
          console.log(list)
          this.historyList = list
        } else {
        }
      }).catch(error => {
        console.log(error)
      })
    }
  },
  mounted () {
    this.histories()
  }
}
</script>

<style lang="stylus" scoped>
  .history
    position relative
    width 100%
    height 100%
    background url(../assets/bg.png) no-repeat
    background-size 100% 100%
    .history-box
      position absolute
      top 50%
      left 50%
      transform translate(-50%, -50%)
      width 79%
      height 79%
      display flex
      flex-direction row
      flex-wrap wrap
      overflow auto
      .history-item
        margin 0 1.5% 25px
        width 22%
        height 240px
        .item-img
          display block
          width 100%
          height 90%
          background-color #fff
        .item-name
          margin-top 10px
          width 100%
          height 10%
          color #fff
          font-size 18px
          font-weight 400
          text-align center
    .dialog
      position absolute
      top 0
      left 0
      width 100%
      height 100%
      background-color rgba(0, 0, 0, .79)
      .dialog-title
        position absolute
        top 85px
        left 0
        width 100%
        color #ffffff
        font-size 29px
        font-weight 400
        text-align center
      .item
        position absolute
        top 143px
        left 50%
        transform translateX(-50%)
        width 370px
        height 520px
        background-color #fff
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
      .btn-print
        position absolute
        left 50%
        bottom 0
        transform translateX(-50%)
        width 180px
        height 80px
        background url(../assets/hisbtn.png) no-repeat
        background-size 100% 100%
        cursor pointer
        color #3E9FD2
        font-size 20px
        font-weight 500
        line-height 75px
        text-align center
</style>
