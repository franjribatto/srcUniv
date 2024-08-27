pswd = str(input("Ingrese la contraseña: "))
i = 0
while True:
    pswd_n = str(input("Ingrese la contraseña nuevamente: "))
    if pswd == pswd_n:
        print("Las contraseñas coinciden pavote, solo intentaste", {i}, "veces")
        break
    i = i + 1