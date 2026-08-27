 pyhton
#ANSİ RGB renk fonksiyonu
def rgb_yaz(metin, r, g, b):
  return f"\033[38;2;{r};{g};{b}m{metin}\033[0m"

#Renkli karşılama başlığı
print(rgb_yaz("===================="),0, 255, 255))
print(rgb_yaz("  Geliştirici Portalına Hoşgeldin  "),0, 255, 255))
print(rgb_yaz("===================="),0, 255, 255))

# Farklı rgb renkleriyle mesajlar
print(rgb_yaz("-> Sİstem Durumu Aktif", 50, 205, 50)) #Yeşil
print(rgb_yaz("-> Hedef: Global Remote AI ENGINER", 255, 215, 0)) #Altın Sarısı
print(rgb_yaz("-> Mod: %100 Odaklanma", 255, 69, 0))
