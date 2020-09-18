function translate(typef, filename) {
    solution = [];
    token = " ";

    f = openfile(filename, "r");
    content = f.read();
    //f.close();

    if (typef == "csv") {
        token = ",";
    } else {
        if (typef == "tsv") {
            token = "   ";
        }
    }
    rows = content.split("\n");
    for (i = 0; i < row.leght(); i++) {
        column = i.split(token);
        solution.push(column);

    }
    return solution;
}