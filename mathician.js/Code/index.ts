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
  cos: (num) => {
    return Math.cos(num);
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
};
