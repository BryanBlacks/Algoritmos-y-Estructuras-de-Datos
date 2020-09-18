function randomInt() {
    return Math.random();
}

function random2Int(min = 0, max = 10) {
    return parseInt(Math.random() * (max - min) + min);
}

function factorial(num) {
    if (num < 2) {
        return 1;
    } else {
        return num * factorial(num - 1);
    }
}

function fibonacci(num) {
    if (num == 0 || num == 1) {
        return num;
    }
    temp = fibonacci(n - 2) + fibonacci(n - 1);
    return temp;
}