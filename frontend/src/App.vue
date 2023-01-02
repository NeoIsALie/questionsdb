<template>
  <app-header />
  <section>
    <BurgerButton
      :active="isActive"
      @click="() => isActive = !isActive"
    />

    <BurgerButton
      :active="!isActive"
      @click="() => isActive = !isActive"
    />
  </section>
  <router-view/>
  <app-footer />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
import AppHeader from '@/components/AppHeader.vue';
import AppFooter from '@/components/AppFooter.vue';
import BurgerButton from '@/components/BurgerButton.vue';

export default {
  components: {
    AppFooter,
    AppHeader,
    BurgerButton,
  },
  data: () => ({ isActive: false }),
};
</script>


