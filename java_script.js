#Quiz convert celsius to fahrenheit
var celsius = 12;
var fahrenheit = celsius* 1.8 + 32;
console.log(fahrenheit);
#output 53.6


#Quiz favorite food
var favoriteFood = 'chicken wings'
console.log(favoriteFood);

#concatenation by combining the lines
Blowing from the west
Fallen leaves gather
In the east.

#code
var haiku = "Blowing from the west\n" + "Fallen leaves gather\n" + "In the east.";/* concatenate the strings here */
console.log(haiku);

#Equality
"3" > 1
true
3 != "3"
false
true >= 0
true
1 != false
true
false === 0
false

#semicolon;
Define two variables called thingOne and thingTwo and assign them values.
Print the values of both variables in one console.log statement using concatenation. For example, (redblue)
#code
var thingOne="red"; var thingTwo="blue";
console.log(thingOne + thingTwo);

#Quiznumber
Create a variable called bill and assign it the result of 10.25 + 3.99 + 7.15 (don't perform the calculation yourself,
let JavaScript do it!). Next, create a variable called tip and assign it the result of multiplying bill by a 15% tip rate.
#code
var bill = 10.25 + 3.99 + 7.15;
var tip = 0.15 * bill;
var total= tip + bill;
console.log("$" + total.toFixed(2));
#output 24.60

#fill blank message with adjective variables
var adjective1 = 'amazing';
var adjective2 = 'fun';
var adjective3 = 'entertaining';
var madLib = "The Intro to JavaScript course is " + adjective1 + ". James and Julia are so " + adjective2 + ".
 I cannot wait to work through the rest of this " + adjective3 +" content!";
console.log(madLib);

#code
var firstName = "Julia";
var interest = "cat";
var hobby = "play video games"
var awesomeMessage = "Hi, my name is "+ firstName + "." + " I love " + interest + "." +  " In my spare time, I like to "+ hobby + ".";
console.log(awesomeMessage);