function CSV() {
    this.generateRandomCVS = CVSGenerateRandomCVS;
}

function CVSGenerateRandomCVS() {

    rows = [];
    r = random2Int();

    for (i = 0; i < r; i++) {

        columns = [];
        c = random2Int();

        for (j = 0; j < 5; j++) {
            //Se establecerea un limite de numeros por filas separados por "," ejem: 2342 , 234234.234 , 567567
            columns.push(random2Int());
        }
        //El push es para agregar a una matriz en JS
        rows.push(columns.join(","));
    }
    return rows.join("<br><br><br>");
}