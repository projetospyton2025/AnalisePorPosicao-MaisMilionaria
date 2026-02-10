# 🔄 Guia de Migração - Criando Repositório Separado

Este guia explica como criar um novo repositório Git para a Dupla Sena a partir do diretório `AnalisePorPosicao-DuplaSena`.

## Por que Separar?

A Dupla Sena é uma **modalidade completamente independente** da +Milionária, com:
- Regras de jogo diferentes
- Estrutura de premiação diferente  
- Dois sorteios independentes
- API própria

Ter um repositório separado permite:
- Desenvolvimento independente
- Versionamento separado
- Deploy independente
- Manutenção mais fácil

## Opção 1: Criar Novo Repositório no GitHub

### Passo 1: Criar Repositório no GitHub

1. Acesse [github.com](https://github.com)
2. Clique em "New repository"
3. Nome sugerido: `AnalisePorPosicao-DuplaSena`
4. Descrição: "Sistema de análise estatística para Dupla Sena"
5. Escolha público ou privado
6. **NÃO** inicialize com README (já temos um)
7. Clique em "Create repository"

### Passo 2: Preparar o Diretório Local

```bash
# Navegue até o diretório da Dupla Sena
cd AnalisePorPosicao-DuplaSena

# Inicialize um novo repositório Git
git init

# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "Initial commit - Sistema de Análise Dupla Sena"
```

### Passo 3: Conectar ao Repositório Remoto

```bash
# Adicione o repositório remoto (substitua YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/AnalisePorPosicao-DuplaSena.git

# Envie o código
git branch -M main
git push -u origin main
```

### Passo 4: Verificar

1. Acesse seu repositório no GitHub
2. Verifique se todos os arquivos foram enviados
3. Confirme que o README.md está sendo exibido

## Opção 2: Extrair do Repositório Atual

Se você quiser manter o histórico do Git:

### Usando git filter-branch

```bash
# Clone o repositório original
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria.git
cd AnalisePorPosicao-MaisMilionaria

# Extraia apenas o diretório Dupla Sena
git filter-branch --prune-empty --subdirectory-filter AnalisePorPosicao-DuplaSena main

# Adicione novo remote
git remote set-url origin https://github.com/YOUR-USERNAME/AnalisePorPosicao-DuplaSena.git

# Push
git push -u origin main
```

### Usando git subtree

```bash
# No repositório original
cd AnalisePorPosicao-MaisMilionaria

# Extraia o subdiretório para uma nova branch
git subtree split -P AnalisePorPosicao-DuplaSena -b duplasena-only

# Crie um novo diretório para o novo repositório
cd ..
mkdir AnalisePorPosicao-DuplaSena-repo
cd AnalisePorPosicao-DuplaSena-repo

# Inicialize e puxe da branch extraída
git init
git pull ../AnalisePorPosicao-MaisMilionaria duplasena-only

# Adicione remote e push
git remote add origin https://github.com/YOUR-USERNAME/AnalisePorPosicao-DuplaSena.git
git branch -M main
git push -u origin main
```

## Estrutura Final do Novo Repositório

```
AnalisePorPosicao-DuplaSena/
├── README.md                  # Documentação principal
├── INSTALACAO.md              # Guia de instalação
├── .gitignore                 # Arquivos ignorados
├── .env.example               # Exemplo de configuração
├── app.py                     # Aplicação Flask
├── config.py                  # Configurações
├── requirements.txt           # Dependências
├── run_duplasena.py           # Script de execução
├── models/                    # Modelos de dados
│   ├── __init__.py
│   └── duplasena_model.py
├── services/                  # Serviços de negócio
│   ├── __init__.py
│   ├── api_duplasena_service.py
│   ├── duplasena_service.py
│   └── estatistica_duplasena_service.py
├── routes/                    # Rotas da API
│   ├── __init__.py
│   └── duplasena_routes.py
├── static/                    # Arquivos estáticos
└── templates/                 # Templates HTML
```

## Configuração Pós-Migração

### 1. Atualizar README.md

Adicione a URL correta do repositório:
```markdown
git clone https://github.com/YOUR-USERNAME/AnalisePorPosicao-DuplaSena.git
```

### 2. Configurar GitHub Actions (Opcional)

Crie `.github/workflows/tests.yml` para CI/CD:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Test import
        run: python -c "from app import app; print('OK')"
```

### 3. Adicionar Tags de Release

```bash
git tag -a v1.0.0 -m "Primeira versão independente da Dupla Sena"
git push origin v1.0.0
```

### 4. Configurar Proteção de Branch

No GitHub:
1. Settings → Branches
2. Add rule para `main`
3. Marque "Require pull request reviews"

## Manutenção Futura

### Sincronizar Melhorias

Se houver melhorias no repositório original que você queira trazer:

```bash
# Adicione o repositório original como remote
git remote add upstream https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria.git

# Busque mudanças
git fetch upstream

# Faça cherry-pick de commits específicos
git cherry-pick <commit-hash>
```

### Deploy Independente

Agora você pode fazer deploy da Dupla Sena independentemente:

```bash
# Heroku
heroku create duplasena-api
git push heroku main

# DigitalOcean App Platform
doctl apps create --spec app.yaml

# Railway
railway init
railway up
```

## Checklist de Migração

- [ ] Repositório criado no GitHub
- [ ] Código commitado localmente
- [ ] Remote configurado
- [ ] Código enviado para GitHub
- [ ] README.md revisado e atualizado
- [ ] .gitignore configurado
- [ ] Requirements.txt testado
- [ ] Aplicação testada localmente
- [ ] Tags de versão adicionadas
- [ ] Documentação completa
- [ ] CI/CD configurado (opcional)

## Problemas Comuns

### Erro: "remote origin already exists"

```bash
git remote remove origin
git remote add origin <nova-url>
```

### Arquivos grandes no histórico

Use git-filter-repo para limpar:
```bash
pip install git-filter-repo
git-filter-repo --path-glob '*.db' --invert-paths
```

### Credenciais Git

Configure suas credenciais:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

## Suporte

Para problemas durante a migração:
1. Verifique a documentação do Git
2. Consulte o GitHub Docs
3. Abra uma issue no repositório

---

**Boa sorte com o novo repositório independente! 🎲**
