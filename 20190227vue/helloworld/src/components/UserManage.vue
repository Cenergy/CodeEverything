<template>
  <div class="user-manage">
    <header-tab backTo='Control'></header-tab>
    <router-link class="add-user" :to="{ path: '/face', query: { form: 'face' }}">新增用户</router-link>
    <p class="del-user">选择用户</p>
    <div class="swiper">
      <!-- swiper -->
      <swiper :options="swiperOption">
        <swiper-slide v-for="item in userList" :key="item.value" @click.native="del(item)">
            <div class="text">{{item.name}}</div>
            <img class="img" :src="item.img" alt="">
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>
    </div>
    <div class="del-user-box" v-if="dialogShow" @click="dialogShow=false">
      <div class="dialog" @click.stop>
        <p class="title">{{dialogTitle}}</p>
        <div class="btn" @click="delUser">确定</div>
        <div class="btn" @click="dialogShow=false">取消</div>
      </div>
    </div>
  </div>
</template>

<script>
import { swiper, swiperSlide } from 'vue-awesome-swiper'
export default {
  data () {
    return {
      swiperOption: {
        slidesPerView: 5,
        slidesPerColumn: 2,
        spaceBetween: 40,
        slidesPerGroup: 5,
        slidesPerColumnFill: 'row',
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      },
      userList: [],
      dialogShow: false,
      dialogTitle: '',
      delItem: null
    }
  },
  components: {
    swiper,
    swiperSlide
  },
  methods: {
    getUser () {
      this.$axios({
        method: 'get',
        url: '/user/lists/',
        data: {
        }
      }).then(res => {
        if (res.status === 200 && res.data.code === 200) {
          console.log(res)
          let data = res.data.data
          let list = []
          for (let index = 0; index < data.length; index++) {
            list.push({
              name: data[index].username,
              img: data[index].user_face_path
            })
          }
          this.userList = list
        } else {
        }
      })
    },
    del (item) {
      this.dialogTitle = `确定删除用户${item.name}？`
      this.delItem = item
      this.dialogShow = true
    },
    delUser () {
      let list = []
      for (let index = 0; index < this.user.length; index++) {
        if (this.user[index].id !== this.delItem.id) {
          list.push(this.user[index])
        }
      }
      this.user = list
      this.dialogShow = false
    }
  },
  mounted () {
    this.getUser()
    console.log(location.origin)
  }
}
</script>

<style lang="stylus" scoped>
  .user-manage
    position relative
    width 100%
    height 100%
    background url(../assets/bg.png) no-repeat
    background-size 100% 100%
    .add-user
    .del-user
      position absolute
      top 190px
      width 160px
      height 43px
      font-size 16px
      font-weight bold
      color rgba(253,252,252,1)
      line-height 43px
      text-align center
      cursor pointer
      background url(../assets/umbtn.png) no-repeat
      background-size 100% 100%
      &:hover
        opacity .7
    .add-user
      left 85px
    .del-user
      right 85px
    .swiper
      position absolute
      left 50%
      bottom 170px
      transform translateX(-50%)
      width 90%
      height 320px
      .swiper-container
        height auto!important
        margin-left auto
        margin-right auto
      .swiper-slide
        position relative
        height 140px
        .img
          width 100%
          height 100%
        .text
          position absolute
          top 50%
          left 50%
          transform translate(-50%, -50%)
          width 90%
          height 90%
          color red
          cursor pointer
          &:hover
            box-shadow: 0 0 15px #fff
    .del-user-box
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
</style>
