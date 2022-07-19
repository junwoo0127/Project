<template>
  <nav>
    <ul class="Navul">
      <li><router-link to="/">Movies</router-link></li>
      <li><router-link to="/movies/genres">Series</router-link></li>
      <li><router-link to="/movies/nowplaying">NowPlaying</router-link></li>      
      <li>
        <router-link :to="{ name: 'articles' }">CommunityHome</router-link>
      </li>    

      
      <div id="searchbox">
        <span id="search">
          <b-form-input type="text" name="query" @keyup.enter="searchMovie" v-model="query" placeholder="찾는 영화를 검색하세요."></b-form-input>
          <i class="fa-solid fa-magnifying-glass" @click="searchMovie" id="magnify"></i>
        </span>
      </div>   
      

      <li><router-link to="/movies/recommendation">Recommendation</router-link></li> 

      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>
      
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'profile', params: { username } }">
          {{ currentUser.username }}'s page
        </router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </li>      
    </ul>
  </nav>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'NavBar',
    data() {
      return {
        query: '',
      }
    },
    methods: {
      ...mapActions(['searchList']),
      searchMovie() {
        this.$store.dispatch('searchList', this.query)
        if(this.$route.path!=='/movies/search') this.$router.push('/movies/search')
        this.$store.dispatch('inputData', this.query)
        this.query = ''
      }
    },    
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>

ul {
    display: flex;
    list-style: none;
    text-align: center;         
    margin: 0;
    justify-content: center;
    align-items: center;  
}

li {    
    float: left;
    margin-left: 40px;    
}

#searchbox {  
  float: left;
  margin-left: 30px;
}

#search {
  display: flex;
  margin: 3px 3px;
}

#magnify {
  margin: auto;
  margin-left: 3px;
  cursor: pointer;
  color: aliceblue;
}

</style>
