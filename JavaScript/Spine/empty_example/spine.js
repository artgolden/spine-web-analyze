

var xray;

function setup() {
    // createCanvas(2130, 5142);
    createCanvas(720, 400);
    xray = loadImage("test.png");    
    console.log("Blaaa");
}

function draw() {
    background(255);
    image(xray, 0, 0);
}