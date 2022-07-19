<template>
  <div class="Articledetailhome">
    <h1 class="title">
      <br>
      <span>Article Detail</span>      
    </h1>

    <div class="articleinfo container">
      <h1>Title: {{article.title}}</h1>
      <div class="articleTitle">
        <div class="articleInfo">
          <h5>Author: {{ article.user.username }}</h5>
        </div>
        <div id="editdeletebtn">
          <div v-if="isAuthor">
            <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
              <b-button >Edit</b-button>
            </router-link>
            |
            <b-button size="sm" variant="danger" @click="deleteArticle(articlePk)">Delete</b-button>
            |                
          </div>      
          <button id="likebtn"
            @click="likeArticle(articlePk)"
          ><i class="fa-solid fa-heart" style="color:red"></i>  좋아요: {{ likeCount }}</button>
        </div>
      </div>
      <hr>
      <br>
      <h2>Content: {{ article.content }}</h2>
      <br>

      <!-- Article Edit/Delete UI -->
            
      <!-- Comment UI -->
      <comment-list :comments="article.comments"></comment-list>

    </div>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>
.articleInfo {

}
.articleTitle {
  display: flex;
  justify-content: space-evenly;

}
#likebtn {
  border: 0;
  outline: 0;
}

#editdeletebtn {
  display: flex;
  margin-left: auto;
}

.articleinfo {
  position: relative;
  top: 27rem;
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
