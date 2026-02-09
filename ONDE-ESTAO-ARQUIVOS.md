# 🗺️ Onde Estão os Arquivos - Mapa do Projeto

Guia completo da estrutura do projeto Sistema de Análise +Milionária.

## 📁 Estrutura Geral

```
AnalisePorPosicao-MaisMilionaria/
├── 📄 Arquivos de Configuração
├── 📊 Banco de Dados
├── 🐍 Código Python
│   ├── 📦 Models (Dados)
│   ├── ⚙️ Services (Lógica)
│   └── 🌐 Routes (Rotas)
├── 🎨 Frontend
│   ├── 📝 Templates (HTML)
│   └── 🎨 Static (CSS/JS)
└── 📚 Documentação
```

## 📄 Arquivos Raiz

### Arquivos Principais

| Arquivo | Descrição | Quando Modificar |
|---------|-----------|------------------|
| `app.py` | 🚀 Aplicação Flask principal | Raramente (só configurações avançadas) |
| `config.py` | ⚙️ Configurações do sistema | Customizações de regras |
| `requirements.txt` | 📦 Dependências Python | Ao adicionar novas bibliotecas |

### Arquivos de Configuração

| Arquivo | Descrição | Quando Modificar |
|---------|-----------|------------------|
| `.env.example` | 📋 Exemplo de variáveis de ambiente | Template - não modificar |
| `.env` | 🔐 Suas configurações (criado por você) | Personalizar porta, debug, etc |
| `.gitignore` | 🚫 Arquivos ignorados pelo Git | Ao adicionar novos tipos de arquivo |

### Arquivos de Documentação

| Arquivo | Descrição | Para Que Serve |
|---------|-----------|----------------|
| `README.md` | 📖 Documentação completa | Entender todo o sistema |
| `QUICKSTART.md` | 🚀 Guia rápido | Começar em 3 minutos |
| `DOWNLOAD.md` | 📥 Instruções de instalação | Instalar e configurar |
| `ONDE-ESTAO-ARQUIVOS.md` | 🗺️ Este arquivo | Navegar no projeto |

## 📊 Banco de Dados

| Arquivo | Descrição | Observações |
|---------|-----------|-------------|
| `database.db` | 💾 SQLite com resultados | Criado automaticamente na 1ª execução |

**Localização**: Raiz do projeto

**Conteúdo**:
- Tabela `resultados` com todos os concursos
- Números sorteados (6 por concurso)
- Trevos sorteados (2 por concurso)
- Dados de premiação (10 faixas)

## 🐍 Código Python

### `/models` - Camada de Dados

| Arquivo | Responsabilidade | Principais Funções |
|---------|------------------|-------------------|
| `__init__.py` | Inicialização do módulo | - |
| `resultado_model.py` | 💾 **Acesso ao banco de dados** | `inserir_resultado()`, `buscar_resultado()`, `listar_resultados()` |

**Quando modificar**: Ao adicionar novos campos ao banco ou mudar estrutura

### `/services` - Lógica de Negócio

| Arquivo | Responsabilidade | Principais Funções |
|---------|------------------|-------------------|
| `__init__.py` | Inicialização do módulo | - |
| `api_caixa_service.py` | 🌐 **Integração com API da Caixa** | `buscar_ultimo_concurso()`, `atualizar_base_dados()` |
| `estatistica_service.py` | 📊 **Cálculos estatísticos** | `calcular_frequencia_numeros()`, `calcular_frequencia_trevos()` |
| `maismilionaria_service.py` | 🎲 **Geração de palpites** | `gerar_palpite()`, `sugerir_trevos()`, `conferir_jogo()` |

**Quando modificar**:
- `api_caixa_service.py`: Se a API da Caixa mudar
- `estatistica_service.py`: Para adicionar novos tipos de análise
- `maismilionaria_service.py`: Para criar novas estratégias de palpites

### `/routes` - Rotas da Aplicação

| Arquivo | Responsabilidade | Endpoints |
|---------|------------------|-----------|
| `__init__.py` | Inicialização do módulo | - |
| `main_routes.py` | 🌐 **Rotas HTML** | `/`, `/palpites` |
| `api_routes.py` | 📡 **API REST** | `/api/estatisticas`, `/api/gerar-palpite`, etc |

**Quando modificar**:
- `main_routes.py`: Para adicionar novas páginas
- `api_routes.py`: Para adicionar novos endpoints da API

## 🎨 Frontend

### `/templates` - Templates HTML

| Arquivo | Página | Conteúdo Principal |
|---------|--------|-------------------|
| `base.html` | 🏗️ **Template base** | Header, navegação, footer |
| `index.html` | 🏠 **Dashboard** | Último resultado, estatísticas |
| `palpites.html` | 🎲 **Gerador de palpites** | Formulário e resultados |

**Quando modificar**:
- `base.html`: Mudanças globais (menu, rodapé)
- `index.html`: Adicionar/remover seções do dashboard
- `palpites.html`: Mudar interface do gerador

### `/static/css` - Estilos

| Arquivo | Responsabilidade | Principais Estilos |
|---------|------------------|-------------------|
| `styles.css` | 🎨 **Todo o visual** | Tema roxo, cards, botões, tabelas |

**Variáveis CSS principais**:
```css
--primary-color: #31357C    /* Roxo +Milionária */
--secondary-color: #a9cf46  /* Verde trevos */
--accent-color: #FFD700     /* Ouro prêmios */
```

**Quando modificar**: Para personalizar cores, fontes, layouts

### `/static/js` - JavaScript

| Arquivo | Responsabilidade | Principais Funções |
|---------|------------------|-------------------|
| `scripts.js` | 💻 **Toda lógica frontend** | `gerarPalpite()`, `carregarEstatisticas()`, `sugerirTrevos()` |

**Principais funcionalidades**:
- Consumo da API REST
- Renderização dinâmica de resultados
- Interações do usuário

**Quando modificar**: Para adicionar novas interações ou melhorar UX

## 🎯 Fluxo de Dados

### 1. Atualização de Dados

```
Usuário → [btn-atualizar] → api_routes.py 
→ api_caixa_service.py → API Caixa 
→ resultado_model.py → database.db
```

### 2. Visualização de Estatísticas

```
Página carrega → scripts.js → /api/estatisticas 
→ api_routes.py → estatistica_service.py 
→ resultado_model.py → database.db
→ Retorna JSON → Renderiza na página
```

### 3. Geração de Palpite

```
Usuário → [form-palpite] → scripts.js 
→ /api/gerar-palpite → api_routes.py 
→ maismilionaria_service.py → estatistica_service.py 
→ resultado_model.py → database.db
→ Retorna palpite → Renderiza na página
```

## 🔍 Encontrar Funcionalidades

### "Onde eu modifico...?"

| O que você quer modificar | Arquivo(s) |
|---------------------------|------------|
| **Cor do tema** | `static/css/styles.css` (variáveis CSS no topo) |
| **Estratégias de palpite** | `services/maismilionaria_service.py` |
| **Cálculos estatísticos** | `services/estatistica_service.py` |
| **Layout das páginas** | `templates/index.html`, `templates/palpites.html` |
| **Estrutura do banco** | `models/resultado_model.py` |
| **URL da API da Caixa** | `config.py` ou `.env` |
| **Porta do servidor** | `config.py` ou `.env` |
| **Novos endpoints API** | `routes/api_routes.py` |
| **Menu de navegação** | `templates/base.html` |
| **Lógica JavaScript** | `static/js/scripts.js` |

## 📝 Checklist de Arquivos

### ✅ Arquivos que DEVEM existir

- [ ] `app.py`
- [ ] `config.py`
- [ ] `requirements.txt`
- [ ] `models/resultado_model.py`
- [ ] `services/api_caixa_service.py`
- [ ] `services/estatistica_service.py`
- [ ] `services/maismilionaria_service.py`
- [ ] `routes/main_routes.py`
- [ ] `routes/api_routes.py`
- [ ] `templates/base.html`
- [ ] `templates/index.html`
- [ ] `templates/palpites.html`
- [ ] `static/css/styles.css`
- [ ] `static/js/scripts.js`

### 📄 Arquivos criados automaticamente

- [ ] `database.db` (na primeira execução)
- [ ] `__pycache__/` (diretórios - ignorados pelo Git)

### 🔐 Arquivos que você cria

- [ ] `.env` (opcional, copiar de `.env.example`)

## 🚫 Arquivos que NÃO devem ser modificados

- `.gitignore` (a menos que saiba o que está fazendo)
- `__init__.py` (geralmente vazios ou apenas imports)
- `.env.example` (é um template)

## 🗂️ Organização por Funcionalidade

### Análise de Números

**Responsável**: `services/estatistica_service.py`

Métodos:
- `calcular_frequencia_numeros()`
- `calcular_atrasos_numeros()`
- `calcular_pares_impares_numeros()`
- `calcular_por_faixa_numeros()`

### Análise de Trevos 🍀

**Responsável**: `services/estatistica_service.py`

Métodos:
- `calcular_frequencia_trevos()`
- `calcular_atrasos_trevos()`
- `calcular_combinacoes_trevos()`
- `calcular_trevos_quentes_frios()`

### Geração de Palpites

**Responsável**: `services/maismilionaria_service.py`

Métodos privados:
- `_gerar_numeros_equilibrados()`
- `_gerar_numeros_agressivos()`
- `_gerar_trevos_frequentes()`
- `_gerar_trevos_combinacao_comum()`

## 💡 Dicas de Navegação

1. **Buscar por texto**: Use `grep` ou busca do editor
   ```bash
   grep -r "calcular_frequencia" .
   ```

2. **Ver estrutura**: Use `tree` (Linux/Mac) ou `dir /s` (Windows)

3. **Entender fluxo**: Comece pelo `app.py`, depois siga para routes

4. **Debug**: Adicione `print()` nos services para acompanhar execução

## 📚 Recursos Adicionais

- [README.md](README.md) - Visão geral e uso
- [QUICKSTART.md](QUICKSTART.md) - Início rápido
- [DOWNLOAD.md](DOWNLOAD.md) - Instalação detalhada

---

**Agora você sabe onde tudo está! 🗺️**
