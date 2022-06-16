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

# #########Para Numeros Primos############
# file = open("harry.txt","r")
# print(file.read().split("#"))

# ###Hotel Review####
# frase = "14,Milestone Hotel Kensington,1 Kensington Court Kensington and Chelsea London W8 5DL United Kingdom"
# pais = "United Kingdom"
# list_frase = frase.split(",")

# if pais in list_frase[2]:
#     print("Si esta")
# else:
#     print("No está")
# ids = {'3': 2, '7': 2}
# most_reviewed = max(ids.values())
# mejores_hoteles = []
# for i in ids.keys():
#     if ids[i] == most_reviewed:
#         mejores_hoteles.append(i)
# print(mejores_hoteles)
reviews = open("reviews.txt")
reviews = reviews.read().split("\n")
bot = open("bots.txt")
bot = bot.read().split("\n")
reviews_index_to_delete = []
print(len(reviews))
for i in bot:
    for j in range(len(reviews)):
        id_usuario = reviews[j].split(",")[0]
        if i == id_usuario:
            reviews_index_to_delete.append(j)
for i in sorted(reviews_index_to_delete,reverse=True):
    reviews.pop(i)
print(len(reviews))