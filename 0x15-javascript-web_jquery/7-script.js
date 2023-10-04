// fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// then display it in the HTML tag DIV#character
const $ = window.$;
$.ajax(
  'https://swapi-api.alx-tools.com/api/people/5/',
  {
    data: { format: 'json' },
    success: function (data) {
      $('DIV#character').html(data.name);
    }
  }
);
