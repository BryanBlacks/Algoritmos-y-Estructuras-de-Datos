function randomInt() {
    return Math.random();
}

function random2Int(min = 0, max = 10) {
    // Se establece la cantidad minima y maxima de renglones que se presentaran en la pagina web.
    return parseInt(Math.random() * (max - min) + min);
}