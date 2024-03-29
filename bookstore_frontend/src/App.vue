<template>
  <HelloWorld msg="Welcome to Bookstore!"/>
  
  <div id="app">
    <BookForm />
    <BookList />
  </div>
</template>

<script>
import BookForm from './components/BookForm.vue';
import BookList from './components/BookList.vue';

export default {
  name: 'App',
  components: {
    BookForm,
    BookList
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
  margin-top: 60px;
}
</style>
