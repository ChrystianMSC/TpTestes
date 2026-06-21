# Idan

Este é um projeto de jogo de cartas competitivo projetado para funcionar via linha de comando, permitindo que dois jogadores se enfrentem diretamente através de uma conexão **Peer-to-Peer (P2P)**.

## 👥 Integrantes
* **Chrystian Martins Soares Costa**

---

## 🕹️ Explicação do Sistema

O sistema consiste em uma aplicação de terminal onde a lógica do jogo e a comunicação de rede acontecem simultaneamente. Diferente de jogos tradicionais que dependem de um servidor central, o **Idan** utiliza a arquitetura **P2P**, onde cada instância do jogo atua tanto como cliente quanto como servidor.

### Funcionamento Geral:
1. **Conexão:** Um jogador atua como o "Host" (aguardando conexão) e o outro como "Guest" (conectando-se ao IP do Host).
2. **Mecânica de Jogo:** O jogo processa turnos alternados, onde cada jogada realizada em um terminal é enviada via *socket* para o adversário.
3. **Interface:** Toda a interação é feita via texto (CLI), exibindo o estado do tabuleiro, a mão do jogador e o log de ações.
4. **Sincronização:** O sistema garante que ambos os jogadores visualizem o mesmo estado de jogo, validando jogadas e atualizando os pontos de vida/cartas em tempo real.

---

## 🛠️ Tecnologias Utilizadas

Para a implementação deste projeto, as seguintes tecnologias e conceitos são fundamentais:

* **Linguagem de Programação:** Python (v3.10+)
* **Protocolo TCP:** Utilização de **Sockets** para garantir a entrega confiável e ordenada de pacotes de dados entre as duas máquinas.
* **Multithreading:** Necessário para permitir que a interface do usuário continue funcional e responsiva para reações rápidas enquanto o sistema "escuta" as jogadas vindas da rede em segundo plano.
* **Serialização de Dados (JSON):** Para converter os objetos das cartas e estados de jogo em texto para transporte via rede e posterior reconstrução no destino.
* **Framework de Testes:** `Pytest` e `Pytest-cov` para automação e mensuração de cobertura de código.

---

## 🚀 Como Executar o Jogo

Certifique-se de estar na raiz do projeto (`chrystianmsc-tptestes/`).

**1. Iniciar o Jogador 1 (Host):**
```bash
python -m src.main host Chrystian

```

**2. Iniciar o Jogador 2 (Guest):**
Abra um segundo terminal e execute:

```bash
python -m src.main guest Adversario

```

---

## 🧪 Como Executar os Testes Localmente

A suíte de testes foi desenvolvida seguindo as melhores práticas de Engenharia de Software, utilizando APIs públicas, testes de comportamento, escopos focados e isolamento via *mocks* para simular a rede de forma determinística.

### Pré-requisitos

Instale as dependências de testes necessárias:

```bash
pip install pytest pytest-cov

```

### Executando os Testes e Gerando Relatório de Cobertura

Para rodar os **30 testes automatizados** (unitários e de integração) e mensurar a cobertura de código, execute o seguinte comando na raiz do repositório:

```bash
python -m pytest --cov=src --cov-report=term-missing tests/

```

> 📊 **Critério de Aceitação:** A cobertura total do código está configurada para se manter **$\ge$ 80%**, cobrindo com precisão as regras de negócio de fluxo de jogo, renderização em terminal, manipulação de estados do jogador e tratamento do protocolo de rede.

---

## ⚙️ CI/CD e Infraestrutura de Testes

O projeto utiliza integração contínua de ponta a ponta configurada através do **GitHub Actions**.

* **Multi-OS Matrix:** Os testes são disparados automaticamente a cada *push* ou *pull request* nas plataformas **Linux (Ubuntu), MacOS e Windows** sob as versões mais recentes do Python.
* **Codecov Integration:** Após a execução bem-sucedida da suíte de testes, o relatório XML de cobertura gerado é exportado automaticamente para a plataforma **Codecov**, permitindo o rastreamento histórico e visual da qualidade do código.

---

## 📥 Como Clonar o Repositório

```bash
git clone https://github.com/chrystianmsc/idan.git

```
