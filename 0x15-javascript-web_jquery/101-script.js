// adds, removes and clears LI elements from a list when the user clicks
window.onload = function () {
  const $ = window.$;
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li> Item </li>');
  });
  $('DIV#remove_item').click(function () {
    $('ul.my_list li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
};
