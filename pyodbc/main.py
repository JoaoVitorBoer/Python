import pyodbc


dados_conexao =  ("Driver={SQL Server};"
                  "Server=DESKTOP-HHNQI9B;"
                  "Database=ContosoRetailDW;")

conexao = pyodbc.connect(dados_conexao, autocommit=True)
cursor = conexao.cursor()

table = cursor.execute('SELECT * FROM ContosoRetailDW.dbo.FactSales')
print(list(table))

cursor.execute('ALTER TABLE ContosoRetailDW.dbo.FactSalesADD Lucro NUMERIC Null')
conexao.commit()
cursor.execute('UPDATE ContosoRetailDW.dbo.FactSales SET Lucro = SalesAmount - TotalCost - DiscountAmount')
conexao.commit()
cursor.execute('SELECT DateKey, SUM(Lucro) as Profit from ContosoRetailDW.dbo.FactSales GROUP BY DateKey')



