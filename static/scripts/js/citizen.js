/* consts
*/
const crewPreview = document.getElementById("crew-preview");
const crewConfirm = document.getElementById("crew");
const crewConfirmBtn = document.getElementById("confirm-crew-btn");
const addToCrewBtns = document.getElementsByClassName("add-to-crew-btn");
const resetCrewBtn = document.getElementById("reset-crew-btn");
const submit = document.getElementById("submit");
let numOfCatsCounter = 0;
let catsdata = [];
/* iterate through all addToCrew buttons
add and event listener to each button
get all the cat info
find the current cat at the same index as the current button 
store the info in the object current cat
change the html in the preview section to be the current cats info
disable the current button
add to the counter which records how many times a user selects a cat
if the counter is equal to 4 disable all buttons

*/
for (let i = 0; i < addToCrewBtns.length; i++) {
	addToCrewBtns[i].addEventListener('click', function () {
    let catsName = document.getElementsByClassName("cat-name");
    let catsJob = document.getElementsByClassName("cat-job");
    let catsFur = document.getElementsByClassName("cat-fur");
    let catsUf = document.getElementsByClassName("cat-uniquef");
    let catPic = document.getElementsByClassName("ctz-img");
    let currentCat = {
      "name": catsName[i].textContent,
      "job": catsJob[i].textContent,
      "fur": catsFur[i].textContent,
      "uniqueFeature": catsUf[i].textContent,
      "img": catPic[i].src
    };
    catsdata.push(currentCat);

    crewPreview.innerHTML += `<div class="col s3 center-align"><img src="${currentCat.img}"> <h3 class="glow-font-medium">${currentCat.name}</h3>`;
    addToCrewBtns[i].disabled = true;
    numOfCatsCounter +=1;
    
    alert("cat added to crew");
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
    crewConfirm.innerText = `${JSON.stringify(catsdata)}`;
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
});

/* add an event listener to the reset button
change the inner html to be blank 
iterate through all  buttons and change disable to false
reset the counter
*/
resetCrewBtn.addEventListener('click', function(){
  crewPreview.innerHTML = "";
  alert("crew reset");
  numOfCatsCounter = 0;
  for (let i = 0; i < addToCrewBtns.length; i++) {
    addToCrewBtns[i].disabled = false;
  }
  return numOfCatsCounter;
});

submit.addEventListener("click", function(){
  if (crewConfirm.innerText == ""){
    alert("not submitted please make sure 4 cats are added");
  }
});

