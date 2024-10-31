def konversi_barang(jumlah_barang):
    gross = jumlah_barang // 144  # 1 gross = 144 buah
    sisa_gross = jumlah_barang % 144
    kodi = sisa_gross // 20 # 1 kodi = 20 buah
    sisa_kodi = sisa_gross % 20
    
    lusin = sisa_kodi // 12  # 1 lusin = 12 buah
    sisa_lusin = sisa_kodi % 12
    buah = sisa_lusin
    return (gross, kodi, lusin, buah)

def batas():
    print("-"*43)