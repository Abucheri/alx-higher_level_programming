/* global $ */

$('document').ready(function () {
  const apiUrl = 'http://localhost:3000/translate';

  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    const requestUrl = `${apiUrl}?lang=${langCode}`;

    $.get(requestUrl, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
