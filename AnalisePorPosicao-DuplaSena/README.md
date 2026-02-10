# 🎲 Sistema de Análise por Posição - DUPLA SENA

## Repositório Independente da Dupla Sena

Sistema completo de análise estatística e geração de palpites inteligentes para a loteria **DUPLA SENA** da Caixa Econômica Federal.

**Este é um repositório INDEPENDENTE e AUTÔNOMO para a modalidade Dupla Sena.**

## 📋 Características da Dupla Sena

A Dupla Sena é única porque possui **DOIS SORTEIOS INDEPENDENTES**:
- **Sorteio 1**: 6 números (01-50)
- **Sorteio 2**: 6 números (01-50)
- Você pode ganhar em **AMBOS** os sorteios com o mesmo jogo!

### Funcionalidades Principais

✅ **API REST Completa**
- Integração com API oficial da Caixa
- Atualização automática de resultados
- Estatísticas separadas para cada sorteio

✅ **Análise Estatística Dupla**
- **Sorteio 1**: Frequência, atrasos, pares/ímpares, distribuição por faixas
- **Sorteio 2**: Frequência, atrasos, pares/ímpares, distribuição por faixas
- **Estatísticas Gerais**: Análise combinada dos dois sorteios

✅ **Gerador de Palpites Inteligentes**
- 5 estratégias diferentes (equilibrada, agressiva, conservadora, atrasados, por_faixa)
- Baseado em análise estatística de ambos os sorteios
- Geração de múltiplos jogos

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone este repositório:
```bash
git clone <repository-url>
cd AnalisePorPosicao-DuplaSena
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. (Opcional) Configure variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env se necessário
```

4. Execute a aplicação:
```bash
python app.py
```

Ou use o script de execução:
```bash
python run_duplasena.py
```

5. Acesse no navegador:
```
http://localhost:5060
```

## 📡 API REST

A API está disponível em: `http://localhost:5060/api/duplasena/*`

### Endpoints Principais

#### Atualizar Base de Dados
```bash
POST /api/duplasena/atualizar
Content-Type: application/json
{
  "concurso_inicial": 1
}
```

#### Gerar Palpites
```bash
POST /api/duplasena/gerar-palpite
Content-Type: application/json
{
  "estrategia": "equilibrada",
  "quantidade_numeros": 6,
  "quantidade_jogos": 1
}
```

#### Estatísticas dos Sorteios
```bash
GET /api/duplasena/estatisticas/sorteio/1
GET /api/duplasena/estatisticas/sorteio/2
GET /api/duplasena/estatisticas/gerais
```

#### Último Resultado
```bash
GET /api/duplasena/ultimo-resultado
```

#### Conferir Jogo
```bash
POST /api/duplasena/conferir
Content-Type: application/json
{
  "numeros": [5, 12, 23, 34, 41, 48],
  "concurso": 2825
}
```

## 🎯 Estratégias de Palpites

| Estratégia | Descrição |
|------------|-----------|
| **equilibrada** | Mix de números frequentes e atrasados |
| **agressiva** | Foca nos números mais sorteados |
| **conservadora** | Prioriza números atrasados |
| **atrasados** | Apenas números com maior atraso |
| **por_faixa** | Distribui entre faixas (01-10, 11-20, etc) |

## 🏆 Sistema de Premiação

A Dupla Sena possui 4 faixas de premiação **por sorteio**:

| Faixa | Acertos | Prêmio |
|-------|---------|--------|
| 1 | 6 números (Sena) | **Prêmio Principal** |
| 2 | 5 números (Quina) | Prêmio Secundário |
| 3 | 4 números (Quadra) | Prêmio |
| 4 | 3 números (Terno) | Prêmio |

**IMPORTANTE**: Você pode ganhar em **AMBOS** os sorteios com o mesmo jogo!

## 📊 Exemplos de Uso

### Python

```python
import requests

# Gerar palpite
response = requests.post('http://localhost:5060/api/duplasena/gerar-palpite', json={
    'estrategia': 'equilibrada',
    'quantidade_numeros': 6,
    'quantidade_jogos': 1
})
print(response.json())

# Buscar estatísticas do sorteio 1
response = requests.get('http://localhost:5060/api/duplasena/estatisticas/sorteio/1')
print(response.json())
```

### JavaScript

```javascript
// Gerar palpite
fetch('http://localhost:5060/api/duplasena/gerar-palpite', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        estrategia: 'equilibrada',
        quantidade_numeros: 6,
        quantidade_jogos: 2
    })
})
.then(res => res.json())
.then(data => console.log(data.jogos));
```

### cURL

```bash
# Atualizar base de dados
curl -X POST http://localhost:5060/api/duplasena/atualizar-ultimos \
  -H "Content-Type: application/json" \
  -d '{"quantidade": 50}'

# Gerar palpites
curl -X POST http://localhost:5060/api/duplasena/gerar-palpite \
  -H "Content-Type: application/json" \
  -d '{"estrategia": "agressiva", "quantidade_numeros": 6}'
```

## 🔧 Configuração

### Variáveis de Ambiente

Edite o arquivo `.env`:

```env
# Porta do servidor
PORT=5060

# Debug mode
DEBUG=True

# Caminho do banco de dados
DATABASE_PATH_DUPLASENA=duplasena.db

# URL da API da Caixa
API_DUPLASENA_URL=https://servicebus2.caixa.gov.br/portaldeloterias/api/duplasena
```

## 🗂️ Estrutura do Projeto

```
AnalisePorPosicao-DuplaSena/
├── app.py                          # Aplicação Flask principal
├── config.py                       # Configurações
├── requirements.txt                # Dependências Python
├── .env.example                   # Exemplo de variáveis de ambiente
├── .gitignore                     # Arquivos ignorados pelo Git
├── run_duplasena.py               # Script de execução
├── models/                        # Modelos de dados
│   ├── __init__.py
│   └── duplasena_model.py         # Model com dois sorteios
├── services/                      # Lógica de negócio
│   ├── __init__.py
│   ├── api_duplasena_service.py   # Integração com API da Caixa
│   ├── estatistica_duplasena_service.py  # Estatísticas
│   └── duplasena_service.py       # Geração de palpites
├── routes/                        # Rotas da API
│   ├── __init__.py
│   └── duplasena_routes.py        # Endpoints REST
├── static/                        # Arquivos estáticos
└── templates/                     # Templates HTML
```

## 💡 Dicas de Uso

1. **Atualize a base de dados regularmente**: Use o endpoint `/api/duplasena/atualizar-ultimos` para manter os dados atualizados
2. **Experimente diferentes estratégias**: Cada estratégia tem características únicas
3. **Analise os dois sorteios**: As estatísticas são calculadas separadamente para cada sorteio
4. **Combine com análise manual**: Use as estatísticas para embasar suas escolhas

## 🔒 Segurança

- Dados obtidos apenas da API oficial da Caixa
- Sem armazenamento de dados pessoais
- Código open source para auditoria
- Use HTTPS em produção
- Altere o `SECRET_KEY` em produção

## 🐳 Deploy com Docker (Opcional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5060
CMD ["python", "app.py"]
```

Build e Run:
```bash
docker build -t duplasena:latest .
docker run -p 5060:5060 duplasena:latest
```

## 📝 Licença

Este projeto é disponibilizado como está, para fins educacionais e de análise estatística.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## ⚠️ Aviso Legal

Este sistema é apenas para análise estatística e entretenimento. Não há garantia de ganhos. Jogue com responsabilidade.

---

**Desenvolvido com 💜 para a comunidade de análise de loterias**
