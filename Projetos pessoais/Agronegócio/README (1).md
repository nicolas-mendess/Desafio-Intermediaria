# 🌾 Gestão Agronegócios

> Sistema de gestão rural para pecuaristas de corte — do terminal Python a uma Progressive Web App.

![Status](https://img.shields.io/badge/status-ativo-brightgreen)
![Versão](https://img.shields.io/badge/versão-2.0-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![HTML](https://img.shields.io/badge/HTML5%20%2F%20CSS3%20%2F%20JS-Vanilla-orange)
![Licença](https://img.shields.io/badge/licença-MIT-green)

---

## 📌 Índice

[Sobre o Projeto](#-sobre-o-projeto)
[Versões](#-versões)
 - [v1.0 — MVP Python (Terminal)](#v10--mvp-python-terminal)
 - [v2.0 — Progressive Web App](#v20--progressive-web-app)
[Estrutura do Repositório](#-estrutura-do-repositório)
[Como Executar](#-como-executar)
[Tecnologias](#-tecnologias)


---

## 📖 Sobre o Projeto

O **Gestão Agronegócios** nasceu como projeto acadêmico de 1º semestre e evoluiu para uma aplicação web instalável. O sistema resolve um problema real do pequeno pecuarista: tomar decisões rápidas no campo sem precisar de planilhas ou conexão com internet.

**Dois módulos principais:**

| Módulo | O que resolve |
|---|---|
| 💰 Gestão Financeira | Calcula lucro/prejuízo da operação e exibe o status de saúde financeira |
| ⚖️ Pesagem e Nutrição | Verifica se o animal atingiu o peso ideal e, se não, aciona automaticamente o plano de nutrição com custo estimado |

---

## 🔄 Versões

### v1.0 — MVP Python (Terminal)

Primeira versão entregue como trabalho acadêmico de 1º semestre. Desenvolvida com recursos básicos de Python, sem uso de bibliotecas, funções, classes ou dicionários, sem o uso de bibliotecas, funções, classes, listas ou dicionários. A aplicação executa um menu interativo no terminal por meio de um laço while True e utiliza apenas estruturas de controle básicas como if/elif/else, input(), print(), float() e break para implementar um Módulo de Gestão Financeira e um Módulo de Pesagem e Nutrição com lógica condicional encadeada, podendo ser executado diretamente com o comando python main.py.
### v1.0 — Python
| Recurso | Uso |
|---|---|
| `while True` | Mantém o menu ativo |
| `if / elif / else` | Lógica de negócio e condicionais |
| `input()` + `float()` | Captura e conversão de dados |
| `print()` + f-strings | Saída formatada no terminal |


### v2.0 — Progressive Web App

Refatoração completa para uma Single Page Application instalável no celular, com suporte offline via Service Worker.

**Arquivo principal:** `index.html`  
**Arquivos de suporte:** `manifest.json`, `service-worker.js`

**O que foi adicionado nesta versão:**

| Recurso | Descrição |
|---|---|
| Tab Bar inferior | Navegação nativa estilo app mobile |
| Validação inline | Erros exibidos abaixo de cada campo, sem `alert()` |
| `localStorage` | Últimos valores preenchidos são restaurados automaticamente |
| Service Worker | Cache offline — funciona sem internet no campo |
| `manifest.json` | Instalável como app no Android e iOS (PWA) |
| `inputmode="decimal"` | Teclado numérico nativo no celular |
| `safe-area-inset` | Suporte a notch e barra de gestos do iPhone |
| Banner de instalação | Aparece automaticamente no Chrome/Android |

**Deploy no GitHub Pages:**
1. Faça upload de `index.html`, `manifest.json` e `service-worker.js` na raiz do repositório
2. Vá em **Settings → Pages → Branch: main → Save**
3. Acesse `https://seu-usuario.github.io/nome-do-repositorio`

---

### Versão Web (v2.0)

**Opção 1 — Direto no navegador:**
Abra o arquivo `index.html` diretamente no Chrome ou Edge.

**Opção 2 — GitHub Pages (recomendado):**
```
https://seu-usuario.github.io/gestao-agronegocios
```

**Opção 3 — Servidor local:**
```bash
# Com Python
python -m http.server 8000

# Com Node.js
npx serve .
```

> Para o Service Worker funcionar corretamente, é necessário rodar via servidor HTTP (opções 2 ou 3), não pelo protocolo `file://`.

---

## 🛠️ Tecnologia

### v2.0 — Web
| Tecnologia | Uso |
|---|---|
| HTML5 | Estrutura da SPA |
| CSS3 (Variáveis + Flexbox) | Layout mobile-first e temas |
| JavaScript Vanilla | Lógica, navegação e DOM |
| Web App Manifest | Instalação como PWA |
| Service Worker | Funcionamento offline |
| localStorage | Persistência leve de dados |

---

Desenvolvido como projeto acadêmico do 1º semestre estruturado em um único arquivo em Python, depois aprimorado do terminal para uma experiência visual acessível com acessibilidade em navegadores e dispositivos móveis, com Interface gráfica responsiva, desacoplamento da lógica de negócio.

---
