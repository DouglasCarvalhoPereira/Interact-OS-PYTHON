#FazendoDando_senitdo_aos_dados
users = {}
name = "goode_user"
cont = 10
i = 0
while i < cont:
    users[name] = users.get(name, 0) +1
    i+=1

print(users)