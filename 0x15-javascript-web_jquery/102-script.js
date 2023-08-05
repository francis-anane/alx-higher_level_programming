/* Fetches and prints how to say “Hello” depending on the language code given */
$(document).ready(function () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?';
  // fetches for translation with the give lang code on button click
  $('INPUT#btn_translate').click(function () {
    $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (content) {
      // Set the text of DIV#hello tag with the value of hello from the translation
      $('DIV#hello').html(content.hello);
    });
  });
});
