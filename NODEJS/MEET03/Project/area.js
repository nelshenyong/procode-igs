let l;
let b;
let r;

const circle = (r) => {
    return 3.14 * r * r;
}

const square = (b) => {
    return b * b;
}

const rectangle = (b, l) => {
    return l * b;
}

const triangle = (b , l) => {
    return b * l / 2;
}

const squarePerimater = (b) => {
    return 4 * b;
}

export { circle, square, rectangle, triangle, squarePerimater};