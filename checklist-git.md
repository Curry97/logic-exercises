
# Checklist para Usar o Mesmo Repositório em Dois Computadores

## 🏡 Computador de Casa

### Antes de começar:
```
git pull
```

### Depois de fazer uma aula nova ou arquivo novo:
```
git add .
git commit -m "Adiciona aula nova"
git push
```

---

## 🏫 Computador da Sala de Aula

### Primeira vez:
```
git clone LINK_DO_SEU_REPO
```

### Sempre que for usar:
Entre na pasta:
```
cd nome-do-repo
```

Antes de começar:
```
git pull
```

Depois que terminar a aula:
```
git add .
git commit -m "Adiciona aula nova"
git push
```

---

## Regras Importantes

- Sempre use **git pull** antes de começar em qualquer computador.
- Sempre finalize com **git add → commit → push**.
- Nunca mova arquivos manualmente entre computadores.
- O GitHub sempre salva a versão atual do seu projeto.
