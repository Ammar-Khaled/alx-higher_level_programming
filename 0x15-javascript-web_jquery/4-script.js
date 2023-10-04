// toggles the class of the <header> element between red and green
// when the user clicks on the tag DIV#toggle_header
const $ = window.$;
$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
