# 🎯 Guia de Uso - Modalidades Separadas

## Visão Geral

Este sistema possui **DUAS MODALIDADES COMPLETAMENTE SEPARADAS**:

1. **+Milionária** - Aplicação independente (porta 5059)
2. **Dupla Sena** - Aplicação independente (porta 5060)

Cada modalidade funciona de forma autônoma, com:
- ✅ Aplicação própria
- ✅ Porta própria
- ✅ Banco de dados próprio
- ✅ Configuração independente

## 🚀 Como Executar

### Executar APENAS +Milionária

```bash
# Opção 1
python app.py

# Opção 2
python run_maismilionaria.py
```

**Porta**: 5059  
**URL**: http://localhost:5059  
**API**: http://localhost:5059/api/*

### Executar APENAS Dupla Sena

```bash
# Opção 1
python app_duplasena.py

# Opção 2
python run_duplasena.py
```

**Porta**: 5060  
**URL**: http://localhost:5060  
**API**: http://localhost:5060/api/duplasena/*

### Executar AMBAS Simultaneamente

Você pode executar as duas modalidades ao mesmo tempo!

```bash
# Terminal 1 - +Milionária
python app.py

# Terminal 2 - Dupla Sena (em outro terminal)
python app_duplasena.py
```

**+Milionária**: http://localhost:5059  
**Dupla Sena**: http://localhost:5060

## 📊 Comparação das Modalidades

| Característica | +Milionária | Dupla Sena |
|----------------|-------------|------------|
| **Aplicação** | `app.py` | `app_duplasena.py` |
| **Porta Padrão** | 5059 | 5060 |
| **Database** | `database.db` | `duplasena.db` |
| **Config** | `ConfigMaisMilionaria` | `ConfigDuplaSena` |
| **Números** | 6 (01-50) | 6 (01-50) |
| **Elemento Extra** | 2 Trevos (1-6) 🍀 | Nenhum |
| **Sorteios** | 1 sorteio | 2 sorteios independentes |
| **API Base** | `/api/*` | `/api/duplasena/*` |

## 🔧 Configuração

### Configurar Portas Diferentes

Edite o arquivo `.env`:

```env
# +Milionária
PORT_MAISMILIONARIA=5059

# Dupla Sena
PORT_DUPLASENA=5060
```

### Configurar Bancos de Dados Separados

```env
# +Milionária
DATABASE_PATH=database.db

# Dupla Sena
DATABASE_PATH_DUPLASENA=duplasena.db
```

## 📡 Endpoints da API

### +Milionária (Porta 5059)

```bash
# Atualizar dados
POST http://localhost:5059/api/atualizar

# Gerar palpite
POST http://localhost:5059/api/gerar-palpite
Body: {
  "estrategia": "equilibrada",
  "quantidade_numeros": 6,
  "quantidade_trevos": 2
}

# Estatísticas
GET http://localhost:5059/api/estatisticas

# Último resultado
GET http://localhost:5059/api/ultimo-resultado
```

### Dupla Sena (Porta 5060)

```bash
# Atualizar dados
POST http://localhost:5060/api/duplasena/atualizar

# Gerar palpite
POST http://localhost:5060/api/duplasena/gerar-palpite
Body: {
  "estrategia": "equilibrada",
  "quantidade_numeros": 6
}

# Estatísticas do sorteio 1
GET http://localhost:5060/api/duplasena/estatisticas/sorteio/1

# Estatísticas do sorteio 2
GET http://localhost:5060/api/duplasena/estatisticas/sorteio/2

# Último resultado
GET http://localhost:5060/api/duplasena/ultimo-resultado
```

## 💡 Exemplos de Uso

### Exemplo 1: Usar apenas +Milionária

```bash
# Iniciar servidor
python app.py

# Em outro terminal, testar API
curl http://localhost:5059/api/ultimo-resultado
```

### Exemplo 2: Usar apenas Dupla Sena

```bash
# Iniciar servidor
python app_duplasena.py

# Em outro terminal, testar API
curl http://localhost:5060/api/duplasena/ultimo-resultado
```

### Exemplo 3: Usar ambas ao mesmo tempo

```bash
# Terminal 1
python app.py

# Terminal 2
python app_duplasena.py

# Terminal 3 - Teste +Milionária
curl -X POST http://localhost:5059/api/gerar-palpite \
  -H "Content-Type: application/json" \
  -d '{"estrategia":"equilibrada","quantidade_numeros":6,"quantidade_trevos":2}'

# Terminal 3 - Teste Dupla Sena
curl -X POST http://localhost:5060/api/duplasena/gerar-palpite \
  -H "Content-Type: application/json" \
  -d '{"estrategia":"equilibrada","quantidade_numeros":6}'
```

## 🐳 Deploy com Docker (Opcional)

Se você quiser fazer deploy de ambas as modalidades com Docker:

### +Milionária

```dockerfile
# Dockerfile.maismilionaria
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5059
CMD ["python", "app.py"]
```

```bash
docker build -f Dockerfile.maismilionaria -t maismilionaria:latest .
docker run -p 5059:5059 maismilionaria:latest
```

### Dupla Sena

```dockerfile
# Dockerfile.duplasena
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5060
CMD ["python", "app_duplasena.py"]
```

```bash
docker build -f Dockerfile.duplasena -t duplasena:latest .
docker run -p 5060:5060 duplasena:latest
```

### Docker Compose (ambas juntas)

```yaml
# docker-compose.yml
version: '3.8'
services:
  maismilionaria:
    build:
      context: .
      dockerfile: Dockerfile.maismilionaria
    ports:
      - "5059:5059"
    volumes:
      - ./database.db:/app/database.db
    
  duplasena:
    build:
      context: .
      dockerfile: Dockerfile.duplasena
    ports:
      - "5060:5060"
    volumes:
      - ./duplasena.db:/app/duplasena.db
```

```bash
docker-compose up -d
```

## ❓ FAQ

### Por que separar as modalidades?

Cada loteria tem suas características únicas e merece uma aplicação dedicada. Isso permite:
- Maior flexibilidade de deploy
- Melhor isolamento de recursos
- Escalabilidade independente
- Manutenção mais fácil

### Posso rodar ambas na mesma máquina?

Sim! As portas são diferentes (5059 e 5060), então não há conflito.

### Os bancos de dados são compartilhados?

Não. Cada modalidade tem seu próprio banco de dados SQLite:
- +Milionária: `database.db`
- Dupla Sena: `duplasena.db`

### Preciso instalar dependências separadas?

Não. O `requirements.txt` é compartilhado pelas duas modalidades.

### Como escolher qual usar?

Depende do seu caso de uso:
- **Apenas +Milionária**: Use `app.py`
- **Apenas Dupla Sena**: Use `app_duplasena.py`
- **Ambas**: Execute os dois scripts em terminais diferentes

## 📚 Documentação Adicional

- **+Milionária**: [README.md](README.md)
- **Dupla Sena**: [DUPLASENA.md](DUPLASENA.md)
- **Download**: [DOWNLOAD.md](DOWNLOAD.md)
- **Quickstart**: [QUICKSTART.md](QUICKSTART.md)

---

**💜 Desenvolvido com carinho para análise de loterias**
