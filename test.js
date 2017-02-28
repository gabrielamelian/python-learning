
// Attempt to replicate extendList problem in JS

var list = []

function extendList(val, list){
    list.push(val)
    return list
}

var list1 = extendList(10)
var list2 = extendList(123,[])
var list3 = extendList('a')

console.log("list1" + list1)
console.log("list2" + list2)
console.log("list3" + list3)
