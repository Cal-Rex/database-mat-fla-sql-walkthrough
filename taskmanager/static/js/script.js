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
  // ---------------------------------------------------------

// ---------------------------------------------------------
// initialisation for datepicker in form
  document.addEventListener('DOMContentLoaded', function() {
    var datepicker = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(datepicker, {
      format: "dd mmm, yyyy",
      i18n: {done: "Select"}
    });
  });
// ---------------------------------------------------------

// ---------------------------------------------------------
// initialisation for category dropdown in form
document.addEventListener('DOMContentLoaded', function() {
  var selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);
});

// ---------------------------------------------------------
// initialisation for collapsible on home page
document.addEventListener('DOMContentLoaded', function() {
  var collapsible = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(collapsible);
});
// ---------------------------------------------------------
// initialisation for collapsible on home page