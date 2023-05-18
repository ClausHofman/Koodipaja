$(document).ready(function() {
  var csrfToken = Cookies.get('csrftoken');
  $('#toggle-button').click(function() {
    var objectId = $(this).data('object-id');

    // Send an AJAX request to toggle the boolean value
    $.ajax({
      url: '/view-article-title/' + objectId + '/',
      type: 'POST',
      headers: { 'X-CSRFToken': csrfToken },
      dataType: 'json',
      success: function(response) {
        // Update the boolean value in the HTML
        $('#boolean-value').text(response.my_boolean_field);
      },
      error: function(xhr, errmsg, err) {
        console.log('Error:', errmsg);
      }
    });
  });
});
