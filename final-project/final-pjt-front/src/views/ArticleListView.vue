<template>
  <div class="Articlelisthome">
     <h1 class="title">
      <br>
      <span>Movie Community</span>      
    </h1>
    <b-button variant="light" id="createbtn" v-if="isLoggedIn">
        <router-link id="link" :to="{ name: 'articleNew' }">New</router-link>
    </b-button>
    <br>
    <br>
    <table class="table">
      <thead>
        <tr>
          <th>Creator</th>
          <th>Title</th>
          <th>Comment</th>
          <th>Likes</th>
          <th>Views</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.pk">          
          <td>{{ article.user.username }}</td>
          <td>
            <router-link id = "link"
            :to="{ name: 'article', params: {articlePk: article.pk} }">
            {{ article.title }}
            </router-link>
          </td>
          <td>{{ article.comment_count }}</td>
          <td>{{ article.like_count }}</td>
          <td>{{ article.views }}</td>          
        </tr>
      </tbody>
    </table>   
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style scoped>
#link {
  text-decoration-line: none;
}

.Articlelisthome {
  color: azure;
}

.table {
  margin-right: auto;
  margin-left: auto;
  width: 65%;
  border-top: 1px solid #ccc;
  border-collapse: collapse;
  color:black;
  position: relative;
  top: 22rem;  
}

#createbtn {
  position: relative;
  right: 20rem;
  top: 21.5rem;
  float: right;
  height: 50%;
  width: 10%;
}

td, th {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.title {
  -webkit-animation: 3s fade;
          animation: 3s fade;
  color: azure;
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
  bottom: 3.5rem;
}
</style>
