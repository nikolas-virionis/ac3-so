import mysql.connector as sql
import pandas as pd
from time import sleep
from random import randint
from faker import Faker
fake = Faker('pt-BR')

# print(fake.email())

mydb = sql.connect(
    host="localhost",
    user="root",
    password="DigitalSchool1$",
    database="ac3_so"
)

while True:

    registros = pd.read_sql(
        sql="SELECT count(id_dado) as qtd FROM dado", con=mydb)["qtd"][0]
    dados = {
        "nome": fake.name(),
        "email": fake.email(),
        "frase": fake.sentence(),
        "numero": randint(0, 435943)
    }
    print("\n", "-=-"*20)
    print(f"Quantidade de registros: {registros}")

    print(f"""Nome: {dados["nome"]}""")
    print(f"""Email: {dados["email"]}""")
    print(f"""Frase: {dados["frase"]}""")
    print(f"""Numero: {dados["numero"]}""")

    mycursor = mydb.cursor()
    sql_query = f"""INSERT INTO dado VALUES (NULL, '{dados["nome"]}', '{dados["email"]}', {dados["numero"]}, '{dados["frase"]}')"""

    mycursor.execute(sql_query)

    mydb.commit()

    print("-=-"*20, "\n")

    sleep(3)

    print("""0 - sair\n1 - continuar\n""")
    escolha = int(input("Escolha uma opção: "))
    while True:
        if (escolha == 0 or escolha == 1):
            break
        else:
            escolha = int(input("Escolha uma opção válida: "))

    if (not escolha):
        break
