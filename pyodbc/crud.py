import pyodbc

dados_conexao =  ("Driver={SQL Server};"
                  "Server=DESKTOP-HHNQI9B;"
                  "Database=ContosoRetailDW;")

conexao = pyodbc.connect(dados_conexao, autocommit=True)
cursor = conexao.cursor()


#CREATE
nomeproduto = "toddynho"
valor = 3


cursor.execute(f"INSERT INTO Vendas (nome_produto, preco) VALUES ('{nomeproduto}', {valor})")
conexao.commit()

#READ
cursor.execute("SELECT * FROM Vendas")
resultado = cursor.fetchall()
print(resultado)

#UPDATE
cursor.execute(f"UPDATE Vendas SET preco = 6 WHERE nome_produto = 'toddynho'")
conexao.commit()

#DELETE
cursor.execute(f"DELETE FROM Vendas WHERE nome_produto = 'toddynho'")
conexao.commit()