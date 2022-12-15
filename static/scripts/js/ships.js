document.addEventListener("load", getShipCol());
function getShipCol(){
    /*
    get the elements with the classes of spaceship and ship colour
    iterate through all html spaceships
    add a colour class to the spaceships based off data recieved from database
     */
    let ships = document.getElementsByClassName("spaceship");
    for (let i = 0; i < ships.length; i++) {
        let ship = ships[i];
            if (ship.classList.contains("1")) {
                ship.classList.add("red-ship");
            } else if (ship.classList.contains("2")) {
                ship.classList.add("green-ship");
            } else if (ship.classList.contains("3")) {
                ship.classList.toggle("blue-ship");
            } else {
                ship.classList.add("yellow-ship");
            } 
        }
    }




