

var xray;

function setup() {
    createCanvas(2130, 5142); 
    // createCanvas(720, 400);
    xray = loadImage("images/spine1.jpg");    
    console.log("Blaaa");
}

function draw() {
    background(0);
    image(xray, 0, 0);
}