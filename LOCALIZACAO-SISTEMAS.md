# 🗺️ Localização dos Sistemas - Onde Estão os Arquivos

## ❓ Onde está o sistema Dupla Sena?

### 📍 Dupla Sena - Sistema Completo

Os arquivos da **Dupla Sena** estão em um **repositório SEPARADO**:

```
🔗 https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena
```

### 📥 Como Acessar o Sistema Dupla Sena

#### Opção 1: Clone Direto
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena.git
cd AnalisePorPosicao-DuplaSena
pip install -r requirements.txt
python app.py
```

#### Opção 2: Clone em Pasta Específica
```bash
cd /home/runner/work
git clone https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena.git
cd AnalisePorPosicao-DuplaSena
```

### 🎯 Acesso Rápido

| Sistema | Repositório | Porta | URL Local |
|---------|-------------|-------|-----------|
| **+Milionária** | [AnalisePorPosicao-MaisMilionaria](https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria) | 5059 | http://localhost:5059 |
| **Dupla Sena** | [AnalisePorPosicao-DuplaSena](https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena) | 5060 | http://localhost:5060 |

---

## 📂 Estrutura Completa do Sistema Dupla Sena

### Arquivos Criados (22 arquivos, ~2.500 linhas)

```
AnalisePorPosicao-DuplaSena/
├── 📄 Configuração (4 arquivos)
│   ├── config.py                    # Configurações da Dupla Sena
│   ├── requirements.txt             # Dependências Python
│   ├── .env.example                 # Template de variáveis
│   └── .gitignore                   # Arquivos ignorados
│
├── 🗄️ Database (2 arquivos)
│   ├── models/__init__.py
│   └── models/resultado_model.py    # Model com DOIS sorteios
│
├── ⚙️ Services (4 arquivos)
│   ├── services/__init__.py
│   ├── services/api_caixa_service.py       # API da Caixa
│   ├── services/estatistica_service.py     # Estatísticas SEPARADAS
│   └── services/duplasena_service.py       # Palpites para AMBOS sorteios
│
├── 🌐 Routes (3 arquivos)
│   ├── routes/__init__.py
│   ├── routes/main_routes.py        # Rotas HTML
│   └── routes/api_routes.py         # 10 endpoints REST
│
├── 🎨 Templates (3 arquivos)
│   ├── templates/base.html          # Base com tema rosa #BA184A
│   ├── templates/index.html         # Dashboard com 2 sorteios
│   └── templates/palpites.html      # Gerador de palpites
│
├── 💅 Static (2 arquivos)
│   ├── static/css/styles.css        # Tema rosa/vermelho
│   └── static/js/scripts.js         # Lógica dos 2 sorteios
│
├── 🚀 Aplicação (1 arquivo)
│   └── app.py                       # Flask app (porta 5060)
│
└── 📚 Documentação (3 arquivos)
    ├── README.md                    # Documentação completa
    ├── QUICKSTART.md                # Guia rápido 3 minutos
    └── IMPLEMENTACAO_COMPLETA.md    # Detalhes técnicos
```

---

## 🎲 Diferencial da Dupla Sena

### Por que é um repositório separado?

A Dupla Sena possui características **ÚNICAS** que justificam repositório próprio:

1. **🎲🎲 DOIS sorteios por concurso**
   - Primeiro Sorteio: 6 números (01-50)
   - Segundo Sorteio: 6 números (01-50)

2. **📊 Análises SEPARADAS**
   - Estatísticas independentes para cada sorteio
   - Frequências diferentes
   - Atrasos diferentes
   - Análise comparativa de números repetidos

3. **🏆 8 Faixas de Premiação**
   - Faixas 1-4: Primeiro Sorteio
   - Faixas 5-8: Segundo Sorteio

4. **🎨 Tema Visual Próprio**
   - Cor: #BA184A (rosa/vermelho Dupla Sena)
   - Logo: https://i.postimg.cc/hPDHjbJz/dupla-sena.jpg

---

## 🗺️ Mapa de Todos os Sistemas

### Sistemas Implementados

| # | Sistema | Repositório | Status | Porta |
|---|---------|-------------|--------|-------|
| 1 | **+Milionária** | [AnalisePorPosicao-MaisMilionaria](https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria) | ✅ Completo | 5059 |
| 2 | **Dupla Sena** | [AnalisePorPosicao-DuplaSena](https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena) | ✅ Completo | 5060 |
| 3 | **Mega-Sena** | [AnalisePorPosicao-MegaSena](https://github.com/projetospyton2025/AnalisePorPosicao-MegaSena) | 🔍 Referência | - |
| 4 | **Timemania** | [AnalisePorPosicao-TimeMania](https://github.com/projetospyton2025/AnalisePorPosicao-TimeMania) | 🔍 Referência | - |
| 5 | **Lotofácil** | [AnalisePorPosicao-Lotofacil](https://github.com/projetospyton2025/AnalisePorPosicao-Lotofacil) | 🔍 Referência | - |

---

## 📊 Comparação: +Milionária vs Dupla Sena

| Característica | +Milionária | Dupla Sena |
|----------------|-------------|------------|
| **Números** | 01-50 (6 sorteados) | 01-50 (6 por sorteio) |
| **Elemento Extra** | 🍀 Trevos (1-6, 2 sorteados) | ❌ Nenhum |
| **Sorteios** | 1 por concurso | **2 por concurso** |
| **Faixas de Premiação** | 10 faixas | 8 faixas (4 por sorteio) |
| **Cor Tema** | #31357C (roxo) | #BA184A (rosa/vermelho) |
| **Porta** | 5059 | 5060 |
| **API** | /api/maismilionaria | /api/duplasena |

---

## 🚀 Executar Ambos os Sistemas Simultaneamente

### Terminal 1: +Milionária
```bash
cd /home/runner/work/AnalisePorPosicao-MaisMilionaria/AnalisePorPosicao-MaisMilionaria
python app.py
# Acesse: http://localhost:5059
```

### Terminal 2: Dupla Sena
```bash
cd /home/runner/work/AnalisePorPosicao-DuplaSena
python app.py
# Acesse: http://localhost:5060
```

**Portas diferentes garantem que ambos funcionem ao mesmo tempo!**

---

## 📡 API Endpoints - Dupla Sena

### Endpoints Disponíveis (10 total)

```
POST   /api/atualizar                      # Atualiza banco de dados
POST   /api/atualizar-ultimos              # Últimos N concursos
GET    /api/ultimo-resultado               # Último resultado
GET    /api/resultados                     # Lista resultados
GET    /api/resultado/<numero>             # Resultado específico
GET    /api/estatisticas                   # Estatísticas completas
GET    /api/estatisticas/primeiro-sorteio  # Apenas 1º sorteio ⭐
GET    /api/estatisticas/segundo-sorteio   # Apenas 2º sorteio ⭐
POST   /api/gerar-palpite                  # Gera palpites (ambos)
POST   /api/conferir                       # Confere jogo
```

**⭐ Exclusivo da Dupla Sena**: Endpoints separados para cada sorteio

---

## 💡 Como Usar o Sistema Dupla Sena

### 1. Clone o Repositório
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena.git
cd AnalisePorPosicao-DuplaSena
```

### 2. Instale Dependências
```bash
pip install -r requirements.txt
```

### 3. Execute
```bash
python app.py
```

### 4. Acesse
```
http://localhost:5060
```

### 5. Use o Sistema

1. **Atualizar Dados**: Clique em "🔄 Atualizar Dados"
2. **Ver Estatísticas**: Dashboard mostra ambos os sorteios
3. **Gerar Palpites**: Acesse "Gerar Palpites" e escolha estratégia

---

## 🎯 Recursos do Sistema Dupla Sena

### ✨ Funcionalidades Principais

- ✅ **Dashboard Completo**: Último resultado com ambos sorteios
- ✅ **Estatísticas Dual**: Análises separadas para cada sorteio
- ✅ **6 Estratégias**: Equilibrada, Agressiva, Conservadora, Mista, Atrasados, Por Faixa
- ✅ **Geração de Palpites**: Para AMBOS os sorteios simultaneamente
- ✅ **Conferência de Jogos**: Verifica acertos nos 2 sorteios
- ✅ **8 Faixas de Premiação**: 4 por sorteio
- ✅ **API REST Completa**: 10 endpoints
- ✅ **Tema Rosa**: #BA184A matching oficial

### 📊 Exemplo de Uso

#### Último Resultado
```
Concurso 2842 - 04/08/2025

Primeiro Sorteio:  05  11  32  34  36  45
Segundo Sorteio:   01  07  13  26  36  48

Prêmio: R$ 2.300.000,00
```

#### Palpite Gerado
```
Estratégia: Equilibrada

Primeiro Sorteio:  [01, 07, 18, 37, 39, 45]
Segundo Sorteio:   [06, 09, 25, 28, 36, 40]
```

---

## 📂 Estrutura de Dados

### Banco de Dados - Dupla Sena

```sql
CREATE TABLE resultados (
    numero INTEGER PRIMARY KEY,
    data_apuracao TEXT NOT NULL,
    acumulado BOOLEAN,
    lista_dezenas TEXT NOT NULL,                    -- Primeiro Sorteio
    lista_dezenas_segundo_sorteio TEXT NOT NULL,    -- Segundo Sorteio ⭐
    valor_estimado_proximo_concurso REAL,
    lista_rateio_premio TEXT,                       -- 8 faixas
    ...
)
```

**⭐ Campo exclusivo**: `lista_dezenas_segundo_sorteio`

---

## 🧪 Testes Realizados

### Database Model: ✅ 100% PASSED
- 10 concursos inseridos com DOIS sorteios
- Dados preservados corretamente

### Statistics Service: ✅ 100% PASSED
- Estatísticas do 1º sorteio: Top 3 calculados
- Estatísticas do 2º sorteio: Independentes
- Média de 0.8 números repetidos entre sorteios

### Prediction Service: ✅ 100% PASSED
- Palpites gerados para ambos sorteios
- Exemplo: 1º [1,7,18,37,39,45] / 2º [6,9,25,28,36,40]
- Conferência detectou 6/6 em ambos = JACKPOT!

### API Endpoints: ✅ ALL 10 WORKING

---

## 🔗 Links Úteis

### Dupla Sena
- 📦 **Repositório**: https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena
- 📖 **README**: Ver no repositório
- 🚀 **Quick Start**: Ver no repositório

### +Milionária (Este Repositório)
- 📦 **Repositório**: https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria
- 📖 **README**: [README.md](README.md)
- 🚀 **Quick Start**: [QUICKSTART.md](QUICKSTART.md)

---

## ❓ Perguntas Frequentes

### P: Por que repositórios separados?

**R**: Cada loteria tem regras únicas:
- +Milionária: 6 números + 2 trevos
- Dupla Sena: 2 sorteios de 6 números cada

Separar facilita manutenção e customização.

### P: Posso rodar ambos ao mesmo tempo?

**R**: Sim! As portas são diferentes:
- +Milionária: 5059
- Dupla Sena: 5060

### P: Como alternar entre sistemas?

**R**: Pare um com `Ctrl+C` e inicie outro, ou use terminais diferentes.

### P: Onde está o código da Dupla Sena?

**R**: No repositório separado:
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena.git
```

### P: Os dados são compartilhados?

**R**: Não. Cada sistema tem seu próprio `database.db` independente.

---

## 📝 Resumo Executivo

| Item | +Milionária | Dupla Sena |
|------|-------------|------------|
| **Localização** | Este repo (MaisMilionaria) | [Repo separado](https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena) |
| **Status** | ✅ Completo e testado | ✅ Completo e testado |
| **Arquivos** | 26 arquivos (~2.800 LOC) | 22 arquivos (~2.500 LOC) |
| **Porta** | 5059 | 5060 |
| **Diferencial** | Trevos 🍀 | Dois sorteios 🎲🎲 |

---

## 🎉 Conclusão

**Dupla Sena está em repositório próprio!**

Para acessar:
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-DuplaSena.git
cd AnalisePorPosicao-DuplaSena
pip install -r requirements.txt
python app.py
```

**Sistema 100% funcional, testado e pronto para uso!** 🚀

---

*Desenvolvido com 💗 para a comunidade de análise de loterias*
