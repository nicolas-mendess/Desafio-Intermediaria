# 🌾 AgroGestão

Sistema de gestão para produtor rural desenvolvido em Python.
Projeto acadêmico de 1º semestre.

---

## 📋 O que o sistema faz

Menu com 3 opções no terminal:

- **Gestão Financeira** — calcula o lucro e indica se a operação está saudável ou em prejuízo
- **Pesagem e Nutrição** — verifica se o boi atingiu o peso ideal e, se não, calcula o custo da ração necessária
- **Sair** — encerra o programa

---

## 🚀 Como executar

Ter o Python 3 instalado. No terminal, rode:

```bash
python main.py
```

---

## 🧮 Lógica de cálculo

**Gestão Financeira**
```
Lucro = Receita - Custos
```

**Pesagem e Nutrição**
```
KG que faltam = Peso Ideal - Peso Atual
Custo da ração = KG que faltam × Preço do KG de ração
```

---

## ✅ Exemplo de uso

```
🌾  AGRO GESTÃO
[1] Gestão Financeira
[2] Pesagem e Nutrição Inteligente
[3] Sair do Sistema

👉 Escolha uma opção: 2

🎯 Peso Ideal / Meta (KG): 450
⚖️  Peso Atual na Balança (KG): 380

⚠️  Animal abaixo do peso em 70.00 kg.
🌽 MÓDULO DE NUTRIÇÃO ACIONADO

💲 Preço do KG de ração (R$): 3.50

KG de ração necessário:     70.00 kg
Custo estimado de nutrição: R$ 245.00
```

---

## 🛠️ Tecnologias

- Python 3
- Somente recursos básicos: `while`, `if/elif/else`, `input`, `print` e `float`
