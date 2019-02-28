<template>
  <div class="control">
    <header-tab backTo='menu'></header-tab>
    <div class="menu">
      <img src="@/assets/stamp1.png" alt="" class="item" @click="userManage">
      <img src="@/assets/stamp2.png" alt="" class="item" @click="stampHandle">
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    stampHandle: function () {
      this.$router.push('/Stamp')
    },
    userManage () {
      this.$router.push('/UserManage')
    }
  }
}
</script>

<style lang="stylus" scoped>
  .control
    width 100%
    height 100%
    background url(../../assets/bg.png) no-repeat center center
    background-size 100% 100%
    .menu
      width 100%
      height 100%
      display flex
      align-items center
      justify-content center
      .item
        width 233px
        height 233px
        margin-right 30px
        cursor pointer
      .item:hover
        opacity .7
</style>
