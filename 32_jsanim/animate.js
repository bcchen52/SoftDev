var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("dvd");


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

var dvdLogoSetup = () => {
    var rectWidth = 60;
    var rectHeight = 40;
    var rectX = 50;
    var rectY = 50;
    var xVel = (Math.random() * 10)-5; //-5 to 5
    var yVel = (Math.random() * 10)-5;
    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    stopIt();

    var dvdLogo = () => {
        window.cancelAnimationFrame(requestID);
        clear();

        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

        rectX += xVel;
        rectY += yVel;
        console.log(rectX);

        if (rectX+xVel <0 || rectX+xVel+(rectWidth) > 500) {
            xVel = -xVel;
        }
        if (rectY+yVel < 0 || rectY+yVel+(rectHeight) > 500) {
            yVel = -yVel;
        }
        
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    
    dvdLogo();
};

var stopIt = () => {
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);