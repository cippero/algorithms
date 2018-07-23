function towerBuilder(nFloors) {
  let stars = '*';
  let tower = [];
  let spaces = 0;
  let rowSpaces = '';
  for (let i=0; i<nFloors; i++) {
    spaces = ((2*nFloors-1)-stars.length)/2;
    for (let j=0; j<spaces; j++) rowSpaces += ' ';
    tower.push(rowSpaces + stars + rowSpaces);
    stars += '**';
    rowSpaces = '';
  }
  return tower
}

console.log(towerBuilder(1)); //["*"]
console.log(towerBuilder(2)); //[" * ","***"]
console.log(towerBuilder(3)); //["  *  "," *** ","*****"]