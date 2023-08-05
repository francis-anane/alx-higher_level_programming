/* Fetches and prints how to say “Hello” depending on the language code given */
$(document).ready(function () {
  $('INPUT#btn_translate').click(getTranslation); // Run on button click
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (ent) {
      if (ent.keyCode === 13) {
        // Run on enter key stroke
        getTranslation();
      }
    });
  });
});

// Get translation from api url
function getTranslation () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (content) {
    $('DIV#hello').html(content.hello);
  });
}
