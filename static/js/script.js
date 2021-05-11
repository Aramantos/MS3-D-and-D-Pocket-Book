 $(document).ready(function(){

    // Materialize Scripts
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();

    // Original Scripts

    //login-register.html
    $('#login-btn').click(function() {
        $('#login-panel').css('visibility', 'visible');
        $('#login-panel').css('display', 'block');
        $('#reg-panel').css('display', 'none');
    })
    $('#reg-btn').click(function() {
        $('#login-panel').css('display', 'none');
        $('#reg-panel').css('display', 'block');
    })

    //profile.html
    $('#game-add-btn').click(function() {
        $('#game-add-panel').css('display', 'block');
    })

    //login-register.html

    //login-register.html
  }); 