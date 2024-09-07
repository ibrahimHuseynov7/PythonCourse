
kitablar = {
    "Dəli Kür": "İsmayıl Şıxlı",
    "Əli və Nino": "Qurban Səid",
    "Yeddi Gözəl": "Nizami Gəncəvi"
}


kitab_adlari = kitablar.keys()
print("Kitab adları:", list(kitab_adlari))


müəllif_adlari = kitablar.values()
print("Müəllif adları:", list(müəllif_adlari))


kitab_muellif_cütleri = kitablar.items()
print("Kitab-Müəllif cütü:")
for kitab, muellif in kitab_muellif_cütleri:
    print(f"{kitab}: {muellif}")
