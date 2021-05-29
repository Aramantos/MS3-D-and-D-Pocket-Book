 $(document).ready(function () {

     // Materialize Scripts
     $('.sidenav').sidenav({
         edge: "right"
     });
     $('.collapsible').collapsible();
     $('select').formSelect();
     $('.dropdown-trigger').dropdown();
     $('.modal').modal();

     // Original Scripts

     //login-register.html
     $('#login-btn').click(function () {
         $('#login-panel').css('visibility', 'visible');
         $('#login-panel').css('display', 'block');
         $('#reg-panel').css('display', 'none');
         $("#reg-username").val("");
         $("#reg-password").val("");
     })
     $('#reg-btn').click(function () {
         $('#reg-panel').css('visibility', 'visible');
         $('#reg-panel').css('display', 'block');
         $('#login-panel').css('display', 'none');
         $("#log-username").val("");
         $("#log-password").val("");
     })
     $('#log-cancel').click(function () {
         $('#login-panel').css('visibility', 'hidden');
         $("#log-username").val("");
         $("#log-password").val("");
     })
     $('#reg-cancel').click(function () {
         $('#reg-panel').css('visibility', 'hidden');
         $("#reg-username").val("");
         $("#reg-password").val("");
     })

     //profile.html
     $('#game-add-btn').click(function () {
         $('#game-add-panel').css('display', 'block');
         $('#char-add-panel').css('display', 'none');
     })
     $('#game-add-cancel').click(function () {
         $('#game-add-panel').css('display', 'none');
     })
     $('#char-add-btn').click(function () {
         $('#char-add-panel').css('display', 'block');
         $('#game-add-panel').css('display', 'none');
     })
     $('#char-add-cancel').click(function () {
         $('#char-add-panel').css('display', 'none');
     })

     //game.html
     $('#item-add-btn').click(function () {
         $('#item-add-panel').css('display', 'block');
     })
     $('#item-add-cancel').click(function () {
         $('#item-add-panel').css('display', 'none');
     })

     //login-register.html

     //login-register.html
 });