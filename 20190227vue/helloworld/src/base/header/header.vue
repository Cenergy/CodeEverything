<template>
  <div class="header">
    <div v-if="backTo" class="back" @click="$router.push(backTo)">
      <img src="@/assets/back.png" alt=""> 返回
    </div>
    <span class="username">{{username}}</span>
    <span class="exit" @click="exit">注销</span>
  </div>
</template>

<script>
export default {
  props: ['backTo'],
  methods: {
    exit () {
      this.$cookies.remove('Authorization')
      this.$cookies.remove('username')
      this.$router.push('/')
    }
  },
  computed: {
    username: function () {
      return this.$cookies.get('username')
    }
  }
}
</script>

<style lang="stylus" scoped>
  .header
    display flex
    justify-content flex-end
    width 100%
    height 30px
    align-self flex-start
    .back
      position absolute
      top 30px
      left 30px
      color #fff
      font-size 18px
      font-weight bold
      cursor pointer
    .username
    .exit
      font-size 24px
      font-family SourceHanSansCN-Regular
      font-weight bold
      color rgba(163,163,163,1)
      margin-right 42px
      line-height 30px
      margin-top 30px
      cursor pointer
    .exit:hover
      color #fff
</style>
