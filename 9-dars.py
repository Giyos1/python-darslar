# 9-dars  for takrorlanish operatorlari
# import turtle
#
# t = turtle.Turtle()
#
# for i in range(4):  # list(range(2)) [0,1,2,3]
#     t.forward(100)
#     t.right(90)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for i in mehmonlar: # ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
#     print(i)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:  # skildi boshi
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")  # skildi tanasi
#     print("Hurmat bilan, Palonchiyevlar oilasi")  # skildi tanasi
#
# for i in range(5): # [0,1,2,3,4]
#     print(i)

# IndentationError: expected an indented block
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
# print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")


# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#
# print("Hurmat bilan, Palonchiyevlar oilasi\n")


# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
#     print(mehmonlar)

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# sonlar = list(range(11))  # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati = []  # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son ** 2)  # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
#
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# karra jadvalidan nechi karrani bilmoqchisiz ? soni kiriting >>

# 1*1 = 1
# 1*2 = 1
# 1*3 = 1
# 1*4 = 1
# 1*5 = 1
# 1*6 = 1
# 1*7 = 1

# a = int(input("karra jadvalidan nechi karrani bilmoqchisiz ? soni kiriting >>"))
#
# for i in range(1, 101):
#     print(f'{a}*{i}={a * i}')


import turtle as t

tim = t.Turtle()
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()  # chizmaydigan qalam
#     tim.forward(10)
#     tim.pendown() # chizadigan qalam
n = int(input('nechi burchak chizmoqchisiz kiriting 3 dan katta son kiriting>>'))

for shape_side_n in range(3, n):
    burchak = 360 / shape_side_n  # nechi burchak chizmoqchi bolsangiz 360 ni oshanga bolganingda chiqan burchaka qayarasiz qalamni
    for _ in range(n):
        tim.color("r")
        tim.forward(100)
        tim.right(burchak)

if __name__ == '__main__':
    pass
