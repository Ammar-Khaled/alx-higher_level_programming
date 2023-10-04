// fetches and lists the title for all movies by using
// this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// in the HTML tag UL#list_movies
const $ = window.$;
$.ajax(
  'https://swapi-api.alx-tools.com/api/films/',
  {
    data: { format: 'json' },
    success: function (data) {
      for (let i = 0; i < data.results.length; i++) {
        $('UL#list_movies').append('<li> ' + data.results[i].title + ' </li>');
      }
    }
  }
);
