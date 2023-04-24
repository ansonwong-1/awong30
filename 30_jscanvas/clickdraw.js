/*
Anson Wong
SoftDev pd2
K30 -- canvas based JS drawing
2023-04-24
*/
//draw rectangle top left corner at click
//draw circle center at click
//rect|circ -> circle -> rectangle

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect"){
        mode = "circ";
    }else{
        mode = "rect";
    }
}

var drawRect = (e) => {
    var mouseX = e.offsetX;  
    var mouseY = e.offsetY;
    console.log("mouseclick registered at", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.fillRect(mouseX, mouseY, 100, 150);
    ctx.strokeRect(mouseX, mouseY, 100, 150);
}

var drawCircle = (e) => {
    var mouseX = e.offsetX;  
    var mouseY = e.offsetY;
    console.log("mouseclick registered at", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(mouseX, mouseY, 50, 0, Math.PI * 2, true);
    
}

var draw = (e) => {
    if (mode == "rect"){
        drawRect(e);
    } else {
        drawCircle(e);
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0,0,600,600);
}


c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");;
clearB.addEventListener("click", wipeCanvas);;

