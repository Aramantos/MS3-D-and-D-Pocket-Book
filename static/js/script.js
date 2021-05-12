 $(document).ready(function(){

    // Materialize Scripts
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();

    // Original Scripts

    //login-register.html
    $('#login-btn').click(function() {
        $('#login-panel').css('visibility', 'visible');
        $('#login-panel').css('display', 'block');
        $('#reg-panel').css('display', 'none');
    })
    $('#reg-btn').click(function() {
        $('#reg-panel').css('visibility', 'visible');
        $('#reg-panel').css('display', 'block');
        $('#login-panel').css('display', 'none');
    })
    $('#log-cancel').click(function() {
        $('#login-panel').css('visibility', 'hidden');
    })
    $('#reg-cancel').click(function() {
        $('#reg-panel').css('visibility', 'hidden');
    })

    //profile.html
    $('#game-add-btn').click(function() {
        $('#game-add-panel').css('display', 'block');
        $('#char-add-panel').css('display', 'none');
    })
    $('#game-add-cancel').click(function() {
        $('#game-add-panel').css('display', 'none');
    })
    $('#char-add-btn').click(function() {
        $('#char-add-panel').css('display', 'block');
        $('#game-add-panel').css('display', 'none');
    })
    $('#char-add-cancel').click(function() {
        $('#char-add-panel').css('display', 'none');
    })

    //login-register.html

    //login-register.html
  }); 