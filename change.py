def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\n"+"Vuelto"+"\n")
    print(f"Pesos:\n{int(money-expense)}")
    print(f"Centavos:\n{int(((money-expense)%1)*100)}")

change()
