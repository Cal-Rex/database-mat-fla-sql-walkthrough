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