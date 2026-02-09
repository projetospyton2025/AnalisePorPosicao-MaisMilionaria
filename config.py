"""
Configurações da aplicação +Milionária
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações gerais da aplicação"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # Server
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5059))
    
    # Database
    DATABASE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.getenv('DATABASE_PATH', 'database.db')
    )
    
    # API
    API_MAISMILIONARIA_URL = os.getenv(
        'API_MAISMILIONARIA_URL',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/maismilionaria'
    )
    
    # +Milionária Rules
    MIN_NUMEROS = 1
    MAX_NUMEROS = 50
    NUMEROS_SORTEADOS = 6
    MIN_JOGO = 6
    MAX_JOGO = 12
    
    # Trevos (elemento exclusivo)
    MIN_TREVOS = 1
    MAX_TREVOS = 6
    TREVOS_SORTEADOS = 2
    MIN_TREVOS_JOGO = 2
    MAX_TREVOS_JOGO = 6
