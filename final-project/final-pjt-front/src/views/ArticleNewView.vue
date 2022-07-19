<template>
  <div>
    <h1 class="title">
      <br>
      <span>New Article</span>      
    </h1>
    <article-form class="articleform" :article="article" action="create"></article-form>
  </div>
</template>

<script>
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style scoped>
.articleform {
  position: relative;
  top: 10rem;
}
.title {
  -webkit-animation: 3s fade;
          animation: 3s fade;
  color:azure;
  font-family: "Abril Fatface", cursive;
  font-size: 5em;
  left: 0;
  position: absolute;
  text-align: center;  
  width: 100%;
  margin: 0;
  height: 10px;  
}
.title span {
  display: inline-block;
  padding: 0.5em 1em;
  position: relative;
  bottom: 2rem;
}
</style>
