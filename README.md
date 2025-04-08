# 🚀 Tutorial de Git e GitHub

Este é um projeto de exemplo para aprender a usar o Git e GitHub. Aqui você encontrará um guia passo a passo sobre como trabalhar com controle de versão.

<div align="center">
  <img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" alt="Git Logo" width="200"/>
  <br>
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="100"/>
</div>

## 📑 Índice
1. [Configuração Inicial](#-configuração-inicial)
2. [Comandos Básicos](#-comandos-básicos)
3. [Trabalhando com Branches](#-trabalhando-com-branches)
4. [Pull Requests](#-pull-requests)
5. [Exemplo Prático](#-exemplo-prático)
6. [Boas Práticas](#-boas-práticas)

## ⚙️ Configuração Inicial

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

## 🔧 Comandos Básicos

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

## 🌳 Trabalhando com Branches

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

## 🔄 Pull Requests

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

## 💻 Exemplo Prático

Vamos criar um projeto Python simples para demonstrar o fluxo de trabalho com Git e GitHub.

### 1. Criar um arquivo Python
Crie um arquivo chamado `main.py` com o seguinte conteúdo:

```python
def calcular_media(numeros):
    """
    Calcula a média de uma lista de números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

# Exemplo de uso
if __name__ == "__main__":
    # Lista de exemplo
    notas = [7.5, 8.0, 9.0, 6.5]
    
    # Calculando a média
    media = calcular_media(notas)
    
    # Mostrando o resultado
    print(f"As notas são: {notas}")
    print(f"A média é: {media:.2f}")
```

### 2. Criar um arquivo de dependências
Crie um arquivo chamado `requirements.txt`:

```
numpy==1.24.0
pandas==2.0.0
```

### 3. Adicionar e commitar os arquivos
```bash
# Adicionar os arquivos
git add main.py requirements.txt

# Criar um commit
git commit -m "Adicionando arquivos Python de exemplo"

# Enviar para o GitHub
git push
```

### 4. Criar uma nova branch para uma funcionalidade
```bash
# Criar e mudar para uma nova branch
git checkout -b feature-nova-funcionalidade

# Fazer alterações no código
# Adicionar e commitar as alterações
git add .
git commit -m "Adicionando nova funcionalidade"

# Enviar a branch para o GitHub
git push -u origin feature-nova-funcionalidade
```

### 5. Criar um Pull Request
1. Vá para o GitHub
2. Clique em "Compare & pull request"
3. Dê um título e descrição ao PR
4. Clique em "Create pull request"
5. Clique em "Merge pull request"

## 📝 Boas Práticas

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

## 📚 Recursos Adicionais

- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## 🤝 Contribuição

Sinta-se à vontade para contribuir com este projeto! Você pode:
1. Reportar erros
2. Sugerir melhorias
3. Adicionar mais conteúdo ao tutorial
4. Corrigir erros de digitação

---

<div align="center">
  <p>Feito com ❤️ para ajudar desenvolvedores iniciantes</p>
</div> 