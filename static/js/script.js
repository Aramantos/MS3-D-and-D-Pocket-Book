 $(document).ready(function(){

    // Materialize Scripts
    $('.sidenav').sidenav({edge: "right"});

    // Original Scripts
    $('#login-btn').click(function() {
        $('#login-panel').css('visibility', 'visible');
        $('#login-panel').css('display', 'block');
        $('#reg-panel').css('display', 'none');
    })
    $('#reg-btn').click(function() {
        $('#login-panel').css('display', 'none');
        $('#reg-panel').css('display', 'block');
    })
  }); 