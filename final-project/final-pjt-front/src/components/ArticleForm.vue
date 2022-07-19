<template>
  <div class="createinfo">
    <b-form class="formdata" @submit.prevent="onSubmit">
      <div class="inputdata">
        <label for="title">Create</label>
        <b-form-input placeholder="제목을 입력해주세요." v-model="newArticle.title" type="text" id="title"></b-form-input>
      </div>
      <br>
      <div class="textareadata">
        <b-form-textarea
          id="content"
          v-model="newArticle.content"
          placeholder="내용을 입력하세요"
          rows="3"
          max-rows="6"
        ></b-form-textarea>
      </div>
      <br>
      <b-button type="submit" variant="warning">{{action}}</b-button>        
    </b-form>

  <!-- <form @submit.prevent="onSubmit">
    <div>
      <label for="title">제목: </label>
      <input class="w3-input w3-border" placeholder="제목을 입력해주세요." v-model="newArticle.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">내용: </label>
      <textarea v-model="newArticle.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form> -->
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style scoped>
.formdata {
  position: relative;
  top: 15rem;
}

.inputdata {
  width: 25%;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
  font-size: xx-large;
  color: black;
}

.textareadata {
  width: 25%;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
  font-size: xx-large;
  color: black;
}
</style>
