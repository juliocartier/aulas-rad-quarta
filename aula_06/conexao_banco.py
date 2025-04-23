import pg8000
try:
    conexao_banco = pg8000.connect(user='postgres',
                                password='123456',
                                host='localhost',
                                database='aula_rad_quarta'
                                )
    print("Conexao com o banco com sucesso", conexao_banco)
    cursor = conexao_banco.cursor()
    cursor.execute("SELECT * FROM EMPREGADO")
    retorno_dados = cursor.fetchall()
    for row in retorno_dados:
        # print(row)
        print(f"Nome = {row[1]} com a data de nascimento = {row[2]}" )


    cursor.close()
    conexao_banco.close()
except Exception as erro:
    print(f"Conexao com o banco falhou: {erro}")
