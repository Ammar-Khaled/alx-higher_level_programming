// adds a <li> element to a list
// when the user clicks on the tag DIV#add_item
const $ = window.$;
$('DIV#add_item').click(function () {
  $('ul.my_list').append('<li> Item </li>');
});
