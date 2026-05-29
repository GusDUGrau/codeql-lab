import sqlite3

# Conexão com banco local
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# Criando tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    senha TEXT
)
""")

# Inserindo usuário de teste
cursor.execute("DELETE FROM usuarios")
cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', '123456')")
conexao.commit()

print("=== Sistema de Login ===")

usuario = input("Usuário: ")
senha = input("Senha: ")

# CÓDIGO VULNERÁVEL A SQL INJECTION
query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"

print("\nConsulta SQL gerada:")
print(query)

cursor.execute(query)
resultado = cursor.fetchone()

if resultado:
    print("\nLogin realizado com sucesso!")
else:
    print("\nUsuário ou senha incorretos.")

conexao.close()
    