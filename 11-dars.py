# 10 dars vazifa
# # 1
# avtolar = ['toyota','mazda','gm','hyundai',]
# for avto in avtolar:
#     if avto != 'gm':
#         print(avto.title())
#     else:
#         print(avto.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda,
# "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# # 2
# login = input("login ismingizni kiriting>>>:")
# if login == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")

# 3
# teng = input('1-sonni kiriting')
# teng0 = input('2-sonni kiriting')
# if teng == teng0:
#     print("Sonlar teng")
# else:
#     print('Sonlar teng emas')

# 4
# son = int(input('istalgan sonni kiriting'))
# if son > 0:
#     print(f'{son**(1/2)}')
# else:
#     print('musbat son kiriting togo!!!')

# 4 yoshdan kichik bolalarga kirish bepul
# 4 yoshdan 12 yoshgacha kirish 5000 so'm
# 12 yoshdan kattalarga 10000 so'm

# yosh = int(input("yoshingiz nechida>>?"))
#
# if yosh < 4:
#     print("4 yoshdan kichik bolarga kirish bepul : siz uchun bepul")
# elif yosh >= 4 and yosh < 12:
#     print("4 yoshdan 12 yoshgacha kirish 5000 so'm")
# else:
#     print("12 yoshdan kattalarga 10000 so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:  # yosh bolalarga bepul
#     price = 0
# elif yosh <= 12:  # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh < 65:  # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# elif yosh <= 90:  # qariyalarga esa 8000 so'm
#     price = 8000
# else:
#     price = "yoshingiz judayam katta"
#
# print(f"Sizga kirish {price} ")
# # price = 0

kun = input("Bugun nima kun?>>>")
if kun.lower() == 'shanba' and kun.lower() == 'yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')

if __name__ == '__main__':
    pass
