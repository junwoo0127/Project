<template>  
  <div>
    <h1 class="title">
      <br>
      <span>{{profile.username}}'s Profile</span>      
    </h1>

    <div class="topcard">
      <b-card-group class="cardleader">
        <b-card title="Written Articles" img-src="https://englishonlinetests.com/wp-content/uploads/2021/02/EnglishArticles.png" img-alt="Image" img-top>
          <b-card-text v-for="article in profile.articles" :key="article.pk">
            <router-link id="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>          
          </b-card-text>        
        </b-card>

        <b-card title="Liked Articles" img-src="https://thehub-io.imgix.net/files/s3/20210427091845-c0c13e370c3755ecc6a0a4bb0123981e.png?w=1600&h=900" img-alt="Image" img-top>
          <b-card-text v-for="article in profile.like_articles" :key="article.pk">
            <router-link id="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </b-card-text>        
        </b-card>

        <b-card title="Liked Movies" img-src="https://i1.sndcdn.com/avatars-000589747854-gzbnlo-original.jpg" img-alt="Image" img-top>
          <b-card-text v-for="movie in profile.like_movies" :key="movie.pk">
            <router-link id="link" :to="{ name: 'movieDetail', params: { moviePk: movie.pk } }">
              {{ movie.title }}
            </router-link>
          </b-card-text>        
        </b-card>
      </b-card-group>
    <div>
      <b-button v-if="isSuperUser" variant="danger" @click="goAdmin">Admin</b-button>
    </div>
  </div>

    <!-- <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 영화</h2>
    <ul>
      <li v-for="movie in profile.like_movies" :key="movie.pk">
        <router-link :to="{ name: 'movieDetail', params: { moviePk: movie.pk } }">
          {{ movie.title }}
        </router-link>
      </li>
    </ul> -->
  </div>
      
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'currentUser']),
    isSuperUser () {
      return this.currentUser.is_superuser
    }
  },
  methods: {
    ...mapActions(['fetchProfile']),
    goAdmin () {
      window.open("http://127.0.0.1:8000/admin/")
    }
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>
img.card-img-top {
  height:15rem
}

#link {
  text-decoration-line: none;
}

.topcard {
  display: flex;
  justify-content: center;
  align-items: center;
}

.cardleader {  
  width:70%;
  height: 10%;
  position: relative; 
  top: 25rem;
}

div.card-body {
  height:25rem;
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
  bottom: 5rem;
}
</style>
