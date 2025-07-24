import mysql.connector

class functions:
    def __init__(self, host, user, password, database):
        self.db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
        }

    def conectar(self):
        return mysql.connector.connect(**self.db_config)


    def remover(self, tabela, campo, objeto_ou_valor):
        try:
            # Se for um objeto com o atributo, extrai o valor
            valor = getattr(objeto_ou_valor, campo) if hasattr(objeto_ou_valor, campo) else objeto_ou_valor # valor direto (ex: int ou str)
            conn = self.conectar()
            cursor = conn.cursor()
            sql = f"DELETE FROM {tabela} WHERE {campo} = %s"
            cursor.execute(sql, (valor,))
            conn.commit()

            if cursor.rowcount == 0:
                print(f"Nenhum registro foi removido da tabela '{tabela}'.")
            else:
                print(f"Registro removido com sucesso da tabela '{tabela}'.")

        except mysql.connector.Error as erro:
            print(f"Erro ao remover dado da tabela '{tabela}': {erro}")
        finally:
            cursor.close()
            conn.close()

    def criar(self, tabela: str, objeto):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            dados = objeto.__dict__
            colunas = ", ".join(dados.keys())
            marcadores = ", ".join(["%s"] * len(dados))
            valores = tuple(dados.values())

            sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({marcadores})"
            cursor.execute(sql, valores)
            conn.commit()

            print("Dado inserido com sucesso!")
            return True

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir dado: {erro}")
            return False
        finally:
            cursor.close()
            conn.close()
    
    def listar(self, tabela):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            sql = f"SELECT * FROM {tabela}"
            cursor.execute(sql)
            resultados = cursor.fetchall()

            #for linha in resultados:
            #    print(linha)
            return resultados

        except mysql.connector.Error as erro:
            print(f"Erro ao consultar dados: {erro}")
            return []
        finally:
            cursor.close()
            conn.close()

    def atualizar(self, tabela, campos: list, valores: tuple, campo_condicao: str, valor_condicao):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            set_clause = ", ".join([f"{campo} = %s" for campo in campos])
            sql = f"UPDATE {tabela} SET {set_clause} WHERE {campo_condicao} = %s"

            valores_totais = valores + (valor_condicao,)
            cursor.execute(sql, valores_totais)
            conn.commit()

            if cursor.rowcount == 0:
                print("⚠️ Nenhum registro foi atualizado.")
            else:
                print("✅ Registro atualizado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao atualizar: {erro}")
        finally:
            cursor.close()
            conn.close()
    
    def join(self, tabela1, tabela2, on, campos="*", where=None, params=None):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            sql = f"SELECT {campos} FROM {tabela1} t1 JOIN {tabela2} t2 ON {on}"
            if where:
                sql += f" WHERE {where}"

            cursor.execute(sql, params if params else ())
            resultados = cursor.fetchall()
            return resultados

        except mysql.connector.Error as erro:
            print(f"Erro ao fazer JOIN entre {tabela1} e {tabela2}: {erro}")
            return []
        finally:
            cursor.close()
            conn.close()

    def adicionar_dualTabela(self, tabela, campos, valores):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            campos_str = ", ".join(campos)
            placeholders = ", ".join(["%s"] * len(campos))
            sql = f"INSERT INTO {tabela} ({campos_str}) VALUES ({placeholders})"

            cursor.execute(sql, valores)
            conn.commit()

            print(f"Inserido em '{tabela}' com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir em '{tabela}': {erro}")
        finally:
            cursor.close()
            conn.close()
    
    def remover_dualTabela(self, tabela, condicoes, texto):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            where_clause = " AND ".join(f"{campo} = %s" for campo in condicoes)
            valores = tuple(condicoes.values())

            sql = f"DELETE FROM {tabela} WHERE {where_clause}"
            cursor.execute(sql, valores)
            conn.commit()
            print(f"Associação removida com sucesso do {texto}'.")
        except mysql.connector.Error as erro:
            print(f"Erro ao remover associação da tabela '{tabela}': {erro}")
        finally:
            cursor.close()
            conn.close()
    
    def adicionar_dualTabela(self, tabela, colunas, valores):
        try:
            conn = self.conectar()
            cursor = conn.cursor()

            colunas_str = ", ".join(colunas)
            placeholders = ", ".join(["%s"] * len(colunas))
            sql = f"INSERT INTO {tabela} ({colunas_str}) VALUES ({placeholders})"

            cursor.execute(sql, valores)
            conn.commit()
            print(f"Animal adicionado com sucesso.")

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir em '{tabela}': {erro}")
        finally:
            cursor.close()
            conn.close()