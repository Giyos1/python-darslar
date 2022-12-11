# 11-dars vazifalar

# 1
# son = float(input("Juft son kiriting: "))
# a = son % 2  # 0,1
# if son % 2 == 1:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

# 2
# yosh = int(input("Yoshingiz nechida?"))
#
# if yosh <= 4 or yosh >= 60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")
# 3
# son = int(input("Birinchi sonni kiriting: "))
# son1 = int(input("Ikkinchi sonni kiriting: "))
# if son == son1:
#     print(f"{son}={son1}")
# elif son < son1:
#     print(f"{son}<{son1}")
# else:
#     print(f"{son}>{son1}")
# 4
# mahsulotlar = ['un', "yog'", "pitoz", 'tuxum', 'piyoz','kartoshka', 'anor', 'banan', 'uzum', 'qovun']
#
# savat = []
# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'shing: "))
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
# 5
# mahsulotlar = ['un', "yog'", "pitoz", 'tuxum', 'piyoz', 'kartoshka', 'anor', 'banan', 'uzum', 'qovun']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
#
# for i in range(5):
#     savat.append(input(f"Savatga {i + 1}-mahsulotni qo'shing: "))
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if mavjud_emas == []:
#     print('siz soragan barcha mahsulot bizda bor')
# else:
#     print(f'Quydagi mahsulotlar yoq {mavjud_emas}')
# 6
# ismlar = ['narimon','aziz','asilbek','yunus']
#
# login = input("Yangi accaunt tanlang: ")
#
# if login in ismlar:
#     print('Accaunt band, yangi Account tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
# 7
# son = int(input("Istalgan butun son kiriting: "))  # 15
# for i in range(2, 11):
#     if not (son % i):
#         print(f"{son} soni {i} ga qoldiqsiz bo'linadi")


# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
#
# if 1:
#     print('jds')
# print("Hello World!")
# son = int(input("Istalgan son kiriting: "))
# if son >= 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

# mevalar = ['olma', 'anor', 'uzum']
# print(mevalar[3])

# x, y = 50, 50
# z = 250 / (x - y)

# mantiqiy xatoliklar

# radius = 5
# pi = 3.14
# aylana_yuzi = pi * radius ** 2
# print(aylana_yuzi)

# son = float(input("Istalgan son kiriting: "))
# ildiz = son ** (1 / 2)
#
# print(f"{son} ning ildizi {ildiz} ga teng")

mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
for meva in mevalar:
    print(meva)
print("Dastur tugadi")

if __name__ == '__main__':
    pass
