var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circ";
    } else {
        mode = "rect";
    }
}

var drawRect = (e) => {
    var mouseX = e.offsetX;  
    var mouseY = e.offsetY;
    console.log("mouseclick registered at", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.fillRect(mouseX, mouseY, 30, 20);
}

var drawCircle = (e) => {
    var mouseX = e.clientX;  
    var mouseY = e.clientY;
    console.log("mouseclick registered at", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.fillRect(mouseX, mouseY, 30, 20);
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


