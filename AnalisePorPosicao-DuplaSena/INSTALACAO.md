# 📥 Guia de Instalação - Dupla Sena

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8 ou superior**
  - Verifique: `python --version` ou `python3 --version`
- **pip** (gerenciador de pacotes Python)
  - Verifique: `pip --version` ou `pip3 --version`
- **Git** (opcional, para clonar o repositório)
  - Verifique: `git --version`

## Instalação Passo a Passo

### 1. Obter o Código

#### Opção A: Clonar o Repositório (Recomendado)

```bash
git clone <url-do-repositorio>
cd AnalisePorPosicao-DuplaSena
```

#### Opção B: Download Direto

1. Baixe o arquivo ZIP do repositório
2. Extraia o conteúdo
3. Navegue até o diretório extraído

### 2. Criar Ambiente Virtual (Recomendado)

#### Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Ambiente (Opcional)

```bash
cp .env.example .env
```

Edite o arquivo `.env` conforme necessário:
```env
PORT=5060
DEBUG=True
DATABASE_PATH_DUPLASENA=duplasena.db
```

### 5. Executar a Aplicação

```bash
python app.py
```

Ou use o script de execução:
```bash
python run_duplasena.py
```

### 6. Verificar Instalação

Abra seu navegador e acesse:
```
http://localhost:5060
```

Ou teste a API:
```bash
curl http://localhost:5060/api/duplasena/ultimo-resultado
```

## Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'flask'"

**Solução**: Certifique-se de que as dependências foram instaladas:
```bash
pip install -r requirements.txt
```

### Erro: "Address already in use"

**Solução**: A porta 5060 já está em uso. Altere a porta no `.env`:
```env
PORT=5061
```

### Erro: "Permission denied" ao executar scripts

**Solução**: Dê permissão de execução:
```bash
chmod +x run_duplasena.py
```

### Python não encontrado

**Solução**: Tente usar `python3` em vez de `python`:
```bash
python3 app.py
```

## Instalação em Diferentes Sistemas

### Ubuntu/Debian

```bash
# Instalar Python e pip
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Clonar e instalar
git clone <url>
cd AnalisePorPosicao-DuplaSena
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### macOS

```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python3

# Clonar e instalar
git clone <url>
cd AnalisePorPosicao-DuplaSena
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Windows

```bash
# Baixar Python de python.org
# Executar instalador (marcar "Add Python to PATH")

# No PowerShell ou CMD:
git clone <url>
cd AnalisePorPosicao-DuplaSena
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Instalação para Produção

### Com Gunicorn (Linux/Mac)

```bash
pip install gunicorn

gunicorn -w 4 -b 0.0.0.0:5060 app:app
```

### Com Docker

```bash
docker build -t duplasena:latest .
docker run -d -p 5060:5060 --name duplasena duplasena:latest
```

### Com systemd (Linux)

Crie o arquivo `/etc/systemd/system/duplasena.service`:

```ini
[Unit]
Description=Dupla Sena API
After=network.target

[Service]
User=seu-usuario
WorkingDirectory=/caminho/para/AnalisePorPosicao-DuplaSena
ExecStart=/caminho/para/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Ative o serviço:
```bash
sudo systemctl enable duplasena
sudo systemctl start duplasena
```

## Próximos Passos

Após a instalação bem-sucedida:

1. **Atualize a base de dados**:
   ```bash
   curl -X POST http://localhost:5060/api/duplasena/atualizar-ultimos \
     -H "Content-Type: application/json" \
     -d '{"quantidade": 100}'
   ```

2. **Explore as estatísticas**:
   ```bash
   curl http://localhost:5060/api/duplasena/estatisticas/sorteio/1
   ```

3. **Gere seu primeiro palpite**:
   ```bash
   curl -X POST http://localhost:5060/api/duplasena/gerar-palpite \
     -H "Content-Type: application/json" \
     -d '{"estrategia": "equilibrada", "quantidade_numeros": 6}'
   ```

## Suporte

Se encontrar problemas durante a instalação:

1. Verifique os logs de erro
2. Consulte a seção de "Solução de Problemas" acima
3. Abra uma issue no repositório com:
   - Sistema operacional
   - Versão do Python
   - Mensagem de erro completa
   - Passos para reproduzir o problema

---

**Boa sorte com suas análises! 🎲**
