import fisika.kecepatan
from fisika.kecepatan import jarak as jr
from ekonomi.pajak import pph as pph

import time
waktu_awal = time.time()

import currency.rupiah
hasil_laju = fisika.kecepatan.laju ( 10 , 5 )
print(f"hasil lajunya adalah : {hasil_laju} m/s")

hasil_jarak = jr(10,5)
print(f"hasil jaraknya adalah : {hasil_jarak} m")

hasil_waktu = fisika.kecepatan.waktu ( 10 , 5 )
print(f"hasil waktunya adalah : {hasil_waktu} s")

waktu_akhir = time.time()
print(f"waktu yang di eksekusi : {waktu_akhir - waktu_awal}")

hasil_pajak = currency.rupiah.jd_rupiah(pph(40000000))
print(f"pajak tahunan anda : {hasil_pajak}")

