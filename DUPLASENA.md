# 🎲 Sistema de Análise por Posição - DUPLA SENA

Sistema completo de análise estatística e geração de palpites inteligentes para a loteria **DUPLA SENA** da Caixa Econômica Federal.

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

### Instalação

O sistema Dupla Sena está integrado ao sistema principal. Siga as instruções do [README.md](README.md) principal para instalar.

### Executar a Aplicação

```bash
python app.py
```

O servidor estará disponível em: `http://localhost:5059`

## 📡 API REST - Dupla Sena

Todos os endpoints da Dupla Sena estão sob o prefixo `/api/duplasena/`

### Endpoints Disponíveis

#### Atualizar Base de Dados

```bash
POST /api/duplasena/atualizar
Content-Type: application/json

{
  "concurso_inicial": 1
}
```

#### Atualizar Últimos Concursos

```bash
POST /api/duplasena/atualizar-ultimos
Content-Type: application/json

{
  "quantidade": 10
}
```

#### Buscar Último Resultado

```bash
GET /api/duplasena/ultimo-resultado
```

Resposta:
```json
{
  "sucesso": true,
  "resultado": {
    "numero": 2825,
    "dataApuracao": "2024-02-03",
    "listaDezenasSorteio1": [5, 12, 23, 34, 41, 48],
    "listaDezenasSorteio2": [7, 15, 28, 32, 39, 45],
    "acumulado": false
  }
}
```

#### Listar Resultados

```bash
GET /api/duplasena/resultados?limite=100
```

#### Buscar Resultado Específico

```bash
GET /api/duplasena/resultado/{numero}
```

#### Estatísticas Completas

```bash
GET /api/duplasena/estatisticas
```

Retorna estatísticas de ambos sorteios e estatísticas gerais.

#### Estatísticas de Sorteio Específico

```bash
GET /api/duplasena/estatisticas/sorteio/1
GET /api/duplasena/estatisticas/sorteio/2
```

#### Estatísticas Gerais

```bash
GET /api/duplasena/estatisticas/gerais
```

#### Gerar Palpite

```bash
POST /api/duplasena/gerar-palpite
Content-Type: application/json

{
  "estrategia": "equilibrada",
  "quantidade_numeros": 6,
  "quantidade_jogos": 3
}
```

Estratégias disponíveis:
- `equilibrada`: Mix de números frequentes e atrasados
- `agressiva`: Foca nos números mais sorteados
- `conservadora`: Prioriza números atrasados
- `atrasados`: Apenas números com maior atraso
- `por_faixa`: Distribui entre faixas (01-10, 11-20, etc)

Resposta:
```json
{
  "sucesso": true,
  "estrategia": "equilibrada",
  "jogos": [
    {
      "numeros": [5, 12, 23, 34, 41, 48]
    },
    {
      "numeros": [7, 15, 28, 32, 39, 45]
    }
  ]
}
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

Resposta:
```json
{
  "sucesso": true,
  "concurso": 2825,
  "sorteio1": {
    "acertos": 6,
    "faixa": 1,
    "premiado": true,
    "numeros_sorteados": [5, 12, 23, 34, 41, 48]
  },
  "sorteio2": {
    "acertos": 2,
    "faixa": 0,
    "premiado": false,
    "numeros_sorteados": [7, 15, 28, 32, 39, 45]
  }
}
```

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
response = requests.post('http://localhost:5059/api/duplasena/gerar-palpite', json={
    'estrategia': 'equilibrada',
    'quantidade_numeros': 6,
    'quantidade_jogos': 1
})
palpite = response.json()
print(palpite['jogos'][0]['numeros'])

# Buscar estatísticas
response = requests.get('http://localhost:5059/api/duplasena/estatisticas/sorteio/1')
stats = response.json()
print(stats['estatisticas']['frequencia'][:10])  # Top 10 números mais frequentes
```

### JavaScript

```javascript
// Gerar palpite
fetch('http://localhost:5059/api/duplasena/gerar-palpite', {
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

// Conferir jogo
fetch('http://localhost:5059/api/duplasena/conferir', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        numeros: [5, 12, 23, 34, 41, 48],
        concurso: 2825
    })
})
.then(res => res.json())
.then(data => {
    console.log('Sorteio 1:', data.sorteio1.acertos, 'acertos');
    console.log('Sorteio 2:', data.sorteio2.acertos, 'acertos');
});
```

### cURL

```bash
# Atualizar base de dados
curl -X POST http://localhost:5059/api/duplasena/atualizar-ultimos \
  -H "Content-Type: application/json" \
  -d '{"quantidade": 50}'

# Gerar palpites
curl -X POST http://localhost:5059/api/duplasena/gerar-palpite \
  -H "Content-Type: application/json" \
  -d '{"estrategia": "agressiva", "quantidade_numeros": 6, "quantidade_jogos": 5}'

# Ver estatísticas
curl http://localhost:5059/api/duplasena/estatisticas/gerais
```

## 🔧 Estrutura do Projeto

```
AnalisePorPosicao-MaisMilionaria/
├── models/
│   ├── duplasena_model.py       # Model com dois sorteios
├── services/
│   ├── api_duplasena_service.py # Integração com API oficial
│   ├── estatistica_duplasena_service.py # Estatísticas separadas
│   └── duplasena_service.py     # Geração de palpites
├── routes/
│   └── duplasena_routes.py      # API REST
└── duplasena.db                 # Banco de dados SQLite
```

## 💡 Dicas Importantes

1. **Dois Sorteios**: Lembre-se que você pode ganhar em ambos os sorteios!
2. **Atualize Regularmente**: Mantenha a base de dados sempre atualizada
3. **Use Estatísticas**: As análises separadas aumentam a precisão
4. **Experimente Estratégias**: Cada estratégia tem características únicas
5. **Jogue com Responsabilidade**: Loterias são jogos de probabilidade

## 🔒 Segurança

- Dados obtidos apenas da API oficial da Caixa
- Sem armazenamento de dados pessoais
- Código open source para auditoria

## ⚠️ Aviso Legal

Este sistema é apenas para análise estatística e entretenimento. Não há garantia de ganhos. Jogue com responsabilidade.

---

**Desenvolvido com 💜 para a comunidade de análise de loterias**
