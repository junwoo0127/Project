<template>
  <div>
    <h1 class="title">
      <br>
      <span>Signup</span>      
    </h1>

    <account-error-list v-if="authError"></account-error-list>
    <div class="signupinfo">
      <b-form @submit.prevent="signup(credentials)">
        <div class="signupdata">
          <label for="username">Username</label>
          <b-form-input v-model="credentials.username" type="text" id="username" required autofocus placeholder="아이디를 입력하세요."></b-form-input>
        </div>
        <div class="signupdata">
          <label for="password">Password</label>
          <b-form-input v-model="credentials.password1" type="password" id="password" required placeholder="비밀번호를 입력하세요."></b-form-input>
        </div>
        <div class="signupdata">
          <label for="password2">Password Confirmation</label>
          <b-form-input v-model="credentials.password2" type="password" id="password2" required placeholder="비밀번호를 한번 더 입력하세요."></b-form-input>
        </div>
        <br>
        <b-button type="submit" variant="warning">Signup</b-button>        
      </b-form>
      <!-- <form @submit.prevent="signup(credentials)">
        <div>
          <label for="username">Username: </label>
          <input  v-model="credentials.username" type="text" id="username" required/>
        </div>
        <div>
          <label for="password1">Password: </label>
          <input v-model="credentials.password1" type="password" id="password1" required />
        </div>
        <div>
          <label for="password2">Password Confirmation:</label>
          <input v-model="credentials.password2" type="password" id="password2" required />
        </div>
        <div>
          <button>Signup</button>
        </div>
      </form> -->
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style scoped>
.signupdata {
  width: 25%;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
}

.signupinfo {
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

