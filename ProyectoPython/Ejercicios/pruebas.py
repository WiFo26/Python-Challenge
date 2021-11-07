#######Para la guerra intergalactica#######
# buzz = [5,6,3,6,4]
# zurg = [3,7,5]
# for i in buzz:
#     for j in zurg:
#         if i > j:
#             print("Buzz ha ganado esta ronda!")
#             zurg.pop(zurg.index(j))
#             buzz[buzz.index(i)] -= 1
#             print(buzz, zurg)
#             break
#         else:
#             print("Zurg ha ganado esta ronda!")
#             buzz.pop(buzz.index(i))
#             zurg[zurg.index(j)] -= 1
#             print(buzz, zurg)
#             break
# battleOver = False
# while not battleOver:
#     if buzz[0] > zurg[0]:
#         print("Buzz ha ganado esta ronda!")
#         zurg.pop(0)
#         buzz[0] -= 1
#     else:
#         print("Zurg ha ganado esta ronda!")
#         buzz.pop(0)
#         zurg[0] -= 1
#     if len(buzz) == 0:
#         print("El malvado emperador Zurg tomara control de la Unimente!")
#         battleOver = True
#     elif len(zurg) == 0:
#         print("Buzz ha vencido!")
#         battleOver = True

#########Para Numeros Primos############
primos = input().split(",")
print(primos)
