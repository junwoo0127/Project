<template>
  <b-form @submit.prevent="onSubmit" class="comment-list-form">
    <div class="commentinput">
      <label for="comment"></label>      
      <b-form-input type="text" id="comment" v-model="content" required placeholder="댓글을 작성하시오."></b-form-input>
      <b-button type="submit" variant="outline-primary">Write</b-button>           
    </div>
    <br>
  </b-form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style scoped>
.commentinput {
  position: relative;
  top: 0.5rem; 
  display: flex; 
  width: 50%;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
}

.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>