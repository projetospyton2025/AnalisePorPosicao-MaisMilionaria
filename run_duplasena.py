#!/usr/bin/env python3
"""
Script para executar a aplicação Dupla Sena
Modalidade SEPARADA e INDEPENDENTE
"""
import sys
import os

# Adicionar diretório ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app_duplasena import app, ConfigDuplaSena

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🎲 INICIANDO SISTEMA DE ANÁLISE DUPLA SENA")
    print("=" * 70)
    print("⚠️  MODALIDADE SEPARADA - Independente da +Milionária")
    print(f"📍 Porta: {ConfigDuplaSena.PORT}")
    print(f"🌐 URL: http://{ConfigDuplaSena.HOST}:{ConfigDuplaSena.PORT}")
    print(f"🔧 Debug: {ConfigDuplaSena.DEBUG}")
    print("=" * 70 + "\n")
    
    app.run(
        host=ConfigDuplaSena.HOST,
        port=ConfigDuplaSena.PORT,
        debug=ConfigDuplaSena.DEBUG
    )
