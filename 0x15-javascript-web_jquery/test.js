// script.js

$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation (languageCode) {
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    // Make the AJAX request to fetch the translation
    $.getJSON(apiUrl, function (data) {
      // Update the text of the DIV#hello with the fetched translation
      $('#hello').text(data.hello);
    });
  }

  // Handle the click event on INPUT#btn_translate
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    fetchTranslation(languageCode);
  });

  // Handle the key press event on INPUT#language_code
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) { // 13 is the keycode for the Enter key
      const languageCode = $('#language_code').val();
      fetchTranslation(languageCode);
    }
  });
});
