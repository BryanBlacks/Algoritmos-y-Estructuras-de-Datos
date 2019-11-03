function MathOperation() {

    //Funciones afuera de la clase
    this.sum = MathOperationSum;
    this.substraction = MathOperationSubstraction;
    this.multiply = MathOperationMultiply;
    this.divide = MathOperationDivide;
}

function MathOperationSum(a, b) {
    return a + b;
}

function MathOperationSubstraction(a, b) {
    return a - b;
}

function MathOperationMultiply(a, b) {
    return a * b;
}

function MathOperationDivide(a, b) {
    return a / b;
}