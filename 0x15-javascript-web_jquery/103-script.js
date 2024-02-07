/* global $ */

$('document').ready(function () {
  $('INPUT#btn_translate').click(translateHello);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translateHello();
      }
    });
  });
});

function translateHello () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
