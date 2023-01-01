<template>
  <div class="bm-burger-button">
    <span class="bm-burger-bars line-style" style="top: 0%"> </span>
    <span class="bm-burger-bars line-style" style="top: 40%"> </span>
    <span class="bm-burger-bars line-style" style="top: 80%"> </span>
  </div>
  <input v-model="search" placeholder="Search a question" />
  <div class="last_questions"> Последние вопросы</div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'QuestionsView',
});
</script>

<style>
input {
  display: block;
  width: 680px;
  margin: 50px auto;
  padding: 10px 45px;
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

 .bm-burger-button {
      position: fixed;
      width: 36px;
      height: 30px;
      left: 36px;
      top: 115px;
      cursor: pointer;
    }
.bm-burger-bars {
      background-color: #373a47;
}
.line-style {
      position: absolute;
      height: 20%;
      left: 0;
      right: 0;
}
</style>
