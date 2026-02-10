# 📦 Guia de Extração - Repositório Dupla Sena

Este guia explica como usar o pacote `AnalisePorPosicao-DuplaSena` para criar um repositório independente.

## 📥 O que está incluído

O pacote contém:
- ✅ Aplicação Flask completa e funcional
- ✅ Todos os modelos, serviços e rotas necessários
- ✅ Configuração independente
- ✅ Documentação completa
- ✅ Scripts de execução
- ✅ Exemplos de uso

## 🚀 Início Rápido

### Método 1: Extrair e Testar Localmente

```bash
# Extrair o arquivo
tar -xzf AnalisePorPosicao-DuplaSena.tar.gz
# ou
unzip AnalisePorPosicao-DuplaSena.zip

# Navegar até o diretório
cd AnalisePorPosicao-DuplaSena

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
python app.py
```

Acesse: http://localhost:5060

### Método 2: Criar Novo Repositório Git

```bash
# Extrair
tar -xzf AnalisePorPosicao-DuplaSena.tar.gz
cd AnalisePorPosicao-DuplaSena

# Inicializar Git
git init
git add .
git commit -m "Initial commit - Dupla Sena independente"

# Criar repositório no GitHub e conectar
git remote add origin https://github.com/SEU-USUARIO/AnalisePorPosicao-DuplaSena.git
git branch -M main
git push -u origin main
```

## 📁 Estrutura do Pacote

```
AnalisePorPosicao-DuplaSena/
├── 📄 README.md                    # Documentação principal
├── 📄 INSTALACAO.md                # Guia de instalação detalhado
├── 📄 MIGRACAO.md                  # Guia para criar novo repositório
├── 🔧 app.py                       # Aplicação Flask
├── ⚙️ config.py                    # Configurações
├── 📋 requirements.txt             # Dependências Python
├── 🚀 run_duplasena.py            # Script de execução
├── 🔒 .gitignore                  # Arquivos ignorados
├── 🔑 .env.example                # Exemplo de configuração
│
├── 📦 models/                      # Modelos de dados
│   ├── __init__.py
│   └── duplasena_model.py         # Modelo com 2 sorteios
│
├── 🎯 services/                    # Lógica de negócio
│   ├── __init__.py
│   ├── api_duplasena_service.py   # API da Caixa
│   ├── duplasena_service.py       # Geração de palpites
│   └── estatistica_duplasena_service.py  # Estatísticas
│
├── 🛣️ routes/                      # Rotas da API
│   ├── __init__.py
│   └── duplasena_routes.py        # Endpoints REST
│
├── 🎨 static/                      # Arquivos estáticos
└── 📄 templates/                   # Templates HTML
```

## ✅ Verificação da Instalação

Execute estes comandos para verificar se tudo está funcionando:

```bash
# 1. Verificar estrutura de arquivos
ls -la

# 2. Verificar imports
python -c "from app import app; print('✅ App importado com sucesso')"

# 3. Testar startup
timeout 3 python app.py || echo "✅ App iniciou corretamente"

# 4. Testar API (em outro terminal)
curl http://localhost:5060/api/duplasena/ultimo-resultado
```

## 🔧 Configuração

### 1. Ambiente Virtual (Recomendado)

```bash
# Criar
python3 -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Variáveis de Ambiente

```bash
# Copiar exemplo
cp .env.example .env

# Editar conforme necessário
nano .env  # ou seu editor preferido
```

Configurações importantes:
```env
PORT=5060                          # Porta do servidor
DEBUG=True                         # Debug mode
DATABASE_PATH_DUPLASENA=duplasena.db  # Banco de dados
```

## 🎯 Casos de Uso

### Uso 1: Desenvolvimento Local

```bash
# Instalar e executar
pip install -r requirements.txt
python app.py

# Em outro terminal
curl -X POST http://localhost:5060/api/duplasena/gerar-palpite \
  -H "Content-Type: application/json" \
  -d '{"estrategia": "equilibrada", "quantidade_numeros": 6}'
```

### Uso 2: Deploy em Produção

```bash
# Instalar com gunicorn
pip install -r requirements.txt gunicorn

# Executar em produção
gunicorn -w 4 -b 0.0.0.0:5060 app:app
```

### Uso 3: Docker

Crie um `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5060
CMD ["python", "app.py"]
```

Build e run:
```bash
docker build -t duplasena:latest .
docker run -p 5060:5060 duplasena:latest
```

### Uso 4: Novo Repositório GitHub

```bash
# Extrair pacote
tar -xzf AnalisePorPosicao-DuplaSena.tar.gz
cd AnalisePorPosicao-DuplaSena

# Inicializar repositório
git init
git add .
git commit -m "🎲 Initial commit - Sistema Dupla Sena"

# Conectar ao GitHub
git remote add origin https://github.com/SEU-USUARIO/seu-repo.git
git branch -M main
git push -u origin main
```

## 📚 Próximos Passos

Após extrair e configurar:

1. **Leia a documentação**
   - README.md - Visão geral completa
   - INSTALACAO.md - Detalhes de instalação
   - MIGRACAO.md - Criar novo repositório

2. **Teste a aplicação**
   ```bash
   python app.py
   ```

3. **Atualize a base de dados**
   ```bash
   curl -X POST http://localhost:5060/api/duplasena/atualizar-ultimos \
     -H "Content-Type: application/json" \
     -d '{"quantidade": 50}'
   ```

4. **Explore a API**
   - `/api/duplasena/estatisticas/sorteio/1` - Estatísticas sorteio 1
   - `/api/duplasena/estatisticas/sorteio/2` - Estatísticas sorteio 2
   - `/api/duplasena/gerar-palpite` - Gerar palpites
   - `/api/duplasena/ultimo-resultado` - Último resultado

## 🆘 Solução de Problemas

### Erro: "No module named 'flask'"
**Solução**: Instale as dependências
```bash
pip install -r requirements.txt
```

### Erro: "Address already in use"
**Solução**: Mude a porta no .env
```bash
echo "PORT=5061" >> .env
```

### Erro: "Permission denied"
**Solução**: Dê permissão de execução
```bash
chmod +x run_duplasena.py
```

## 📦 Formatos Disponíveis

- **TAR.GZ**: `AnalisePorPosicao-DuplaSena.tar.gz` (33KB)
  - Melhor para Linux/Mac
  - Preserva permissões de arquivo
  
- **ZIP**: `AnalisePorPosicao-DuplaSena.zip` (47KB)
  - Melhor para Windows
  - Compatível com todos os sistemas

## 🔄 Atualizações

Para manter seu código atualizado:

```bash
# Se você criou um repositório Git
git pull origin main

# Reinstalar dependências
pip install -r requirements.txt --upgrade
```

## 📞 Suporte

Problemas durante a extração ou uso?

1. Verifique a documentação incluída (README.md, INSTALACAO.md)
2. Certifique-se de ter Python 3.8+ instalado
3. Verifique se todas as dependências foram instaladas
4. Abra uma issue no repositório original

## 📝 Licença

Este código é fornecido para fins educacionais e de análise estatística.

---

**Pronto para começar! 🎲 Boa sorte com suas análises da Dupla Sena!**
