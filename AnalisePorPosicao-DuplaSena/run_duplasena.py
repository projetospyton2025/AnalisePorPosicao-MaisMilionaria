#!/usr/bin/env python3
"""
Script para executar a aplicação Dupla Sena
Modalidade INDEPENDENTE
"""
import sys
import os

# Adicionar diretório ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, Config

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🎲 INICIANDO SISTEMA DE ANÁLISE DUPLA SENA")
    print("=" * 70)
    print("⚠️  MODALIDADE INDEPENDENTE")
    print(f"📍 Porta: {Config.PORT}")
    print(f"🌐 URL: http://{Config.HOST}:{Config.PORT}")
    print(f"🔧 Debug: {Config.DEBUG}")
    print("=" * 70 + "\n")
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
