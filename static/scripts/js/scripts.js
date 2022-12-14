const collapse = document.getElementsByClassName("collapse");

// materialise collapsable burger button from https://materializecss.com/navbar.html
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});


// collapse button build based off https://stackoverflow.com/questions/51031556/display-collapse-content-one-at-a-time
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

// materialise auto init from https://materializecss.com/auto-init.html
M.AutoInit()
