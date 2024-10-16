def pph ( nominal ):
    if(nominal < 50000000):
        nilai_pajak = nominal * 0.05
    elif(nominal < 250000000):
        nilai_pajak = nominal * 0.15
    elif(nominal < 500000000):
        nilai_pajak = nominal * 0.25
    elif(nominal >= 500000000):
        nilai_pajak = nominal * 0.30
    else : 
        nilai_pajak = "Tidak ditemukan"
    return nilai_pajak