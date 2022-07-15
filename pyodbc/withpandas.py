import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

dados_conexao =  ("Driver={SQL Server};"
                  "Server=DESKTOP-HHNQI9B;"
                  "Database=ContosoRetailDW;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

vendas_df = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.FactSales', conexao)
print(vendas_df)

vendas_df['Lucro'] = vendas_df['SalesAmount'] - vendas_df['TotalCost'] - vendas_df['DiscountAmount']
vendas_diarias = vendas_df.groupby(['DateKey']).sum()

grafico = vendas_diarias['Lucro'].plot(figsize=(15,5), color='green')
grafico.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('${x:,.0f}'))
plt.show()