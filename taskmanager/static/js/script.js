// ---------------------------------------------------------
// initialisation for navbar
document.addEventListener('DOMContentLoaded', function() {
    var sidenav = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(sidenav);
  });

//   same code as above, but for if JQuery being used
    // $(document).ready(function(){
    //     $('.sidenav').sidenav();
    // });
// ---------------------------------------------------------

// ---------------------------------------------------------
// initialisation for "delete" modals
document.addEventListener('DOMContentLoaded', function() {
  var modal = document.querySelectorAll('.modal');
  var instances = M.Modal.init(modal);
});

  //   same code as above, but for if JQuery being used
  // $(document).ready(function(){
  //   $('.modal').modal();
  // });