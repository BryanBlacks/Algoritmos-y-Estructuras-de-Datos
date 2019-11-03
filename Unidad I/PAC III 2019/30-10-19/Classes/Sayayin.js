function Sayayin(chi){

    this.chi = chi;
    this.fusion = SayayinFusion;

}

    function SayayinFusion(sayayin){

        newSayayin = new Sayayin(this.chi + sayayin.chi * .30);
        return newSayayin;
        
    }