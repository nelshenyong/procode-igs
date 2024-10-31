const favorites = ["Seafood", "Salad", "Nugget", "Soup"];
const other = ["Cake", "Pie ", "Donut"];

const allFav = [...favorites, ...other];

console.log(allFav);

const obj1 = {
    firstName: 'Oni-wan',
    age: 30
};

const obj2 = {
    lastName: 'Kenobi',
    gender: 'M'
}

const Obj = {...obj1, ...obj2};

console.log(Obj);