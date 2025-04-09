# 🚀 Tutorial Completo de Git e GitHub

Este é um guia completo e detalhado para aprender Git e GitHub, desde o básico até conceitos avançados. Este tutorial foi desenvolvido para ajudar tanto iniciantes quanto usuários intermediários a dominarem o controle de versão.

<div align="center">
  <img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" alt="Git Logo" width="200"/>
  <br>
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="100"/>
</div>

## 📑 Índice
1. [Introdução ao Controle de Versão](#-introdução-ao-controle-de-versão)
2. [Configuração Inicial](#-configuração-inicial)
3. [Comandos Básicos](#-comandos-básicos)
4. [Trabalhando com Branches](#-trabalhando-com-branches)
5. [Colaboração com GitHub](#-colaboração-com-github)
6. [Gerenciamento Avançado](#-gerenciamento-avançado)
7. [Fluxos de Trabalho](#-fluxos-de-trabalho)
8. [Resolução de Problemas](#-resolução-de-problemas)
9. [Exemplo Prático](#-exemplo-prático)
10. [Boas Práticas](#-boas-práticas)
11. [Recursos Adicionais](#-recursos-adicionais)

## 📘 Introdução ao Controle de Versão

### O que é Git?
Git é um sistema de controle de versão distribuído que permite:
- Rastrear mudanças no código
- Trabalhar em equipe de forma eficiente
- Manter diferentes versões do projeto
- Reverter alterações quando necessário

### Por que usar Git?
- **Histórico completo**: Mantenha todo o histórico de alterações
- **Trabalho em equipe**: Permite que várias pessoas trabalhem no mesmo projeto
- **Branches**: Desenvolvimento paralelo de funcionalidades
- **Segurança**: Backup distribuído do código
- **Rastreabilidade**: Saiba quem fez cada alteração e quando

## ⚙️ Configuração Inicial

### 1. Instalação do Git

#### Windows
```bash
# Opção 1: Baixar o instalador
# Acesse: https://git-scm.com/download/win

# Opção 2: Usar o winget
winget install --id Git.Git -e --source winget
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install git
```

#### macOS
```bash
# Com Homebrew
brew install git
```

### 2. Configuração Inicial do Git
```bash
# Configurar nome de usuário
git config --global user.name "Seu Nome"

# Configurar email
git config --global user.email "seu.email@exemplo.com"

# Configurar editor padrão (opcional)
git config --global core.editor "code --wait"  # Para VS Code

# Verificar configurações
git config --list
```

### 3. Configuração do GitHub

#### Criar Conta no GitHub
1. Acesse [GitHub.com](https://github.com)
2. Clique em "Sign up"
3. Preencha as informações necessárias

#### Configurar Autenticação

##### Método 1: Token de Acesso Pessoal (Recomendado)
1. Acesse GitHub.com e faça login
2. Vá em Settings > Developer settings > Personal access tokens > Tokens (classic)
3. Clique em "Generate new token (classic)"
4. Nome sugerido: "Git Local Access"
5. Selecione as permissões:
   - repo
   - workflow
   - write:packages
   - delete:packages
   - admin:org
   - admin:public_key
6. Gere o token e guarde-o em local seguro

##### Método 2: Chave SSH
```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu.email@exemplo.com"

# Copiar chave pública
# Windows
type %userprofile%\.ssh\id_ed25519.pub

# Linux/macOS
cat ~/.ssh/id_ed25519.pub
```

Depois, adicione a chave em GitHub > Settings > SSH and GPG keys

## 🔧 Comandos Básicos

### Iniciando um Projeto

```bash
# Criar diretório do projeto
mkdir meu-projeto
cd meu-projeto

# Inicializar repositório Git
git init

# Verificar status
git status
```

### Ciclo Básico do Git

#### 1. Modificar Arquivos
```bash
# Criar arquivo de exemplo
echo "# Meu Projeto" > README.md
```

#### 2. Preparar Alterações (Staging)
```bash
# Adicionar arquivo específico
git add README.md

# Adicionar todos os arquivos
git add .

# Verificar status
git status
```

#### 3. Commit das Alterações
```bash
# Criar commit com mensagem
git commit -m "Primeiro commit: Adiciona README"

# Commit com descrição detalhada
git commit -m "Título do commit" -m "Descrição detalhada do que foi feito"
```

### Histórico e Logs

```bash
# Ver histórico de commits
git log

# Ver histórico resumido
git log --oneline

# Ver histórico com gráfico
git log --graph --oneline --all

# Ver alterações em um arquivo
git log -p README.md
```

## 🌳 Trabalhando com Branches

### Conceitos Básicos

```bash
# Listar branches
git branch

# Criar nova branch
git branch feature-nova

# Criar e mudar para nova branch
git checkout -b feature-nova

# Mudar de branch
git checkout main

# Ver branches remotas
git branch -r
```

### Mesclando Branches

```bash
# Mesclar branch feature na main
git checkout main
git merge feature-nova

# Mesclar com commit específico
git merge --no-ff feature-nova
```

### Resolvendo Conflitos

1. Quando ocorrer um conflito, você verá:
```bash
<<<<<<< HEAD
# código da branch atual
=======
# código da outra branch
>>>>>>> feature-nova
```

2. Para resolver:
   - Abra o arquivo
   - Escolha qual código manter
   - Remova os marcadores de conflito
   - Salve o arquivo
   - Adicione e faça commit

```bash
# Após resolver manualmente
git add .
git commit -m "Resolve conflitos na merge da feature-nova"
```

## 🤝 Colaboração com GitHub

### Conectando ao GitHub

```bash
# Adicionar repositório remoto
git remote add origin https://github.com/seu-usuario/seu-repo.git

# Verificar remotos configurados
git remote -v

# Enviar código para GitHub
git push -u origin main
```

### Trabalhando com Repositório Remoto

```bash
# Baixar alterações
git fetch origin

# Baixar e mesclar alterações
git pull origin main

# Enviar alterações
git push origin main

# Clonar repositório existente
git clone https://github.com/usuario/repositorio.git
```

### Fluxo de Trabalho com Pull Requests

1. Criar branch para nova feature
```bash
git checkout -b feature/nova-funcionalidade
```

2. Fazer alterações e commits
```bash
git add .
git commit -m "Implementa nova funcionalidade"
```

3. Enviar branch para GitHub
```bash
git push origin feature/nova-funcionalidade
```

4. No GitHub:
   - Clique em "Compare & pull request"
   - Preencha título e descrição
   - Adicione revisores se necessário
   - Clique em "Create pull request"

5. Após aprovação:
   - Clique em "Merge pull request"
   - Confirme o merge
   - Delete a branch remota

6. Atualizar local
```bash
git checkout main
git pull origin main
git branch -d feature/nova-funcionalidade
```

## 🛠️ Gerenciamento Avançado

### Stash

```bash
# Guardar alterações temporariamente
git stash

# Listar stashes
git stash list

# Aplicar último stash
git stash pop

# Aplicar stash específico
git stash apply stash@{2}
```

### Tags

```bash
# Criar tag anotada
git tag -a v1.0.0 -m "Versão 1.0.0"

# Listar tags
git tag

# Enviar tags para GitHub
git push origin --tags
```

### Reset e Revert

```bash
# Desfazer último commit mantendo alterações
git reset --soft HEAD~1

# Desfazer último commit descartando alterações
git reset --hard HEAD~1

# Criar novo commit que desfaz alterações
git revert HEAD
```

## 🔄 Fluxos de Trabalho

### GitFlow
- `main`: Código em produção
- `develop`: Desenvolvimento
- `feature/*`: Novas funcionalidades
- `release/*`: Preparação para release
- `hotfix/*`: Correções urgentes

### GitHub Flow
1. Criar branch da main
2. Adicionar commits
3. Abrir Pull Request
4. Discussão e revisão
5. Deploy
6. Merge

## 🔍 Resolução de Problemas

### Problemas Comuns

```bash
# Corrigir último commit
git commit --amend

# Remover arquivo do staging
git restore --staged arquivo.txt

# Descartar alterações locais
git restore arquivo.txt

# Ver quem alterou cada linha
git blame arquivo.txt
```

## 💻 Exemplo Prático

Vamos criar um projeto Python com funções estatísticas como exemplo:

1. Inicializar projeto
```bash
mkdir projeto-estatistica
cd projeto-estatistica
git init
```

2. Criar arquivo principal
```python
# main.py
def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    if not numeros:
        return 0
    numeros_ordenados = sorted(numeros)
    meio = len(numeros_ordenados) // 2
    if len(numeros_ordenados) % 2 == 0:
        return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    return numeros_ordenados[meio]
```

3. Adicionar e commitar
```bash
git add main.py
git commit -m "Adiciona funções básicas de estatística"
```

4. Criar branch para nova funcionalidade
```bash
git checkout -b feature/desvio-padrao
```

5. Adicionar nova função
```python
def calcular_desvio_padrao(numeros):
    if not numeros:
        return 0
    media = calcular_media(numeros)
    variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)
    return variancia ** 0.5
```

6. Commitar e enviar alterações
```bash
git add main.py
git commit -m "Adiciona função de desvio padrão"
git push origin feature/desvio-padrao
```

## 📝 Boas Práticas

### Commits
- Faça commits pequenos e frequentes
- Use mensagens claras e descritivas
- Siga o padrão: "tipo: descrição"
  - feat: nova funcionalidade
  - fix: correção de bug
  - docs: documentação
  - style: formatação
  - refactor: refatoração
  - test: testes
  - chore: tarefas diversas

### Branches
- Use prefixos descritivos:
  - feature/: novas funcionalidades
  - bugfix/: correções
  - hotfix/: correções urgentes
  - release/: preparação para release
- Mantenha branches atualizadas
- Delete branches após merge

### Segurança
- Nunca comite senhas ou chaves
- Use .gitignore para arquivos sensíveis
- Revise código antes de commits
- Faça backup regularmente

## 📚 Recursos Adicionais

- [Documentação Oficial do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Oh My Git!](https://ohmygit.org/) - Jogo para aprender Git
- [Learn Git Branching](https://learngitbranching.js.org/) - Tutorial interativo

## 🤝 Contribuição

Se você encontrou um erro ou quer melhorar este tutorial:
1. Faça um fork do repositório
2. Crie uma branch para sua contribuição
3. Faça suas alterações
4. Envie um pull request

---

<div align="center">
  <p>Feito com ❤️ para ajudar desenvolvedores a dominarem Git e GitHub</p>
</div>