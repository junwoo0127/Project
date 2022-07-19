import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    movies: [], // title, overview
    movie: {},  // 다 들어가고, actors(pk, 이름), reviews('pk', 'content')
    review: {},
    nowPlayingMovies: [],
    movieGenreList: [], // MovieGenreList 눌렀을때 영화 선택
    movieGenre: [],  // 장르에 해당하는 영화 목록 
    searchList: [],
    recommendList:[],
    inputData: '', 
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    review: state => state.review,
    nowplaying: state => state.nowPlayingMovies,
    movieGenreList: state => state.movieGenreList,
    movieGenre: state => state.movieGenre,
    searchList: state => state.searchList,
    recommendList: state => state.recommendList,
    inputData: state => state.inputData,
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    },
    ismovie: state => !_.isEmpty(state.movie),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = [...state.movies, ...movies],
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, review) => (state.review = review),
    SET_NOWPLAYING: (state, nowplaying) => (state.nowPlayingMovies = nowplaying),
    SET_MOVIEGENRELIST: (state, movieGenreList) => (state.movieGenreList = movieGenreList),
    SET_MOVIEGENRE: (state, movieGenre) => (state.movieGenre = movieGenre),
    SET_SEARCHLIST: (state, searchList) => (state.searchList = searchList),
    SET_RECOMMENDLIST: (state, recommendList) => (state.recommendList = recommendList),
    RESET_SEARCH: (state, resetSearch) => (state.searchList = resetSearch),
    INPUT_DATA: (state, inputData) => (state.inputData = inputData),
  },

  actions: {
    recommendList({ commit, getters }) {
      axios({
        url: drf.movies.recommendation(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_RECOMMENDLIST', res.data)
        console.log(res.data)})
        .catch (err => console.error(err.response))
    },
    inputData({commit}, inputData) {
      commit('INPUT_DATA', inputData)
    },
    resetSearch({commit}) {
      commit('RESET_SEARCH', [])
    },
    searchList({ commit, getters}, query) {
      axios({
        url: drf.movies.search(query),
        method: 'get',
        headers: getters.authHeader,
      }) 
        .then(res => commit('SET_SEARCHLIST', res.data))
        .catch (err => {
          commit('SET_SEARCHLIST', [])
          console.error(err.response)})
    },  
    nowPlayingMovies({ commit, getters}) {
      axios({
        url: drf.movies.nowplaying(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_NOWPLAYING', res.data))
        .catch (err => console.error(err.response))
    },
    fetchMovies({ commit, getters }, page) {
      /* 영화 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 영화들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movies() + `?page=${page}`,
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch (err => {
          commit('SET_MOVIES', [])
          console.error(err.response)
      })
    },

    fetchMovie({ commit, getters }, moviePk) {
      /* 단일 영화 받아오기
      GET: movie URL (token)
        성공하면
          응답으로 받은 영화들을 state.movies에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    createMovie({ commit, getters }, movie) {
      /* 영화 생성
      POST: movies URL (영화 입력정보, token)
        성공하면
          응답으로 받은 영화을 state.movie에 저장
          movieDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      
      axios({
        url: drf.movies.movies(),
        method: 'post',
        data: movie,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
          router.push({
            name: 'movie',
            params: { moviePk: getters.movie.pk }
          })
        })
    },

    updateMovie({ commit, getters }, { pk, title, content}) {
      /* 영화 수정
      PUT: movie URL (영화 입력정보, token)
        성공하면
          응답으로 받은 영화을 state.movie에 저장
          movieDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movie(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
          router.push({
            name: 'movie',
            params: { moviePk: getters.movie.pk }
          })
        })
    },

    deleteMovie({ commit, getters }, moviePk) {
      /* 영화 삭제
      사용자가 확인을 받고
        DELETE: movie URL (token)
          성공하면
            state.movie 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.movie(moviePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_MOVIE', {})
            router.push({ name: 'movies' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeMovie({ commit, getters }, moviePk) {
      /* 좋아요
      POST: likemovie URL(token)
        성공하면
          state.movie 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    fetchReviews({ commit, getters }, { moviePk, reviewPk }) {
      /* 리뷰 목록 받아오기   안쓸 가능성 높음
      GET: movies URL (token)
        성공하면
          응답으로 받은 영화들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {commit('SET_MOVIE_REVIEWS', res.data)
      console.log(res)})
        .catch(err => console.error(err.response))
    },

		createReview({ commit, getters }, { moviePk, score }) {
      /* 리뷰 생성
      POST: reviews URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.movie의 reviews 갱신
        실패하면
          에러 메시지 표시
      */
      const review = {  score }
      console.log(review)
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { moviePk, reviewPk, score }) {
      /* 리뷰 수정
      PUT: review URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.movie의 reviews 갱신
        실패하면
          에러 메시지 표시
      */
      const review = { score }
      console.log(review)
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
      /* 리뷰 삭제
      사용자가 확인을 받고
        DELETE: review URL (token)
          성공하면
            응답으로 state.movie의 reviews 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.review(moviePk, reviewPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_REVIEWS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
    movieGenreList({ commit, getters}) {
      axios({
        url: drf.movies.genres(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIEGENRELIST', res.data))
        .catch (err => console.error(err.response))
    },
    movieGenre({ commit, getters },  genrePk ) {
      console.log(genrePk)
      axios({
        url: drf.movies.genreMovie(genrePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIEGENRE', res.data.movies))
        .catch (err => console.error(err.response))
    },
  },
}
