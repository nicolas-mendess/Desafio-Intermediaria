# 🌾 AgroGestão
> **Gestão Inteligente e Acessível para a Pecuária de Corte.**

O **AgroGestão** é uma solução digital desenhada para democratizar o acesso à tecnologia no campo. O foco principal é auxiliar o pequeno e médio pecuarista de corte na fase de **engorda**, permitindo um controle rigoroso sobre a saúde financeira e o desenvolvimento ponderal do rebanho de forma simples e intuitiva.

---

## 🚀 Evolução do Projeto

Este projeto nasceu como um desafio acadêmico para a disciplina de **Introdução à Computação**. 
- **v1.0 (Terminal):** Desenvolvido em Python, focado na lógica pura e processamento de dados via terminal.
- **v2.0 (Web PWA):** Evolução para uma interface moderna (Mobile-First) utilizando HTML5, CSS3 e JavaScript Vanilla, preparada para funcionar como um aplicativo (PWA).

---

## 🛠️ Funcionalidades Core

O sistema está dividido em dois módulos estratégicos:

### 1. Gestão Financeira 💰
Permite ao produtor ter uma visão clara da saúde do seu negócio.
* **Cálculo de Lucratividade:** Processa ganhos totais vs. custos de operação.
* **Diagnóstico Instantâneo:** Alertas visuais indicando se a operação está saudável ou se há prejuízo, auxiliando na tomada de decisão rápida.

### 2. Pesagem e Nutrição (Lógica Condicional) ⚖️
O "cérebro" do projeto, que utiliza conceitos reais de zootecnia para automatizar o plano alimentar.
* **Alerta de Déficit:** Identifica se o animal está abaixo da meta de peso.
* **Conversão Alimentar (CA):** Aplica a variável fixa de `7.0` (padrão médio para gado de corte) para calcular a demanda real de matéria seca.
* **Custo de Nutrição:** Calcula automaticamente quanto o produtor precisará investir em ração para que o animal atinja o peso ideal.

---

## 📐 Regras de Negócio & Fórmulas

O projeto aplica as seguintes lógicas matemáticas:

| Módulo | Fórmula |
| :--- | :--- |
| **Financeiro** | `Lucro = Ganhos - Custos` |
| **Déficit de Peso** | `Diferença = Peso Ideal - Peso Atual` |
| **Nutrição** | `KG Ração = Diferença × 7.0 (CA)` |
| **Investimento** | `Custo Total = KG Ração × Preço da Ração` |

---

## 💻 Tecnologias Utilizadas

- **HTML5:** Estruturação semântica.
- **CSS3:** Design responsivo com Variáveis CSS e animações suaves.
- **JavaScript (ES6+):** Lógica de negócios, manipulação de DOM e persistência local (`localStorage`).
- **PWA (Progressive Web App):** Estrutura preparada para instalação no dispositivo e uso offline.

---

## ⚙️ Como Executar o Projeto

1.  Clone o repositório:
    ```bash
    git clone https://github.com/nicolas-mendess/IC-AV01.git
    ```
2.  Abra o arquivo `index.html` em qualquer navegador moderno.
3.  (Opcional) Para visualizar como App, utilize as ferramentas de desenvolvedor do navegador (F12) e altere a visualização para dispositivos móveis.

---

## 📝 Autor

Desenvolvido por **Nicolas Mendes** como parte do projeto de Introdução à Computação.

---
*Este projeto foi desenvolvido com unindo lógica de programação e agronegócio.*
