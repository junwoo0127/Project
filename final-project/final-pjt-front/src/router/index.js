import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'


import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleNewView from '@/views/ArticleNewView'
import ArticleEditView from '@/views/ArticleEditView'


import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'
import SeriesView from '@/views/SeriesView.vue'
import SearchView from '@/views/SearchView.vue'
import NowPlayingView from '@/views/NowPlayingView.vue'
import MovieRecommendView from '@/views/MovieRecommendView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',  // /profile/neo
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/articles',  // Community Home
    name: 'articles',
    component: ArticleListView
  },
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies/genres',
    name: 'movieGenres',
    component:SeriesView
  },
  {
    path: '/movies/nowplaying',
    name: 'movieNowPlaying',
    component:NowPlayingView
  },
  {
    path: '/movies/search',
    name: 'movieSearch',
    component:SearchView
  },
  {
    path: '/movies/recommendation',
    name: 'movieRecommendation',
    component:MovieRecommendView
  },
  {
    path: '/movies/:moviePk',
    name: 'movieDetail',
    component: MovieDetailView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404    
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
