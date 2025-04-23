import pg8000

conexao_banco = pg8000.connect(user='postgres',
                            password='123456',
                            host='localhost',
                            database='aula_rad_quarta'
                            )

def inserir_empregado_com_matricula_automatica(nome, data_nasc):
    cursor = conexao_banco.cursor()
    cursor.execute(
        "INSERT INTO EMPREGADOS_INST (nome_empregado, data_nasc) VALUES ( %s, %s)",
        (nome, data_nasc)
    )

    conexao_banco.commit()
    cursor.close()
    print("Empregado inserido com sucesso")


def inserir_empregado(matricula, nome, data_nasc):
    cursor = conexao_banco.cursor()
    cursor.execute(
        "INSERT INTO EMPREGADOS_INSTITUICAO (matricula, nome_empregado, data_nasc) VALUES (%s, %s, %s)",
        (matricula, nome, data_nasc)
    )

    conexao_banco.commit()
    cursor.close()
    print("Empregado inserido com sucesso")

def listar_empregados():
    cursor = conexao_banco.cursor()
    cursor.execute("SELECT MATRICULA, NOME_EMPREGADO, DATA_NASC FROM EMPREGADOS_INSTITUICAO")
    empregados = cursor.fetchall()
    for emp in empregados:
        print(f"MATRICULA: {emp[0]}, Nome: {emp[1]}, Nascimento: {emp[2]}")
    cursor.close()

def atualizar_nome(matricula, novo_nome):
    cursor = conexao_banco.cursor()
    cursor.execute(
        "update empregados_instituicao set nome_empregado = %s where matricula = %s",
        (novo_nome, matricula)
    )

    retorno = cursor.rowcount
    print(retorno)
    if retorno == 0:
        print("Esse dado nao existe para atualizar")

    conexao_banco.commit()
    cursor.close()
    print("Nome atualizado")

def deletar_empregado(matricula):
    cursor = conexao_banco.cursor()
    cursor.execute(
        "DELETE FROM empregados_instituicao WHERE matricula = %s",
        (matricula, )
    )
    conexao_banco.commit()
    cursor.close()
    print("Empregado removido")

# inserir_empregado(1, "Francisco Wendel", "2005-05-05")
# inserir_empregado(3, "Michel", "2002-05-08")
# listar_empregados()
atualizar_nome(2, "Michel Barbosa de Gouveas")
# deletar_empregado(1)
listar_empregados()
conexao_banco.close()