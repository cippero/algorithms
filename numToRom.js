const romNoms = { 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M" };
const values = Object.keys(romNoms);

const numToRom = (num) => {
    // get the next bigger roman numeral in case we need to substract, and the one preceding it if we need to add
    const bigger = values.filter(val => val >= num)[0] !== undefined 
        ? values.filter(val => val >= num)[0] 
        : 1000;
    const smaller = values.indexOf(bigger)-1 !== -1 
        ? values[values.indexOf(bigger)-1] 
        : 1;

    // if num is equal to a pure roman numeral or it's bigger than the biggest numeral we want to add
    if (Number(bigger) === num || bigger === 1000) return romanNumeral(num-bigger, romNoms[bigger])

    // set the substracting numeral to be either I,X,C, or M
    const subNum = Number(smaller[0]) === 1 || num < 10 
        ? smaller 
        : values[values.indexOf(smaller)-1];
        
    // if we need to use more than 3 of the same numeral, we need to subtract from the next numeral. otherwise we just add
    return subNum*4 < num 
        ? romanNumeral(num-(bigger-subNum), romNoms[subNum]+romNoms[bigger]) 
        : romanNumeral(num-smaller, romNoms[smaller])
}

const romanNumeral = (num, rom) => {
    // recursively build up the roman numeral until num is 0
    return num > 0 ? rom += numToRom(num) : rom
}

console.log("150", numToRom(150));
console.log("47", numToRom(47));
console.log("123", numToRom(123));
console.log("1998", numToRom(1998));
console.log("2345", numToRom(2345));