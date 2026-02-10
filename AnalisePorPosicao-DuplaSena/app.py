"""
Aplicação Flask - Sistema de Análise DUPLA SENA
Modalidade separada e independente
"""
from flask import Flask
from config import Config
from routes import duplasena_bp
from models import DuplaSenaModel

# Criar aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)

# Registrar blueprint da Dupla Sena
app.register_blueprint(duplasena_bp)

# Inicializar banco de dados
def init_db():
    """Inicializa o banco de dados"""
    try:
        model = DuplaSenaModel()
        print("✅ Banco de dados Dupla Sena inicializado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados Dupla Sena: {e}")

# Executar ao iniciar
with app.app_context():
    init_db()

if __name__ == '__main__':
    print("=" * 60)
    print("🎲 Sistema de Análise DUPLA SENA")
    print("=" * 60)
    print(f"🌐 Servidor rodando em: http://{Config.HOST}:{Config.PORT}")
    print("📊 Modalidade INDEPENDENTE")
    print("🎯 API disponível em /api/duplasena/*")
    print("=" * 60)
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
