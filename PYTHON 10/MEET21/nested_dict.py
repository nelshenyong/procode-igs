data_mobil = {
    'mobil1' :{
        'merk' : 'Innova Reborn 2.4 G 2016',
        'transmisi' : 'm/t',
        'tahun' : '2016'
    },
    'mobil2' :{
        'merk' : 'Innova Zenix Modellista Hybrid Q',
        'transmisi' : 'a/t',
        'tahun' : '2022'
    },
    'mobil3' :{
        'merk' : 'Fortuner GR Sport',
        'transmisi' : 'm/t',
        'tahun' : '2020'
    }
}

#Ambil data dict
print(f"Data mobil 3: {data_mobil.get('mobil3')}")

print(f"Data mobil 3, merk: {data_mobil['mobil3']['merk']}")
print(f"Data mobil 2, tahun: {data_mobil.get('mobil2').get('tahun')}")

print("-"*25)
#Tidak berlaku
data_mobil_copy = data_mobil.copy()
data_mobil['mobil2']['merk'] = 'Innvova Zenix Non Hybrid V'
print(f"Data mobil ori: {data_mobil}")
print(f"Data mobil copy: {data_mobil_copy}")

#Berlaku
print("-"*25)
from copy import deepcopy
data_mobil_copy2 = deepcopy(data_mobil)
data_mobil['mobil1']['merk'] = 'Innova 2.0 G 2015'
print(f"Data mobil ori: {data_mobil}")
print(f"Data mobil copy: {data_mobil_copy2}")

