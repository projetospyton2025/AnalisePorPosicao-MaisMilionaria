# 🚀 Guia Rápido - Sistema +Milionária

Comece a usar o sistema em **3 minutos**!

## ⚡ Instalação Expressa

```bash
# 1. Clone o repositório
git clone https://github.com/projetospyton2025/AnalisePorPosicao-MaisMilionaria.git
cd AnalisePorPosicao-MaisMilionaria

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute
python app.py
```

Acesse: **http://localhost:5059**

## 📊 Primeiros Passos

### 1. Atualize os Dados (Primeira vez)

```
Dashboard → Botão "🔄 Atualizar Dados"
```

Aguarde alguns minutos para sincronizar todos os concursos.

### 2. Veja as Estatísticas

O Dashboard mostra automaticamente:
- ✅ Último resultado (números + trevos)
- ✅ Top 10 números mais frequentes
- ✅ Top 10 números mais atrasados
- ✅ Frequência e combinações de trevos 🍀

### 3. Gere Seu Primeiro Palpite

```
Gerar Palpites → Escolha "Equilibrada" → Clique em "🎯 Gerar Palpite"
```

## 🎯 Uso Básico

### Gerar Palpite Simples

1. Vá para **"Gerar Palpites"**
2. Mantenha as configurações padrão:
   - Estratégia: **Equilibrada**
   - Números: **6**
   - Trevos: **2**
3. Clique em **"🎯 Gerar Palpite"**

### Sugerir Trevos Automaticamente

1. Na página de Palpites
2. Clique em **"🍀 Sugerir Trevos Automaticamente"**
3. O sistema sugere os melhores trevos baseado em estatísticas

### Atualizar Dados Regularmente

**Recomendado**: Atualize antes de cada jogo

```
Dashboard → "🔄 Atualizar Dados" → Aguarde confirmação
```

## 🎲 Estratégias Rápidas

| Estratégia | Quando Usar |
|------------|-------------|
| **Equilibrada** | Uso geral (recomendado) |
| **Agressiva** | Confia nos números quentes |
| **Conservadora** | Aposta nos atrasados |
| **Combinações de Trevos** | Foca em trevos históricos |

## 💡 Dicas Rápidas

✅ **Sempre atualize** os dados antes de gerar palpites  
✅ **Trevos são importantes** - Não ignore as sugestões  
✅ **Experimente estratégias** - Cada uma tem seu estilo  
✅ **Veja as estatísticas** - Entenda os padrões  
✅ **Jogue com responsabilidade** - É um jogo de probabilidades  

## ⚙️ Configurações Opcionais

### Mudar a Porta

Edite `.env`:
```
PORT=5059  # Mude para outra porta se necessário
```

### Modo Debug

Desabilite em produção:
```
DEBUG=False
```

## 🔧 Solução de Problemas

### Erro: "Módulo não encontrado"
```bash
pip install -r requirements.txt
```

### Erro: "Porta já em uso"
```bash
# Mude a porta no .env ou use:
python app.py  # O sistema tentará outra porta
```

### Erro: "Não foi possível conectar à API"
```bash
# Verifique sua conexão com a internet
# A API da Caixa pode estar temporariamente indisponível
```

## 📱 Acesso Remoto

Para acessar de outros dispositivos na mesma rede:

1. Configure no `.env`:
```
HOST=0.0.0.0
```

2. Acesse de outro dispositivo:
```
http://[SEU_IP]:5059
```

## 🎓 Próximos Passos

1. ✅ Explore as **Estatísticas** no Dashboard
2. ✅ Teste diferentes **Estratégias** de palpites
3. ✅ Use **"Sugerir Trevos"** para otimizar jogos
4. ✅ Leia o **README.md** completo para recursos avançados

## 📚 Documentação Completa

- **[README.md](README.md)** - Documentação completa
- **[DOWNLOAD.md](DOWNLOAD.md)** - Instalação detalhada
- **[ONDE-ESTAO-ARQUIVOS.md](ONDE-ESTAO-ARQUIVOS.md)** - Estrutura do projeto

## 🆘 Precisa de Ajuda?

1. Verifique o [README.md](README.md)
2. Veja os Issues no GitHub
3. Abra uma nova Issue

---

**Boa sorte! 🍀**
