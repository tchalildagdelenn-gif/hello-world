# Kullanıcıyı karşılama ve temel hesaplama programı

kullanici_adi = "Mühendis"
hedef_yil = 4

print("Merhaba " + kullanici_adi + "!")
print ("Önümüzdeki" + str(hedef_yil) + " yıl boyunca harika projeler yapacaksın.")

# Basit bir döngü ile sayaç
for yil in range(1, hedef_yil + 1):
  print(str(yil) + ". yil hedefleri için çalışmaya devam!")
