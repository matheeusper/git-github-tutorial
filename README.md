# Tutorial de Git e GitHub

Este é um projeto de exemplo para aprender a usar o Git e GitHub. Aqui você encontrará um guia passo a passo sobre como trabalhar com controle de versão.

## Índice
1. [Configuração Inicial](#configuração-inicial)
2. [Comandos Básicos](#comandos-básicos)
3. [Trabalhando com Branches](#trabalhando-com-branches)
4. [Pull Requests](#pull-requests)
5. [Boas Práticas](#boas-práticas)

## Configuração Inicial

### 1. Instalar o Git
- Baixe o Git para Windows em: https://git-scm.com/download/win
- Ou use o comando: `winget install --id Git.Git -e --source winget`

### 2. Configurar suas credenciais
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### 3. Criar um Token de Acesso no GitHub
1. Acesse GitHub.com e faça login
2. Vá em Settings > Developer settings > Personal access tokens
3. Clique em "Generate new token (classic)"
4. Dê um nome ao token
5. Selecione as permissões necessárias (pelo menos 'repo')
6. Copie o token gerado (você só verá ele uma vez!)

## Comandos Básicos

### Iniciar um Projeto
```bash
# Criar um novo diretório
mkdir meu-projeto
cd meu-projeto

# Inicializar o Git
git init

# Adicionar arquivos
git add .

# Criar um commit
git commit -m "Primeiro commit"

# Conectar com o GitHub
git remote add origin https://seu-token@github.com/seu-usuario/seu-repositorio.git

# Enviar para o GitHub
git push -u origin master
```

### Trabalhando com Alterações
```bash
# Ver status das alterações
git status

# Adicionar alterações
git add nome-do-arquivo

# Criar um commit
git commit -m "Descrição das alterações"

# Enviar para o GitHub
git push
```

## Trabalhando com Branches

### Criar e Usar Branches
```bash
# Criar uma nova branch
git checkout -b nome-da-branch

# Mudar para uma branch existente
git checkout nome-da-branch

# Ver todas as branches
git branch

# Enviar uma nova branch para o GitHub
git push -u origin nome-da-branch
```

## Pull Requests

### Criar um Pull Request
1. Faça alterações em uma branch
2. Envie as alterações para o GitHub
3. No GitHub, clique em "Compare & pull request"
4. Dê um título e descrição ao PR
5. Clique em "Create pull request"
6. Clique em "Merge pull request"

### Atualizar após um Merge
```bash
# Atualizar a branch principal
git checkout master
git pull

# Remover a branch local após o merge
git branch -d nome-da-branch
```

## Boas Práticas

1. **Commits**
   - Faça commits frequentes
   - Use mensagens claras e descritivas
   - Um commit por funcionalidade/correção

2. **Branches**
   - Use branches para novas funcionalidades
   - Mantenha a branch master sempre estável
   - Delete branches após o merge

3. **Pull Requests**
   - Revise seu código antes de criar um PR
   - Escreva descrições claras
   - Responda a comentários e faça ajustes quando necessário

## Recursos Adicionais

- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## Contribuição

Sinta-se à vontade para contribuir com este projeto! Você pode:
1. Reportar erros
2. Sugerir melhorias
3. Adicionar mais conteúdo ao tutorial
4. Corrigir erros de digitação 