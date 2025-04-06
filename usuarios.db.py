import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# CREATE TABLE – Criar a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
conn.commit()

# CREATE – Inserir novo usuário
def criar_usuario(nome, email):
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    print("Usuário criado com sucesso!")

# READ – Listar todos os usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    for linha in cursor.fetchall():
        print(linha)

# UPDATE – Atualizar nome e email do usuário
def atualizar_usuario(id_usuario, novo_nome, novo_email):
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_usuario))
    conn.commit()
    print("Usuário atualizado com sucesso!")

# DELETE – Remover um usuário
def deletar_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conn.commit()
    print("Usuário deletado com sucesso!")

# Testando o CRUD
criar_usuario("Ana", "ana@email.com")
criar_usuario("Carlos", "carlos@email.com")

print("\nLista de usuários:")
listar_usuarios()

print("\nAtualizando usuário:")
atualizar_usuario(1, "Ana Paula", "ana.paula@email.com")

print("\nLista após atualização:")
listar_usuarios()

print("\nDeletando usuário:")
deletar_usuario(2)

print("\nLista final:")
listar_usuarios()

# Fechar a conexão ao final
conn.close()
