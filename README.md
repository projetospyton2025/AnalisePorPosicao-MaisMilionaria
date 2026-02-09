# 🍀 Sistema de Análise por Posição - +MILIONÁRIA

Sistema completo de análise estatística e geração de palpites inteligentes para a loteria **+MILIONÁRIA** da Caixa Econômica Federal.

![+Milionária Logo](https://i.postimg.cc/DywMFvD1/mais-Milionaria.png)

## 📋 Características

### O Diferencial da +Milionária

A +Milionária é ÚNICA porque combina DOIS elementos independentes:
- **6 Números (01-50)** - Análise estatística tradicional
- **2 Trevos (1-6) 🍀** - Elemento exclusivo com análise SEPARADA

### Funcionalidades Principais

✅ **Dashboard Completo**
- Visualização do último resultado (números + trevos)
- Estatísticas em tempo real
- 10 faixas de premiação

✅ **Análise Estatística Dupla**
- **Números**: Frequência, atrasos, pares/ímpares, distribuição por faixas
- **Trevos**: Frequência individual, combinações mais comuns, análise de padrões

✅ **Gerador de Palpites Inteligentes**
- 7 estratégias diferentes (equilibrada, agressiva, conservadora, etc)
- Sugestão automática de trevos baseada em dados reais
- Geração de múltiplos jogos

✅ **Integração com API Oficial**
- Dados sempre atualizados da Caixa
- Histórico completo de concursos

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria.git
cd AnalisePorPosicao-MaisMilionaria
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

5. Acesse no navegador:
```
http://localhost:5059
```

## 📖 Documentação Completa

- **[QUICKSTART.md](QUICKSTART.md)** - Guia rápido de uso
- **[DOWNLOAD.md](DOWNLOAD.md)** - Instruções detalhadas de instalação
- **[ONDE-ESTAO-ARQUIVOS.md](ONDE-ESTAO-ARQUIVOS.md)** - Mapa do projeto

## 🎯 Como Usar

### 1. Atualizar Base de Dados

Primeiro, atualize a base de dados com os resultados mais recentes:

```
1. Acesse o Dashboard
2. Clique no botão "🔄 Atualizar Dados"
3. Aguarde a sincronização com a API da Caixa
```

### 2. Visualizar Estatísticas

No Dashboard você encontra:
- **Último resultado** com números e trevos destacados
- **Estatísticas de números**: mais frequentes, mais atrasados, distribuição par/ímpar
- **Estatísticas de trevos**: frequência individual e combinações mais comuns

### 3. Gerar Palpites

```
1. Acesse "Gerar Palpites"
2. Escolha uma estratégia
3. Defina quantidade de números (6-12) e trevos (2-6)
4. Clique em "🎯 Gerar Palpite"
5. Use "🍀 Sugerir Trevos Automaticamente" para sugestões baseadas em dados
```

### Estratégias Disponíveis

| Estratégia | Descrição |
|------------|-----------|
| **Equilibrada** | Mix balanceado de números frequentes e atrasados |
| **Agressiva** | Foca nos números e trevos mais sorteados |
| **Conservadora** | Prioriza números e trevos atrasados |
| **Mista** | Variação aleatória entre diferentes abordagens |
| **Atrasados** | Apenas números com maior atraso |
| **Por Faixa** | Distribui uniformemente entre faixas (01-10, 11-20, etc) |
| **Combinações de Trevos** | Usa pares de trevos mais frequentes |

## 🏆 Sistema de Premiação

A +Milionária possui 10 faixas de premiação:

| Faixa | Acertos | Prêmio |
|-------|---------|--------|
| 1 | 6 números + 2 trevos | **Prêmio Principal** |
| 2 | 6 números + 1 ou 0 trevos | Prêmio Secundário |
| 3 | 5 números + 2 trevos | Prêmio |
| 4 | 5 números + 1 ou 0 trevos | Prêmio |
| 5 | 4 números + 2 trevos | Prêmio |
| 6 | 4 números + 1 ou 0 trevos | Prêmio |
| 7 | 3 números + 2 trevos | Prêmio |
| 8 | 3 números + 1 trevo | Prêmio |
| 9 | 2 números + 2 trevos | Prêmio |
| 10 | 2 números + 1 trevo | Prêmio |

## 🔧 Estrutura do Projeto

```
AnalisePorPosicao-MaisMilionaria/
├── app.py                      # Aplicação Flask principal
├── config.py                   # Configurações
├── requirements.txt            # Dependências
├── .env.example               # Exemplo de variáveis de ambiente
├── models/                    # Modelos de dados
│   ├── __init__.py
│   └── resultado_model.py     # Model com números E trevos
├── services/                  # Lógica de negócio
│   ├── __init__.py
│   ├── api_caixa_service.py   # Integração com API oficial
│   ├── estatistica_service.py # Estatísticas separadas
│   └── maismilionaria_service.py # Geração de palpites
├── routes/                    # Rotas
│   ├── __init__.py
│   ├── main_routes.py         # Rotas HTML
│   └── api_routes.py          # API REST
├── templates/                 # Templates HTML
│   ├── base.html
│   ├── index.html             # Dashboard
│   └── palpites.html          # Gerador de palpites
└── static/                    # Arquivos estáticos
    ├── css/
    │   └── styles.css         # Tema roxo #31357C
    └── js/
        └── scripts.js         # Lógica frontend
```

## 🎨 Design

- **Cor Principal**: #31357C (roxo escuro)
- **Cor Secundária**: #a9cf46 (verde dos trevos)
- **Logo Oficial**: https://i.postimg.cc/DywMFvD1/mais-Milionaria.png
- **Ícone Especial**: 🍀 para representar trevos

## 📡 API REST

### Endpoints Disponíveis

```
POST   /api/atualizar              # Atualiza base de dados
POST   /api/atualizar-ultimos      # Atualiza últimos N concursos
GET    /api/ultimo-resultado       # Retorna último resultado
GET    /api/resultados             # Lista resultados
GET    /api/resultado/<numero>     # Resultado específico
GET    /api/estatisticas           # Estatísticas completas
GET    /api/estatisticas/numeros   # Apenas números
GET    /api/estatisticas/trevos    # Apenas trevos
GET    /api/sugerir-trevos         # Sugere 2 trevos
POST   /api/gerar-palpite          # Gera palpites
POST   /api/conferir               # Confere jogo
```

### Exemplo de Uso da API

```javascript
// Gerar palpite
fetch('/api/gerar-palpite', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        estrategia: 'equilibrada',
        quantidade_numeros: 6,
        quantidade_trevos: 2
    })
})
.then(res => res.json())
.then(data => console.log(data.jogos));

// Sugerir trevos
fetch('/api/sugerir-trevos?estrategia=frequentes')
.then(res => res.json())
.then(data => console.log(data.trevos)); // [3, 6]
```

## 💡 Dicas Importantes

1. **Trevos são essenciais**: Para o prêmio principal, é necessário acertar 6 números + 2 trevos
2. **Atualize regularmente**: Mantenha a base de dados sempre atualizada
3. **Use estatísticas**: As análises separadas de números e trevos aumentam a precisão
4. **Experimente estratégias**: Cada estratégia tem características únicas
5. **Jogue com responsabilidade**: Loterias são jogos de probabilidade

## 🔒 Segurança

- Dados obtidos apenas da API oficial da Caixa
- Sem armazenamento de dados pessoais
- Código open source para auditoria

## 📝 Licença

Este projeto é disponibilizado como está, para fins educacionais e de análise estatística.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação
2. Procure em issues existentes
3. Abra uma nova issue se necessário

## ⚠️ Aviso Legal

Este sistema é apenas para análise estatística e entretenimento. Não há garantia de ganhos. Jogue com responsabilidade.

---

**Desenvolvido com 💜 para a comunidade de análise de loterias**
