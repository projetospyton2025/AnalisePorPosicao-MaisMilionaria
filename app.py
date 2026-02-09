"""
Aplicação Flask - Sistema de Análise +Milionária
"""
from flask import Flask
from config import Config
from routes import main_bp, api_bp
from models import ResultadoModel

# Criar aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)

# Registrar blueprints
app.register_blueprint(main_bp)
app.register_blueprint(api_bp)

# Inicializar banco de dados
def init_db():
    """Inicializa o banco de dados"""
    try:
        model = ResultadoModel()
        print("✅ Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados: {e}")

# Executar ao iniciar
with app.app_context():
    init_db()

if __name__ == '__main__':
    print("=" * 60)
    print("🍀 Sistema de Análise +Milionária")
    print("=" * 60)
    print(f"🌐 Servidor rodando em: http://{Config.HOST}:{Config.PORT}")
    print("📊 Acesse o dashboard para começar!")
    print("=" * 60)
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
