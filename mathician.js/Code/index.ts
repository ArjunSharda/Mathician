module.exports = {
  add: (num1, num2) => {
    return num1+num2;
  },
  subtract: (num1, num2) => {
    return num1-num2;
  },
  multiply: (num1, num2) => {
    return num1*num2;
  },
  divide: (num1, num2) => {
    return num1/num2;
  },
  square: (num) => {
    return num*num;
  },
  floor: (num) => {
    return Math.floor(num);
  },
  ceil: (num) => {
    return Math.ceil(num);
  },
  squareroot: (num) => {
    return Math.sqrt(num);
  },
  log: (num) => {
    return Math.log(num);
  },
  cos: (num1, num2) => {
    return Math.cos(num1, num2);
  },
  cosh: (num1, num2) => {
    return Math.cosh(num1, num2);
  },
  pow: (num) => {
    return Math.pow(num);
  },
  fahrenheit_to_celsius: (num) => {
    return num - 32 * .5556;
  },
  celsius_to_fahrenheit: (num) => {
    return num + 32 * 1.8;
  },
  abs: (num1, num2) => {
    return Math.abs(num1, num2);
  },
  round: (num) => {
    return Math.round(num1, num2);
  },
};
