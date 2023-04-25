var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillstyle = "red";

var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,500,500);
    //console.log("hi");
};

var radius = 0;
var growing = true;

var drawDot = () => {
    //we solved the issue of the circle getting bigger faster
    //by cancelling at the beginning so it would stop the animation 
    //and run it again instead of speeding up every time the button was clicked
    window.cancelAnimationFrame(requestID);
    clear();
    ctx.beginPath();
    //although fillstyle matches what we assigned it, our circles are black?
    //console.log(ctx.fillstyle);
    ctx.arc(250,250, radius, 0, Math.PI * 2, true);
    ctx.fill();
    if (growing){
        radius++; //= radius + 10;
    } else {
        radius--; //= radius - 10;
    }
    if (radius == 250){
        growing = false;
    } else if (radius == 0){
        growing = true;
    }
    //console.log(radius);
    requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);