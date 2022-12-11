# Narimon
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for ism in ismlar:
    print(f"Salom {ism},")
print("kod 5 marta takrorlandi\n")

# 3
toq_sonlar = list(range(11, 100, 2))
print(toq_sonlar)
for son in toq_sonlar:
    print(f"{son ** 2} ")

# 4
kinolar = []
print("5ta eng sevgan filmingiz")
for i in range(5):  # n bu yerda 0 dan 4 gacha qiymatlar oladi
    kinolar.append(input(f"{i + 1}-sevgan kinoyingizni kiriting: "))
print(kinolar)

# 5
Dust = []
input('Bugun necha kishi bilan uchrashdingiz?>>>')
for i in range(4):
    Dust.append(input(f"{i + 1}-suhbat qilgan do'stingiz ismi: "))
print(Dust)
print('Dus\'t')
if __name__ == '__main__':
    pass
