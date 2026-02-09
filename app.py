"""
Aplicação Flask - Sistema de Análise +Milionária e Dupla Sena
"""
from flask import Flask
from config import Config
from routes import main_bp, api_bp, duplasena_bp
from models import ResultadoModel, DuplaSenaModel

# Criar aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)

# Registrar blueprints
app.register_blueprint(main_bp)
app.register_blueprint(api_bp)
app.register_blueprint(duplasena_bp)

# Inicializar banco de dados
def init_db():
    """Inicializa os bancos de dados"""
    try:
        model = ResultadoModel()
        print("✅ Banco de dados +Milionária inicializado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados +Milionária: {e}")
    
    try:
        duplasena_model = DuplaSenaModel()
        print("✅ Banco de dados Dupla Sena inicializado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados Dupla Sena: {e}")

# Executar ao iniciar
with app.app_context():
    init_db()

if __name__ == '__main__':
    print("=" * 60)
    print("🍀 Sistema de Análise +Milionária e Dupla Sena")
    print("=" * 60)
    print(f"🌐 Servidor rodando em: http://{Config.HOST}:{Config.PORT}")
    print("📊 Acesse o dashboard para começar!")
    print("🎲 Dupla Sena API disponível em /api/duplasena/*")
    print("=" * 60)
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
