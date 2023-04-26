var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "purple";

var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,500,500);
    console.log("hi");
};

var radius = 0;
var growing = true;

var drawDot = () => {
    //window.cancelAnimationFrame(requestID);
    window.cancelAnimationFrame(requestID);
    clear();
    if (growing){
        radius ++;
    } else {
        radius --;
    }
    if (radius == 250){
        growing = false;
    } else if (radius == 0){
        growing = true;
    }
    ctx.beginPath();
    ctx.arc(250,250, radius, 0, Math.PI * 2, true);
    ctx.fill();
    
    console.log(radius);
    
    requestID = window.requestAnimationFrame(drawDot);
};

var stopIt = () => {
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);