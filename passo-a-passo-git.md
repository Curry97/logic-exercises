
# Passo a Passo para Usar o Mesmo Repositório em Dois Computadores

## 📌 1. No seu computador de casa (onde o repositório já existe)

Sempre que terminar uma nova aula:

```
git add .
git commit -m "Adiciona aula nova"
git push
```

Isso envia tudo para o GitHub.

---

## 📌 2. No computador da sala de aula (primeira vez)

Você NÃO precisa copiar arquivos manualmente.

Basta clonar o repositório:

```
git clone https://github.com/SEU-USUARIO/SEU-REPO.git
```

(Depois me diga o link real e eu coloco ele aqui para você.)

Isso cria uma pasta igual à do seu PC de casa.

---

## 📌 3. Depois de editar, criar ou fazer uma aula nova no computador da sala

Entre na pasta clonada e execute:

```
git add .
git commit -m "Adiciona aula nova"
git push
```

---

## 📌 4. Quando voltar para o computador de casa

Antes de continuar trabalhando, sempre execute:

```
git pull
```

Isso sincroniza tudo e baixa o que foi feito na sala.

---

## 🎯 Resumo Rápido

**Computador Casa →** `add` → `commit` → `push`  
**Computador Sala →** `clone` (só na primeira vez)  
Depois → `add` → `commit` → `push`  
**Voltar para Casa →** `git pull`

---

Se quiser, posso colocar o link correto do seu repositório aqui no arquivo.
