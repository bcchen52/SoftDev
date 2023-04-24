/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Briki :: Brian Chen, Mahir Riki
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};



//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};



//insert your implementations here for...

function fact(n){
  if (n<= 0) 
      return "Error";
  else if (n == 1)
      return 1;
  else {
      var output = 1;
      for (var i = 1; i <= n; i++) {
          output *=i;
      }
      return output;
  }
};

var fib = function(n){
  if(n < 2){
      return n;
  }return (fib(n - 1) + fib(n - 2));
};

function gcd(n1,n2){
  if (n1%n2==0){
    return n2;
  } if (n2%n1==0){
    return n1;
  } 
  return gcd(n2, n1 % n2);
};

//console.log(fib(5));

var dasbut = document.getElementById("fib"); 
dasbut.addEventListener('click', ()=>{
  console.log(fib(7));
  var output = fib(7);
	addItem(output);
});

var dasbut = document.getElementById("fact"); 
dasbut.addEventListener('click', ()=>{
	console.log(fact(5));
  var output = fact(5);
	addItem(output);
});

var dasbut = document.getElementById("gcd"); 
dasbut.addEventListener('click', ()=>{
  var output = gcd(17220,1238);
	addItem(output);
});


// FAC
// GCD
// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};


