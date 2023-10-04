//  fetches and prints how to say "Hello" depending on the language
window.onload = function () {
  const $ = window.$;
  $('INPUT#btn_translate').click(function () {
    const inputLang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/', { lang: inputLang }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
};
