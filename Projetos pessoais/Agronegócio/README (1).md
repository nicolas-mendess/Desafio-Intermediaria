# 🌾 Gestão Agronegócios

> Sistema de gestão rural para pecuaristas de corte — do terminal Python a uma Progressive Web App.

---

## 📌 Índice

- [Sobre o Projeto]
- [Versões]
 - [v1.0 — MVP Python (Terminal)]
 - [v2.0 — Progressive Web App]
- [Estrutura do Repositório]
- [Como Executar]
- [Tecnologias]


---

## 📖 Sobre o Projeto

O **Gestão Agronegócios** nasceu como projeto acadêmico de 1º semestre e evoluiu para uma aplicação web instalável. O sistema resolve um problema real do pequeno pecuarista: tomar decisões rápidas no campo sem precisar de planilhas ou conexão com internet.

Problema que resolve: o pequeno pecuarista não tem ferramenta simples para tomar decisões rápidas no campo — quanto vale o boi hoje, se está pronto para venda e quanto vai custar engordá-lo até o peso ideal
Público-alvo: produtor rural de baixa familiaridade tecnológica, usando smartphone no curral, sob sol forte
Princípio de design: alto contraste, botões grandes, zero complexidade desnecessária, resultados imediatos na tel

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



---

### Versão Web (v2.0)

## 🛠️ Tecnologia

| Tecnologia | Uso |
|---|---|
| HTML5 | Estrutura da SPA |
| CSS3 (Variáveis + Flexbox) | Layout mobile-first e temas |
| JavaScript Vanilla | Lógica, navegação e DOM |
| Web App Manifest | Instalação como PWA |
| Service Worker | Funcionamento offline |
| localStorage | Persistência leve de dados |

---
Versão 2.0 — SPA Web 🚧 Em andamento

Refatoração completa para index.html único (HTML5 + CSS3 + JS Vanilla)
Toda a lógica Python traduzida para JavaScript (parseFloat, toLocaleString para BRL)
Design mobile-first com fonte DM Serif Display + DM Sans, paleta verde #0d3318 / #1f5c1f
Navegação SPA: 3 telas (home, financeiro, pesagem) trocadas via navigate() sem reload
Animação fadeIn em cada troca de tela e em cada resultado
Deploy previsto: GitHub Pages (repositório com index.html na raiz)


### Próximos Passos — Fase Front-end Web

Validação de inputs mais robusta: impedir valores negativos, mostrar erros inline (abaixo do campo) em vez de alert()
Persistência leve: salvar os últimos valores usados via localStorage para o produtor não redigitar tudo
Histórico de cálculos: exibir os últimos 3–5 resultados numa secção "Histórico" na Home
Módulo Boi na Balança integrado como terceira opção no menu (cálculo de arrobas + cotação)
Modo offline / PWA: adicionar manifest.json e um Service Worker básico para o app funcionar sem internet no campo
Acessibilidade: aria-labels nos inputs, contraste revisado com WCAG AA
README atualizado com screenshots da SPA e instruções de deploy no GitHub Pages

Desenvolvido como projeto acadêmico do 1º semestre estruturado em um único arquivo em Python, depois aprimorado do terminal para uma experiência visual acessível com acessibilidade em navegadores e dispositivos móveis, com Interface gráfica responsiva, desacoplamento da lógica de negócio.

---
