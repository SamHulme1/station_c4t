/* consts
*/
const crewPreview = document.getElementById("crew-preview");
const crewConfirm = document.getElementById("crew");
const crewConfirmBtn = document.getElementById("confirm-crew-btn");
const addToCrewBtns = document.getElementsByClassName("addToCrew"); 
const collapse = document.getElementsByClassName("collapse");
const resetCrewBtn = document.getElementById("reset-crew-btn");
let numOfCatsCounter = 0;


/* collapse buttons
  get element with class of collapse

*/
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
  var instances = M.Sidenav.init(elems);
});

/* iterate through all addToCrew buttons
add and event listener to each button
get all the cat info
find the current cat at the same index as the current button 
change the html in the preview section to be the current cats information
disable the current button
add to the counter which records how many times a user selects a cat
if the counter is equal to 4 disable all buttons

*/
for (let i = 0; i < addToCrewBtns.length; i++) {
	addToCrewBtns[i].addEventListener('click', function () {
    let cats = document.getElementsByClassName("cat-info");
    currentCat = cats[i].innerHTML;
    crewPreview.innerHTML += `${currentCat}`;
    addToCrewBtns[i].disabled = true;
    numOfCatsCounter +=1
    alert("cat added to crew");
    alert(`${numOfCatsCounter}`);
    if (numOfCatsCounter == 4){
      alert("all cats addded");
      for (let i = 0; i < addToCrewBtns.length; i++) {
        addToCrewBtns[i].disabled = true;
      }
    }
	});
}

/* add and event listener to the confirm button
if the number of cats is equal to 4 change the inner html in the crew confirm area to be the inner html of the cat preview area
iterate through all buttons and disable
else if the number of cats is not equal to 4 then tell the user they need to add more cats 
*/
crewConfirmBtn.addEventListener("click", function (){
  if (numOfCatsCounter == 4) {
    crewConfirm.innerHTML = `${crewPreview.textContent}`;
    crewPreview.innerHTML = "";
    crewConfirmBtn.disabled = true;
    resetCrewBtn.disabled = true;
    alert("crew confirmed");
    for (let i = 0; i < addToCrewBtns.length; i++) {
      addToCrewBtns[i].disabled = true;
    }
  } else {
    alert("not enough cats added");
  }
})

/* add an event listener to the reset button
change the inner html to be blank 
iterate through all  buttons and change disable to false
reset the counter
*/
resetCrewBtn.addEventListener('click', function(){
  crewPreview.innerHTML = "";
  alert("crew reset");
  numOfCatsCounter = 0
  for (let i = 0; i < addToCrewBtns.length; i++) {
    addToCrewBtns[i].disabled = false;
  }
  return numOfCatsCounter;
})


M.AutoInit()
