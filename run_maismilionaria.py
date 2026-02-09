#!/usr/bin/env python3
"""
Script para executar a aplicação +Milionária
"""
import sys
import os

# Adicionar diretório ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, ConfigMaisMilionaria

if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🍀 INICIANDO SISTEMA DE ANÁLISE +MILIONÁRIA")
    print("=" * 70)
    print(f"📍 Porta: {ConfigMaisMilionaria.PORT}")
    print(f"🌐 URL: http://{ConfigMaisMilionaria.HOST}:{ConfigMaisMilionaria.PORT}")
    print(f"🔧 Debug: {ConfigMaisMilionaria.DEBUG}")
    print("=" * 70 + "\n")
    
    app.run(
        host=ConfigMaisMilionaria.HOST,
        port=ConfigMaisMilionaria.PORT,
        debug=ConfigMaisMilionaria.DEBUG
    )
