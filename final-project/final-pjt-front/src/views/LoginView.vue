<template>
  <div>
    <h1 class="title">
      <br>
      <span>Login</span>      
    </h1>

    <account-error-list v-if="authError"></account-error-list>

    <div class="logininfo">
      <b-form class="formdata" @submit.prevent="login(credentials)">
        <div class="inputdata">
          <label for="username">username</label>
          <b-form-input v-model="credentials.username" type="text" id="username" autofocus required placeholder="아이디를 입력하세요."></b-form-input>
        </div>
        <div class="inputdata">
          <label for="password">password</label>
          <b-form-input v-model="credentials.password" type="password" id="password" required placeholder="비밀번호를 입력하세요."></b-form-input>
        </div>
        <br>
        <b-button type="submit" variant="warning">LOGIN</b-button>        
      </b-form>
      <!-- <b-form @submit.prevent="login(credentials)">
        <div>
          <label for="username">username</label>
          <b-form-input v-model="credentials.username" type="text" id="username" required ></b-form-input>
        </div>
        <br>
        <div>
          <label for="password">password</label>
          <b-form-input v-model="credentials.password" type="password" id="password" required ></b-form-input>
        </div>
        <br>
        <b-button variant="primary">Save</b-button>
      </b-form> -->
    </div>

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
.inputdata {
  width: 25%;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
}

.logininfo {
  position: relative;
  color:#eae9ea ;
  top: 6rem;
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
  bottom: 10rem;
}
</style>
