uniteUnique = (...arrays) => {
  let uniqueArr = [];
  for (let i=0; i<arrays.length; i++) {
    arrays[i].forEach(val => {
      if (Array.isArray(val) && uniqueArr.indexOf(val[0]) === -1 ) { uniqueArr.push([val[0]]); }
      else if (uniqueArr.indexOf(val) === -1) { uniqueArr.push(val); }
    });
  }
  return console.log(uniqueArr)
}


// uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) //should return [1, 3, 2, 5, 4].
// uniteUnique([1, [5], 2], [1, [5]], [2, [4]]) //should return [1, 3, 2, [5], [4]].
// uniteUnique([1, 2, 3], [5, 2, 1]) //should return [1, 2, 3, 5].
// uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]) //should return [1, 2, 3, 5, 4, 6, 7, 8].