/* Adds, removes and clears LI elements from a list when the user clicks */
$('document').ready(function () {
  // Add Item on click
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // Remove item on click
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  // clear items on click
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
