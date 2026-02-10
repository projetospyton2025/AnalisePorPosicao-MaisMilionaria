"""
Configuração da aplicação Dupla Sena
Modalidade SEPARADA e INDEPENDENTE
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configurações da aplicação Dupla Sena"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # Server
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5060))
    
    # Database
    DATABASE_PATH_DUPLASENA = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.getenv('DATABASE_PATH_DUPLASENA', 'duplasena.db')
    )
    
    # API
    API_DUPLASENA_URL = os.getenv(
        'API_DUPLASENA_URL',
        'https://servicebus2.caixa.gov.br/portaldeloterias/api/duplasena'
    )
    
    # DuplaSena Rules
    DUPLASENA_MIN_NUMEROS = 1
    DUPLASENA_MAX_NUMEROS = 50
    DUPLASENA_NUMEROS_SORTEADOS = 6
    DUPLASENA_MIN_JOGO = 6
    DUPLASENA_MAX_JOGO = 15


# Alias for compatibility
ConfigDuplaSena = Config
