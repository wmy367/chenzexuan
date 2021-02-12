<template>
  <div id="app">
    <!-- <img alt="Blinks" src="./assets/logo.jpeg"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <ShowX />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Vue from 'vue';
import ShowX from './components/ShowX.vue'
export default {
  name: 'App',
  components: {
    // HelloWorld
    ShowX
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  background-color: black;
}
</style>
