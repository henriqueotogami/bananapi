# Estrutura do Projeto BananaPi

## 📁 Visão Geral da Organização

```
bananapi/
│
├── 📄 README.md                    # Documentação principal
├── 📄 LICENSE                      # Licença MIT
├── 📄 .gitignore                   # Arquivos ignorados pelo Git
│
├── 📁 projects/                     # Projetos principais
│   └── sirios/                     # Projeto SIRIOS
│       ├── backend/                # Scripts Python (CGI)
│       │   ├── gpio_on.py
│       │   └── gpio_off.py
│       ├── frontend/               # Interface web
│       │   ├── index.html
│       │   └── style.css
│       └── README.md               # Documentação do projeto
│
├── 📁 scripts/                      # Scripts reutilizáveis
│   ├── python/                     # Scripts Python
│   │   ├── blink.py               # Piscar LED básico
│   │   ├── blink_mqtt.py          # Blink com MQTT
│   │   └── publish_mqtt.py        # Publicar MQTT
│   ├── shell/                      # Scripts Shell
│   │   ├── Blink.sh
│   │   ├── BlinkPublishMQTT.sh
│   │   └── SendBlink.sh
│   └── README.md                   # Documentação dos scripts
│
├── 📁 docs/                         # Documentação
│   ├── guides/                     # Guias e tutoriais
│   │   ├── buildroot-banana-pi-p2-zero-guide.md
│   │   ├── buildroot-boot-travado-solucao.md
│   │   ├── buildroot-erro-analise-solucao.md
│   │   └── sirios-tutorial.txt
│   ├── articles/                   # Artigos técnicos
│   └── README.md                   # Índice da documentação
│
├── 📁 assets/                       # Recursos estáticos
│   ├── images/
│   │   ├── screenshots/            # Screenshots das interfaces
│   │   ├── diagrams/               # Diagramas de arquitetura
│   │   └── icons/                  # Ícones e logos
│   ├── schematics/                 # Esquemáticos PDF
│   ├── fritzing/                   # Arquivos Fritzing
│   └── excalidraw/                 # Diagramas editáveis
│
└── 📁 archive/                      # Arquivos arquivados
    ├── logs/                       # Logs de instalação/erros
    ├── packages/                   # Listas de pacotes
    └── images/                     # Imagens antigas do sistema
```

## 🎯 Descrição das Pastas

### `projects/`
Contém os projetos principais do repositório. Cada projeto tem sua própria estrutura e documentação.

**Projeto SIRIOS:**
- Sistema completo de controle web de LED
- Backend: Scripts Python executados via CGI
- Frontend: Interface web HTML/CSS

### `scripts/`
Scripts reutilizáveis que podem ser usados em diferentes projetos.

**Python:**
- Scripts básicos de GPIO
- Integração com MQTT
- Utilitários diversos

**Shell:**
- Scripts de automação
- Scripts de deploy
- Scripts de execução

### `docs/`
Toda a documentação do projeto organizada por tipo.

**Guides:**
- Tutoriais passo a passo
- Guias de instalação
- Soluções de problemas

**Articles:**
- Artigos técnicos
- Análises aprofundadas
- Estudos de caso

### `assets/`
Recursos estáticos do projeto.

**Images:**
- Screenshots: Capturas de tela das interfaces
- Diagrams: Diagramas de arquitetura e fluxo
- Icons: Ícones e logos

**Outros:**
- Schematics: Esquemáticos das placas em PDF
- Fritzing: Arquivos de circuitos editáveis
- Excalidraw: Diagramas editáveis

### `archive/`
Arquivos antigos, logs e dados históricos que não são mais ativos no projeto.

## 📝 Convenções de Nomenclatura

### Arquivos Python
- `snake_case.py` (ex: `blink_mqtt.py`)
- Nomes descritivos e claros

### Arquivos Shell
- `PascalCase.sh` ou `snake_case.sh`
- Nomes que descrevem a ação

### Documentação
- `kebab-case.md` ou `snake_case.md`
- Nomes descritivos do conteúdo

## 🔍 Como Encontrar Arquivos

### Procurar um script Python
→ `scripts/python/`

### Procurar documentação
→ `docs/guides/` ou `docs/articles/`

### Procurar imagens
→ `assets/images/`

### Procurar um projeto específico
→ `projects/[nome-do-projeto]/`

## 📚 READMEs por Seção

Cada seção principal tem seu próprio README:

- `README.md` - Visão geral do projeto
- `projects/sirios/README.md` - Documentação do SIRIOS
- `docs/README.md` - Índice da documentação
- `scripts/README.md` - Documentação dos scripts

## 🎨 Benefícios da Organização

1. **Clareza** - Fácil encontrar o que você precisa
2. **Manutenibilidade** - Estrutura lógica facilita manutenção
3. **Escalabilidade** - Fácil adicionar novos projetos/scripts
4. **Profissionalismo** - Estrutura padrão de projetos open source
5. **Documentação** - Cada seção tem sua documentação

---

**Última atualização:** 2025-01-XX

