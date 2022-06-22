// Ask user to enter operator
let operator =  prompt("Choose basic operator: +, -, *, or / ");

//collect operands from user
 let num1 = parseFloat(prompt("Enter your first number: "));
 let num2 = parseFloat(prompt("Enter your last number: "));

 let answer;

if (operator == "+") {
    answer = num1 + num2;
 }
 else if (operator == "-") {
    answer = num1 - num2;
 }
 else if (operator == "*") {
    answer = num1 * num2;
 }
 else {
    answer = num1 / num2;
 }
 
 console.log(`${num1} ${operator} ${num2} = ${answer}`);
