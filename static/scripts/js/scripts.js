
 /* collapse buttons
    get element with class of collapse

  */
  let collapse = document.getElementsByClassName("collapse");
  for (let i = 0; i < collapse.length; i++) {
    collapse[i].addEventListener("click", function() {
      this.classList.toggle("active");
      let content = this.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }

 // materialise collapsable burger button
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });

  window.addEventListener("load", function() {
    this.alert("Welcome to the staion username(placeholder), on this site you can create your own cat spaceship, ready to take on the stars Customise your crew and ship and share them with friends!")
});


M.AutoInit()
