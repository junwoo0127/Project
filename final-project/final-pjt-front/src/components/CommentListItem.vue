<template>
  <div class="comment-list-item">
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }} 
    </router-link>: 
    
    <span v-if="!isEditing"> {{ payload.content }}</span>
    <div class="editdeletebtn">
      <span v-if="isEditing">
        <input type="textarea" v-model="payload.content">
        <b-button size="sm" @click="onUpdate">Update</b-button> |
        <b-button variant="danger" @click="switchIsEditing">Cancel</b-button>
      </span>
      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <b-button @click="switchIsEditing">Edit</b-button> |
        <b-button variant="danger" @click="deleteComment(payload)">Delete</b-button>
      </span>
    </div>
    <br>
    <hr>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style scoped>
.comment-list-item {
  margin-left: auto;
  margin-right: auto;
  display: flex;
  width: 60rem;
  justify-content: center;
  align-items: center;
  height: auto;
}
.editdeletebtn {
  margin-left: auto;
}
</style>