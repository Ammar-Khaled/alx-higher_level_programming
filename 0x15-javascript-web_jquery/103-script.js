// fetches and prints how to say "Hello" depending on the language
window.onload = function () {
  function sayHello () {
    const inputLang = $('INPUT#language_code').val();
    console.log(inputLang);
    $.get('https://fourtonfish.com/hellosalut/', { lang: inputLang }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  const $ = window.$;
  $('INPUT#btn_translate').click(function () {
    sayHello();
  });

  $('INPUT#language_code').keydown(function (event) {
    // if the key code of the pressed key is 13, which corresponds to the Enter key:
    if (event.which === 13) {
      sayHello();
    }
  });
};
