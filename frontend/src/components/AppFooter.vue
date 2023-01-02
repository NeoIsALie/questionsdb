<template>
  <footer>
    <nav>
      <h1>
        <img src="@/assets/images/logo.png" alt="questionsdb" />
      </h1>
      <ul>
        <li>© 2022 neoisalie feat. negovori</li>
      </ul>
    </nav>
  </footer>
</template>

<script lang="ts">
import { Vue } from 'vue-class-component';

export default class TheFooter extends Vue {}
</script>

<style lang="scss" scoped>
footer {
  width: 100%;
  height: 3rem;
  border-top: 1px solid $color-border-primary;
  position: absolute;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  nav {
    width: 90%;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
li {
  margin: 0 0.5rem;
  a {
    color: $color-text-primary;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}
h1 {
  margin: 0;
  display: flex;
  align-items: center;
  color: $color-text-primary;
  img {
    height: 2rem;
  }
  a {
    color: $color-text-primary;
    text-decoration: none;
    margin: 0;
    padding: 0.75rem 1.5rem;
    display: inline-block;
    &:hover,
    &:active,
    &.router-link-active {
      border-color: transparent;
    }
  }
}
</style>
