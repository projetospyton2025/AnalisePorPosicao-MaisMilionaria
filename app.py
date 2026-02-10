"""
Aplicação Flask - Sistema de Análise +Milionária
"""
from flask import Flask
from config import ConfigMaisMilionaria
from routes import main_bp, api_bp
from models import ResultadoModel

# Criar aplicação Flask
app = Flask(__name__)
app.config.from_object(ConfigMaisMilionaria)

# Registrar blueprints
app.register_blueprint(main_bp)
app.register_blueprint(api_bp)

# Inicializar banco de dados
def init_db():
    """Inicializa o banco de dados"""
    try:
        model = ResultadoModel()
        print("✅ Banco de dados +Milionária inicializado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco de dados +Milionária: {e}")

# Executar ao iniciar
with app.app_context():
    init_db()

if __name__ == '__main__':
    print("=" * 60)
    print("🍀 Sistema de Análise +MILIONÁRIA")
    print("=" * 60)
    print(f"🌐 Servidor rodando em: http://{ConfigMaisMilionaria.HOST}:{ConfigMaisMilionaria.PORT}")
    print("📊 Acesse o dashboard para começar!")
    print("=" * 60)
    
    app.run(
        host=ConfigMaisMilionaria.HOST,
        port=ConfigMaisMilionaria.PORT,
        debug=ConfigMaisMilionaria.DEBUG
    )
