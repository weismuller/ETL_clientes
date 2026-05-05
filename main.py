from extract import extract_data
from transform import transform_data
from load import load_data

df = extract_data('ETL_clientes\clientes_100.csv')
df_transformado = transform_data(df)
load_data(df_transformado, 'ETL_clientes\clientes_tratados.csv')

print('ETL concluído com sucesso!')