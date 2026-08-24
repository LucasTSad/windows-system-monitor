# 🖥️ Monitor de Sistema para Windows

## 🎯 Objetivo

Desenvolver um monitor de sistema para **Windows** utilizando Python, capaz de acompanhar em tempo real informações sobre o estado atual do computador.

O projeto tem como objetivo principal servir como projeto de aprendizagem para praticar:

- organização de projetos Python;
- modularização;
- coleta e tratamento de dados;
- tratamento de erros;
- interfaces gráficas;
- monitoramento em tempo real;
- boas práticas de desenvolvimento.

---

## 📌 Status do projeto

**Em desenvolvimento — fase de construção do backend de coleta de dados.**

### Atualmente implementado

- [x] Estrutura inicial do projeto
- [x] Monitoramento de CPU
- [x] Monitoramento de memória RAM
- [ ] Monitoramento de disco
- [ ] Monitoramento de rede
- [ ] Monitoramento de GPU
- [ ] Monitoramento de processos
- [ ] Informações de hardware
- [ ] Interface gráfica
- [ ] Atualização em tempo real
- [ ] Tratamento completo de erros
- [ ] Empacotamento para Windows
- [ ] Deploy/release

---

## 🧰 Biblioteca utilizada

### `psutil`

Principal biblioteca de coleta de informações do sistema.

Será utilizada para obter informações como:

- CPU;
- memória RAM;
- discos;
- rede;
- processos;
- usuários;
- tempo de inicialização;
- sensores disponíveis.

## Bibliotecas futuras

### `tkinter`

Biblioteca utilizada para construir a interface gráfica do monitor.

Será responsável futuramente pela apresentação dos dados coletados e pela interação com o usuário.

### `GPUtil`

Biblioteca destinada à coleta de informações relacionadas à placa de vídeo/GPU.

Possíveis informações:

- utilização da GPU;
- memória utilizada;
- memória disponível;
- temperatura, quando suportada;
- identificação da GPU.

### `WMI`

Biblioteca utilizada para consultar informações de hardware e recursos do Windows por meio do Windows Management Instrumentation.

Possíveis informações:

- processador;
- placa-mãe;
- BIOS;
- dispositivos;
- informações do sistema.

---

## 🏗️ Arquitetura planejada

A aplicação será dividida inicialmente em módulos responsáveis por diferentes componentes do sistema.

```text
Monitor de Sistema
│
├── main.py
│
├── bytes_2_gb.py
│
└── monitor
    ├── cpu
    │   └── cpu_monitor.py
    │
    ├── memory
    │   └── memory_monitor.py
    ├── disk
    │   └── disk_monitor.py
    │
    ├── net
    │   └── network_monitor.py
    ├── gpu
    │   └── gpu_monitor.py
    │
    ├── process
    │   └── process_monitor.py
    └── hardware
        └── hardware_monitor.py
```

A estrutura poderá ser modificada conforme o projeto evoluir.

### Princípio de organização

Os módulos de monitoramento devem ser responsáveis principalmente por:

```text
Sistema
   ↓
Coleta de dados
   ↓
Estrutura de dados
   ↓
Interface / aplicação
   ↓
Apresentação ao usuário
```

A intenção é evitar que a lógica de coleta fique diretamente misturada com a interface gráfica.

---

## 📊 Informações monitoradas

### CPU

- [x] Uso total
- [x] Uso por núcleo
- [x] Núcleos físicos
- [x] Núcleos lógicos
- [x] Frequência atual
- [x] Frequência mínima
- [x] Frequência máxima
- [ ] Temperatura
- [ ] Informações avançadas

### Memória RAM

- [x] Memória Ram total
- [x] Memória Ram utilizada
- [x] Memória Ram disponível
- [x] Percentual utilizado
- [x] Memória Swap total
- [x] Memória Swap utilizada

### Disco

- [ ] Partições/volumes
- [ ] Espaço total
- [ ] Espaço utilizado
- [ ] Espaço livre
- [ ] Percentual utilizado
- [ ] Leitura
- [ ] Escrita
- [ ] Velocidade de leitura/escrita

### Rede

- [ ] Bytes recebidos
- [ ] Bytes enviados
- [ ] Velocidade de download
- [ ] Velocidade de upload
- [ ] Interfaces de rede
- [ ] Status das interfaces
- [ ] Endereços IP

### GPU

- [ ] Nome da GPU
- [ ] Utilização
- [ ] Memória utilizada
- [ ] Memória disponível
- [ ] Temperatura

### Processos

- [ ] Lista de processos
- [ ] PID
- [ ] Nome
- [ ] Uso de CPU
- [ ] Uso de memória
- [ ] Usuário
- [ ] Ordenação
- [ ] Filtros

### Hardware

- [ ] Processador
- [ ] Placa-mãe
- [ ] BIOS
- [ ] Sistema operacional
- [ ] Dispositivos disponíveis

---

## 🖼️ Interface gráfica planejada

A interface será desenvolvida utilizando `tkinter`.

Possível organização:

```text
┌─────────────────────────────────────────────┐
│              SYSTEM MONITOR                 │
├─────────────────────────────────────────────┤
│                                             │
│  CPU                    MEMÓRIA RAM         │
│  Uso: 35%               Uso: 62%            │
│  ███████░░░             ███████████░        │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│  DISCO                  GPU                 │
│  Uso: 48%               Uso: 27%             │
│  █████████░             █████░░░░░          │
│                                             │
├─────────────────────────────────────────────┤
│              PROCESSOS                      │
│                                             │
│  PID       Nome          CPU       RAM      │
│  ...       ...           ...       ...      │
│                                             │
└─────────────────────────────────────────────┘
```

A interface acima é apenas uma referência inicial e poderá ser alterada durante o desenvolvimento.

---

## 🔄 Atualização em tempo real

O monitor deverá atualizar os dados periodicamente sem congelar a interface.

Esse requisito deverá ser implementado posteriormente, considerando:

- atualização periódica;
- tempo de coleta;
- desempenho;
- responsividade do Tkinter;
- execução de tarefas em segundo plano;
- sincronização dos dados.

---

## 🛡️ Tratamento de erros

O programa deverá considerar que nem todas as informações estarão necessariamente disponíveis em todos os computadores.

Exemplos:

- GPU não identificada;
- sensor de temperatura indisponível;
- frequência da CPU indisponível;
- acesso negado a um processo;
- processo encerrado durante a coleta;
- interface de rede indisponível;
- hardware não suportado.

A aplicação deve evitar que uma informação indisponível faça o monitor inteiro parar.

---

## 🧪 Testes

Futuramente o projeto deverá possuir testes para verificar:

- [ ] Coleta de CPU
- [ ] Coleta de memória
- [ ] Coleta de disco
- [ ] Coleta de rede
- [ ] Coleta de GPU
- [ ] Coleta de processos
- [ ] Tratamento de informações indisponíveis
- [ ] Tratamento de exceções
- [ ] Atualização da interface

---

## 📚 Objetivos de aprendizagem

Durante o desenvolvimento, o projeto será utilizado para praticar:

- Python;
- funções;
- módulos;
- estruturas de dados;
- dicionários;
- tratamento de exceções;
- orientação a objetos, quando necessário;
- APIs/bibliotecas externas;
- coleta de dados do sistema;
- programação concorrente;
- interfaces gráficas;
- arquitetura de software;
- debugging;
- testes;
- documentação;
- empacotamento e deploy.

---

## 🗺️ Roadmap

### Fase 1 — Exploração

- [x] Estudar `psutil`
- [x] Testar informações de CPU
- [x] Testar informações de memória
- [ ] Testar disco
- [ ] Testar rede
- [ ] Testar processos

### Fase 2 — Backend

- [x] Criar `cpu_monitor.py`
- [x] Criar `memory_monitor.py`
- [ ] Criar `disk_monitor.py`
- [ ] Criar `network_monitor.py`
- [ ] Criar `gpu_monitor.py`
- [ ] Criar `process_monitor.py`
- [ ] Criar módulo de hardware
- [ ] Padronizar estruturas de retorno
- [ ] Melhorar tratamento de erros

### Fase 3 — Interface

- [ ] Criar janela principal
- [ ] Criar componentes de CPU
- [ ] Criar componentes de RAM
- [ ] Criar componentes de disco
- [ ] Criar componentes de rede
- [ ] Criar componentes de GPU
- [ ] Criar tabela de processos
- [ ] Definir layout final

### Fase 4 — Tempo real

- [ ] Implementar atualização periódica
- [ ] Evitar congelamento da interface
- [ ] Sincronizar coleta e apresentação
- [ ] Otimizar consumo de recursos

### Fase 5 — Robustez

- [ ] Tratamento de exceções
- [ ] Logs
- [ ] Validação de dados
- [ ] Testes
- [ ] Compatibilidade com diferentes hardwares

### Fase 6 — Release

- [ ] `requirements.txt`
- [ ] README final
- [ ] Build do `.exe`
- [ ] Teste em máquina limpa
- [ ] Release
- [ ] Documentação de instalação

---

## 📝 Decisões de desenvolvimento

Este projeto será desenvolvido de forma incremental.

A prioridade não é criar imediatamente uma aplicação completa, mas construir cada parte, entender seu funcionamento e posteriormente integrá-las.

As decisões de arquitetura poderão ser alteradas conforme novos requisitos ou problemas forem encontrados.

---

## 👤 Autor

**Lucas Tostes Sad**

Projeto pessoal desenvolvido com foco em aprendizagem de Python, monitoramento de sistemas e desenvolvimento de software.
