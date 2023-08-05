/* fetches and displays the value of "hello" from the given url in the HTML tag DIV#hello, with JQuery */

$(document).ready(function () { // Allow script to execute only after DOM is fully loaded
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (content) {
    // Update the text of the DIV#hello with the fetched translation
    $('DIV#hello').text(content.hello);
  });
});
