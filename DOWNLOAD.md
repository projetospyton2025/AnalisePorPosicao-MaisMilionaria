# 📥 Instruções de Download e Instalação

Guia completo para baixar e configurar o Sistema de Análise +Milionária.

## 📋 Requisitos do Sistema

### Obrigatórios

- **Python**: Versão 3.8 ou superior
- **pip**: Gerenciador de pacotes Python
- **Conexão com Internet**: Para buscar dados da API da Caixa

### Recomendados

- **Sistema Operacional**: Windows 10+, macOS 10.14+, ou Linux (Ubuntu 18.04+)
- **RAM**: Mínimo 2GB disponível
- **Espaço em Disco**: 100MB livres

## 🔽 Opção 1: Download via Git (Recomendado)

### Instalar Git

**Windows:**
```bash
# Baixe e instale de: https://git-scm.com/download/win
```

**macOS:**
```bash
brew install git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install git
```

### Clonar o Repositório

```bash
# Clone o repositório
git clone https://github.com/projetospython2025/AnalisePorPosicao-MaisMilionaria.git

# Entre no diretório
cd AnalisePorPosicao-MaisMilionaria
```

## 🔽 Opção 2: Download Direto (ZIP)

1. Acesse: https://github.com/projetospython2025/AnalisePorPosicao-MaisMilionaria
2. Clique em **"Code"** → **"Download ZIP"**
3. Extraia o arquivo ZIP
4. Abra o terminal/prompt na pasta extraída

## 🐍 Configurar Python

### Verificar Instalação do Python

```bash
python --version
# ou
python3 --version
```

Deve mostrar: `Python 3.8.x` ou superior

### Instalar Python (se necessário)

**Windows:**
1. Baixe de: https://www.python.org/downloads/
2. Execute o instalador
3. ✅ **IMPORTANTE**: Marque "Add Python to PATH"

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

## 📦 Instalar Dependências

### Método Padrão

```bash
# Instalar dependências
pip install -r requirements.txt

# ou, se pip não funcionar:
pip3 install -r requirements.txt
```

### Método com Ambiente Virtual (Recomendado)

**Criar ambiente virtual:**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Instalar dependências:**

```bash
pip install -r requirements.txt
```

### Verificar Instalação

```bash
pip list
```

Deve mostrar:
- Flask
- requests
- python-dotenv

## ⚙️ Configuração Inicial

### 1. Configurar Variáveis de Ambiente (Opcional)

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar (opcional)
nano .env  # ou use seu editor preferido
```

### 2. Configurações Disponíveis

```env
# .env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
HOST=0.0.0.0
PORT=5059
DATABASE_PATH=database.db
API_MAISMILIONARIA_URL=https://servicebus2.caixa.gov.br/portaldeloterias/api/maismilionaria
```

**Nota**: As configurações padrão funcionam perfeitamente. Só mude se necessário.

## 🚀 Executar a Aplicação

### Primeira Execução

```bash
python app.py
```

**Saída esperada:**
```
============================================================
🍀 Sistema de Análise +Milionária
============================================================
✅ Banco de dados inicializado com sucesso!
🌐 Servidor rodando em: http://0.0.0.0:5059
📊 Acesse o dashboard para começar!
============================================================
```

### Acessar no Navegador

Abra seu navegador e acesse:
```
http://localhost:5059
```

## 🔧 Solução de Problemas Comuns

### Erro: "pip: command not found"

**Solução:**
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### Erro: "ModuleNotFoundError"

**Solução:**
```bash
# Reinstalar dependências
pip install --upgrade -r requirements.txt
```

### Erro: "Address already in use" (Porta 5059 ocupada)

**Solução 1 - Mudar porta:**
```bash
# Edite .env
PORT=5060  # ou outra porta disponível
```

**Solução 2 - Liberar porta:**
```bash
# Windows
netstat -ano | findstr :5059
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5059 | xargs kill
```

### Erro: "Failed to connect to API"

**Causas possíveis:**
1. Sem conexão com internet
2. Firewall bloqueando
3. API da Caixa temporariamente offline

**Solução:**
- Verifique sua conexão
- Tente novamente mais tarde
- Verifique se há dados já salvos no banco

### Erro: "Permission denied" ao criar database.db

**Solução:**
```bash
# Linux/macOS
chmod 755 .
chmod 666 database.db

# Windows
# Execute o terminal como Administrador
```

## 📱 Acesso Remoto na Rede Local

### Configurar para Acesso Remoto

1. Edite `.env`:
```env
HOST=0.0.0.0
PORT=5059
```

2. Execute:
```bash
python app.py
```

3. Descubra seu IP:
```bash
# Windows
ipconfig

# macOS/Linux
ifconfig
# ou
ip addr show
```

4. Acesse de outro dispositivo:
```
http://SEU_IP:5059
```

Exemplo: `http://192.168.1.100:5059`

### Configurar Firewall

**Windows:**
```
Painel de Controle → Windows Defender Firewall → 
Configurações Avançadas → Regras de Entrada → Nova Regra →
Porta → TCP → 5059 → Permitir conexão
```

**Linux (Ubuntu):**
```bash
sudo ufw allow 5059/tcp
```

**macOS:**
```
System Preferences → Security & Privacy → Firewall →
Firewall Options → Adicionar Python → Permitir
```

## 🔄 Atualizar o Sistema

### Via Git

```bash
# Entrar no diretório
cd AnalisePorPosicao-MaisMilionaria

# Atualizar
git pull origin main

# Reinstalar dependências (se houver mudanças)
pip install -r requirements.txt
```

### Via Download Manual

1. Faça backup do `database.db`
2. Baixe a nova versão
3. Extraia substituindo os arquivos
4. Restaure o `database.db`
5. Reinstale dependências se necessário

## 🗑️ Desinstalar

### Remover Aplicação

```bash
# Simplesmente delete a pasta
rm -rf AnalisePorPosicao-MaisMilionaria
```

### Remover Ambiente Virtual

```bash
# Se usou venv
rm -rf venv
```

### Limpar Dependências

```bash
# Desinstalar pacotes (opcional)
pip uninstall Flask requests python-dotenv
```

## 📚 Próximos Passos

Após a instalação:

1. ✅ Leia o [QUICKSTART.md](QUICKSTART.md) para uso básico
2. ✅ Atualize a base de dados no Dashboard
3. ✅ Explore as estatísticas
4. ✅ Gere seus primeiros palpites

## 🆘 Suporte

Se encontrar problemas:

1. Consulte a seção "Solução de Problemas" acima
2. Verifique o [README.md](README.md)
3. Procure nos Issues do GitHub
4. Abra um novo Issue descrevendo o problema

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] pip funcionando
- [ ] Repositório clonado/baixado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Aplicação executando (`python app.py`)
- [ ] Navegador acessando http://localhost:5059
- [ ] Dados atualizados no Dashboard

---

**Instalação concluída! Boa sorte! 🍀**
