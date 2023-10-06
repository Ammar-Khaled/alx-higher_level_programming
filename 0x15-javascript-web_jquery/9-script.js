// fetches hello from https://fourtonfish.com/hellosalut/?lang=fr
// and displays it in the HTML tag DIV#hello
const $ = window.$;
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});
