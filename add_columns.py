from app import create_app, db

# Função para adicionar colunas à tabela
def add_columns():
    with db.engine.connect() as conn:
        try:
            # Adicionar a coluna status
            conn.execute("ALTER TABLE missions ADD COLUMN status TEXT")
            # Adicionar a coluna info
            conn.execute("ALTER TABLE missions ADD COLUMN info TEXT")
            # Adicionar a coluna duration
            conn.execute("ALTER TABLE missions ADD COLUMN duration TEXT")
            # Adicionar a coluna cost
            conn.execute("ALTER TABLE missions ADD COLUMN cost NUMERIC(10, 2)")
            print("Colunas adicionadas com sucesso")
        except Exception as e:
            print(f"Erro ao adicionar colunas: {e}")

# Criar um contexto de aplicação
app = create_app()
with app.app_context():
    add_columns()
