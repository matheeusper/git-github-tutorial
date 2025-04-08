# 🚀 Tutorial Completo de Git e GitHub

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
4. [Colaboração com GitHub](#-colaboração-com-github)
5. [Gerenciamento Avançado](#-gerenciamento-avançado)
6. [Exemplo Prático](#-exemplo-prático)
7. [Boas Práticas](#-boas-práticas)
8. [Recursos Adicionais](#-recursos-adicionais)

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
```

### Trabalhando com Alterações
```bash
# Ver status das alterações
git status

# Adicionar alterações
git add nome-do-arquivo

# Criar um commit
git commit -m "Descrição das alterações"
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
```

### Resolvendo Conflitos
1. Quando houver conflitos, você verá algo assim:
```python
<<<<<<< HEAD
seu código aqui
=======
código do outro desenvolvedor aqui
>>>>>>> master
```

2. Para resolver:
   - Abra o arquivo com conflito
   - Escolha qual código manter
   - Remova as linhas de marcação (<<<<<<< HEAD, =======, >>>>>>> master)
   - Salve o arquivo

3. Depois de resolver:
```bash
git add arquivo-com-conflito
git commit -m "Resolvendo conflitos"
```

## 🤝 Colaboração com GitHub

### Conectando seu Projeto ao GitHub
```bash
# Conectar com o GitHub
git remote add origin https://seu-token@github.com/seu-usuario/seu-repositorio.git

# Enviar para o GitHub
git push -u origin master
```

### Trabalhando com Repositórios Remotos
```bash
# Atualizar seu repositório local
git pull origin master

# Enviar alterações para o GitHub
git push origin master

# Enviar uma nova branch para o GitHub
git push -u origin nome-da-branch
```

### Pull Requests
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

## 🛠️ Gerenciamento Avançado

### Verificar e Limpar Branches
```bash
# Ver branches locais
git branch

# Ver todas as branches (locais e remotas)
git branch -a

# Deletar branch local
git branch -d nome-da-branch

# Forçar deleção de branch local
git branch -D nome-da-branch

# Deletar branch remota
git push origin --delete nome-da-branch
```

### Tags e Versões
```bash
# Criar uma tag anotada
git tag -a v1.0.0 -m "Primeira versão estável"

# Listar todas as tags
git tag

# Ver detalhes de uma tag
git show v1.0.0

# Enviar tags para o GitHub
git push origin v1.0.0
```

### Versionamento Semântico
- v1.0.0 (Major.Minor.Patch)
  - Major: Mudanças incompatíveis
  - Minor: Novas funcionalidades compatíveis
  - Patch: Correções de bugs

## 💻 Exemplo Prático

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
    notas = [7.5, 8.0, 9.0, 6.5]
    media = calcular_media(notas)
    print(f"As notas são: {notas}")
    print(f"A média é: {media:.2f}")
```

### 2. Criar uma branch para nova funcionalidade
```bash
git checkout -b feature-nova-funcionalidade
```

### 3. Adicionar novas funções
```python
def calcular_mediana(numeros):
    """
    Calcula a mediana de uma lista de números
    """
    if not numeros:
        return 0
    numeros_ordenados = sorted(numeros)
    meio = len(numeros_ordenados) // 2
    if len(numeros_ordenados) % 2 == 0:
        return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    return numeros_ordenados[meio]
```

### 4. Commitar e enviar alterações
```bash
git add main.py
git commit -m "Adicionando função para calcular mediana"
git push -u origin feature-nova-funcionalidade
```

### 5. Criar e mesclar Pull Request
1. No GitHub, crie um Pull Request
2. Revise as alterações
3. Mescle o PR
4. Delete a branch após o merge

## 📝 Boas Práticas

### Commits
- Faça commits frequentes
- Use mensagens claras e descritivas
- Um commit por funcionalidade/correção

### Branches
- Use branches para novas funcionalidades
- Mantenha a branch master sempre estável
- Delete branches após o merge
- Mantenha apenas branches ativas
- Use nomes descritivos para branches

### Pull Requests
- Revise seu código antes de criar um PR
- Escreva descrições claras
- Responda a comentários e faça ajustes quando necessário

### Versionamento
- Use tags para marcar versões importantes
- Siga o versionamento semântico
- Mantenha um changelog atualizado

## 📚 Recursos Adicionais

- [Documentação oficial do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Versionamento Semântico](https://semver.org/)

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