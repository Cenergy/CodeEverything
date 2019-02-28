<template>
  <div class="stamp">
    <header-tab backTo='Control'></header-tab>
    <div class="container">
      <div class="stamp-btn">
        <div class="stamp-item">新增印章</div>
        <div class="stamp-item">选择印章</div>
      </div>
      <ul class="stamp-list">
        <li class="list-item" v-for="item in stampList" :key="item.value">
          <div class="stamp-img"></div>
          <span class="stamp-text">{{item.name}}</span>
        </li>
        <!-- <li class="list-item">
          <div class="stamp-img"></div>
          <span class="stamp-text">1.XXXXXX印章</span>
        </li>
        <li class="list-item">
          <div class="stamp-img"></div>
          <span class="stamp-text">1.XXXXXX印章</span>
        </li>
        <li class="list-item">
          <div class="stamp-img"></div>
          <span class="stamp-text">1.XXXXXX印章</span>
        </li> -->
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      stampList: []
    }
  },
  methods: {
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
          // this.stampList = data
          // console.log(this.stampList)
        } else {
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted () {
    this.getStampLists()
  }
}
</script>

<style lang="stylus" scoped>
  .stamp
    width 100%
    height 100%
    background url(../../assets/bg.png) no-repeat center center
    background-size 100% 100%
    .container
      width 100%
      height 95%
      display flex
      flex-direction column
      align-items center
      justify-content center
      .stamp-btn
        width 640px
        display flex
        justify-content space-between
        margin-bottom 3px
        .stamp-item
          width 169px
          height 53px
          background url(../../assets/stampbd.png) no-repeat center center
          font-size 16px
          font-family SourceHanSansCN-Regular
          font-weight 400
          color rgba(253,252,252,1)
          text-align center
          line-height 53px
          cursor pointer
        .stamp-item:hover
          opacity .7
      .stamp-list
        max-height 600px
        overflow-y auto
        .list-item
          width 640px
          height 40px
          border 1px solid rgba(0,255,255,1)
          margin-bottom 3px
          font-size 24px
          font-family SourceHanSansCN-Regular
          font-weight 400
          color rgba(255,255,255,1)
          display flex
          align-items center
          cursor pointer
          .stamp-img
            background url(../../assets/stampimg.png) no-repeat center center
            width 22px
            height 23px
            display inline-block
            margin-left 9px
            margin-right 20px
</style>
