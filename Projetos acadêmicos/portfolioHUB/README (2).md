# portfolioHUB

> Portfólio digital profissional de **Nicolas Fernandes Mendes**  
> Desenvolvido para hospedagem no GitHub Pages como parte das diretrizes acadêmicas do curso de Ciência da Computação — UniCEUB (1º Semestre, 2026).

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Demonstração](#demonstração)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar Localmente](#como-executar-localmente)
- [Deploy no GitHub Pages](#deploy-no-github-pages)
- [Seções do Portfólio](#seções-do-portfólio)
- [Personalização](#personalização)
- [Boas Práticas Aplicadas](#boas-práticas-aplicadas)
- [Autor](#autor)
- [Licença](#licença)

---

## Visão Geral

O **portfolioHUB** é um portfólio digital de página única (*single-page*) desenvolvido inteiramente com tecnologias web nativas — HTML5, CSS3 e JavaScript puro — sem dependência de frameworks ou bibliotecas JavaScript externas.

O projeto foi criado para atender às diretrizes acadêmicas do UniCEUB, apresentando de forma estruturada a trajetória, habilidades e projetos do estudante, com foco em usabilidade, acessibilidade e design responsivo.

---

## Demonstração

🔗 **Site publicado:** `https://nicolas-mendess.github.io/portfolioHUB/`

> Substitua pelo link real após ativar o GitHub Pages.

---

## Funcionalidades

- ✅ **Navegação fixa (Sticky Header)** com indicador de seção ativa e efeito de blur ao rolar
- ✅ **Menu hambúrguer** para dispositivos móveis
- ✅ **Animações de entrada** via `IntersectionObserver` (scroll reveal)
- ✅ **Barras de progresso animadas** que disparam ao entrar na viewport
- ✅ **Efeito de digitação** no subtítulo do Hero
- ✅ **Apresentação em slides** embarcada via Google Slides (`<iframe>`)
- ✅ **Links funcionais** para GitHub, LinkedIn e e-mail
- ✅ **Design totalmente responsivo** para mobile, tablet e desktop
- ✅ **Paleta de cores via CSS Custom Properties** (fácil de tematizar)
- ✅ **Zero dependências JavaScript** externas

---

## Estrutura do Projeto

```
portfolioHUB/
│
├── index.html          # Estrutura e conteúdo da página
├── style.css           # Todos os estilos (944 linhas)
├── script.js           # Interatividade (158 linhas)
│
├── assets/             # (criar manualmente)
│   └── foto.jpg        # Foto profissional do autor
│
├── README.md           # Este documento
└── DEPLOY_GUIDE.md     # Guia passo a passo para o GitHub Pages
```

> **Nota:** A pasta `assets/` deve ser criada manualmente e populada com a foto profissional antes do deploy.

---

## Tecnologias Utilizadas

| Tecnologia | Versão / Fonte | Finalidade |
|---|---|---|
| HTML5 | — | Estrutura semântica da página |
| CSS3 | — | Estilização, layout e animações |
| JavaScript (ES6+) | — | Interatividade e comportamento |
| [Google Fonts](https://fonts.google.com) | Playfair Display + DM Sans | Tipografia |
| [Font Awesome](https://fontawesome.com) | 6.5.0 (CDN) | Ícones |
| [Google Slides](https://slides.google.com) | Embed via `<iframe>` | Apresentação de competências |

**Sem frameworks, sem bundlers, sem Node.js** — o projeto roda diretamente no navegador, o que o torna ideal para o GitHub Pages.

---

## Como Executar Localmente

Não é necessária nenhuma instalação. Basta:

**Opção A — Abrir diretamente:**
```
Clique duplo em index.html
```

**Opção B — Servidor local (recomendado para evitar restrições de CORS com o iframe):**

Se tiver o Python instalado:
```bash
# Python 3
python -m http.server 8080

# Acesse: http://localhost:8080
```

Se tiver o VS Code com a extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer):
```
Clique com botão direito em index.html → "Open with Live Server"
```

---

## Deploy no GitHub Pages

> Para instruções detalhadas, consulte o arquivo [`DEPLOY_GUIDE.md`](./DEPLOY_GUIDE.md).

**Resumo dos passos:**

1. Crie um repositório público chamado `portfolioHUB` no GitHub
2. Suba os arquivos (`index.html`, `style.css`, `script.js`, pasta `assets/`)
3. Vá em **Settings → Pages**
4. Em *Source*, selecione branch `main` e pasta `/ (root)`
5. Clique em **Save** e aguarde ~2 minutos

**URL resultante:**
```
https://<seu-usuario>.github.io/portfolioHUB/
```

---

## Seções do Portfólio

O site é dividido em 4 seções principais, acessíveis pelo menu de navegação:

### 01 · Perfil Pessoal
Apresentação pessoal com biografia, localização e links de contato (e-mail, LinkedIn, GitHub). Reserva espaço para foto profissional.

### 02 · Currículo Digital
Timeline com formação acadêmica (UniCEUB e Colégio Militar de Brasília), atividades complementares (Monitoria de TI), habilidades técnicas com tags, idiomas com barras de nível e certificações da Cisco Networking Academy.

### 03 · Projetos
Cards de projetos acadêmicos com descrição e links para repositórios no GitHub. Inclui aviso de projetos em desenvolvimento.

### 04 · Habilidades & Competências
Quatro áreas de competência com barras de progresso animadas (Desenvolvimento Web, Git/GitHub, Cibersegurança/Hardware, Inglês) mais apresentação em slides incorporada via Google Slides.

---

## Personalização

### Trocar a foto de perfil

1. Salve sua foto como `assets/foto.jpg`
2. Em `index.html`, localize e substitua:
```html
<!-- De: -->
src="https://placehold.co/400x480/0f172a/3b82f6?text=Nicolas+M."

<!-- Para: -->
src="assets/foto.jpg"
```

### Alterar o esquema de cores

Todas as cores estão centralizadas no início do `style.css` via CSS Custom Properties:

```css
:root {
  --clr-bg:        #0b1121;   /* Fundo principal */
  --clr-primary:   #3b82f6;   /* Azul principal (destaques, links) */
  --clr-accent:    #06b6d4;   /* Ciano (tags, badges) */
  --clr-text:      #e2e8f0;   /* Texto principal */
  --clr-text-muted:#94a3b8;   /* Texto secundário */
  /* ... */
}
```

Alterar essas variáveis propaga a mudança por todo o site.

### Atualizar os slides

No `index.html`, localize o `<iframe>` da seção de Habilidades e substitua o `src` pelo ID da sua apresentação:

```html
<iframe
  src="https://docs.google.com/presentation/d/SEU_ID_AQUI/embed?start=false&loop=false&delayms=3000"
  ...
></iframe>
```

---

## Boas Práticas Aplicadas

- **HTML semântico** — uso de `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>` e atributos `aria-label`
- **CSS com variáveis** — todas as cores, tipografias e espaçamentos centralizados em `:root`
- **Mobile-first responsivo** — breakpoints em 768px e 1024px com Flexbox e CSS Grid
- **Performance** — sem JavaScript de terceiros; animações via CSS com `will-change` implícito
- **Acessibilidade básica** — atributos `alt` em imagens, `aria-label` em botões e links de ícone
- **Organização de código** — CSS dividido em seções comentadas; JS encapsulado em IIFE
- **Nenhum inline style** — exceção apenas para as variáveis `--pct` das barras de progresso, que são dinâmicas por design

---

## Autor

**Nicolas Fernandes Mendes**  
Estudante de Ciência da Computação — 1º Semestre  
Centro Universitário de Brasília (UniCEUB) · Brasília, DF

[![LinkedIn](https://img.shields.io/badge/LinkedIn-nicolas--fernandes--mendes-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/nicolas-fernandes-mendes-9b50b23b0)
[![GitHub](https://img.shields.io/badge/GitHub-nicolas--mendess-181717?style=flat&logo=github)](https://github.com/nicolas-mendess)
[![Email](https://img.shields.io/badge/Email-nicolas.mendes%40sempreceub.com-D14836?style=flat&logo=gmail)](mailto:nicolas.mendes@sempreceub.com)

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos. Sinta-se à vontade para usar a estrutura como referência, desde que os créditos ao autor sejam mantidos.

---

<p align="center">Feito com HTML, CSS e ☕ · portfolioHUB © 2026</p>
