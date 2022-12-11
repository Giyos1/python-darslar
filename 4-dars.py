# 4-Lesson.String and Number va mantiqiy amalar
# string
# shahar = "Қўқон"
# viloyat = 'Фарғона'
#
# # unicode
# print("menga 📞🎇🎏🥾 qil")
# print('\u0061')
# print('\u0032')
#
# # stringda ustida amalar bajarish
# ism = 'Muhammad ali'
# print('Mening ismim ' + ism)
# a = 'Narimon '  # string
# b = 'Muhammad ali '  # string
# print(a + b + 'aka uka')
# yoshi = 12
# print(ism + " " + str(yoshi) + ' da')
# # str(yoshi) stringa ogiradi integerni
#
# # f string
# ism = "Narimon"
# familiya = 'Burxonov'
# tugulgan = 2010
# ism_sharif = f"{ism} {familiya} {yoshi} yoshda tugulgan yili {tugulgan}"
#
# print(ism_sharif)
#
# # maxsus belgilar

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')
# print("ildiz(a+b)")

# string methodlari
# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

# ism_sharif = 'james bond'
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")
#
# ism = input("Ismingiz nima?")
# print("Assalom alaykum, " + ism)
#
# # yangi_ozgaruvchi = f'{} kochasi,{}'
#
# # sonlar
# aholi_soni = '7_594_000_000'
# print(int(aholi_soni))
#
# PI = 3.14
#
# a, b, c = 1, 2, 3
# print("a*b*c=" + str(a * b * c))  # '6'
#
# print(type(a))
# print(type(aholi_soni))

# 1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
# 2 foydalanuvchi yoshini xisoblaymiz
yosh = 2022 - int(t_yil)  # 10 integer
# 3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")

# bir tipdan ikkichi tipga ogirishg
a = 12  # int
print(type(str(a)))
if __name__ == '__main__':
    pass
