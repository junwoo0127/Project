const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    movies: () => HOST + MOVIES + 'movies/',
    movie: moviePk => HOST + MOVIES + 'movies/' + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIES + 'movies/' + `${moviePk}/` + 'like/',
    actors: () => HOST + MOVIES + 'actors/',
    actor: actorPk => HOST + MOVIES + 'actors/' + `${actorPk}/`,
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
    nowplaying: () => HOST + MOVIES + 'nowplaying/',
    genres: () => HOST + MOVIES + 'genres/',
    genreMovie: (genrePk) => HOST + MOVIES + 'genres/' + `${genrePk}/`,
    search: (query) => HOST + MOVIES + 'search/' + `${query}`,
    recommendation: () => HOST + MOVIES + 'recommendation/',
  }
}
