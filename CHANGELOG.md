# Changelog - Reorganização do Projeto

## [2.0.0] - 2025-01-XX

### 🎯 Reorganização Completa

#### ✅ Estrutura de Diretórios
- Criada estrutura `projects/` para projetos principais
- Criada estrutura `scripts/` para scripts reutilizáveis  
- Criada estrutura `docs/` para documentação organizada
- Criada estrutura `assets/` para recursos estáticos
- Criada estrutura `archive/` para arquivos antigos

#### 📦 Movimentação de Arquivos

**Projetos:**
- `project-sirios/` → `projects/sirios/`
  - Scripts Python → `projects/sirios/backend/`
  - Interface web → `projects/sirios/frontend/`

**Scripts:**
- `python/` → `scripts/python/`
- `shell/` → `scripts/shell/`

**Documentação:**
- `notes/buildroot-*.md` → `docs/guides/`
- `notes/tutorial-sirios.txt` → `docs/guides/`

**Recursos:**
- `resources/images/` → `assets/images/`
  - Screenshots → `assets/images/screenshots/`
  - Diagramas → `assets/images/diagrams/`
  - Ícones → `assets/images/icons/`
- `resources/excalidraw/` → `assets/excalidraw/`
- `resources/fritzing/` → `assets/fritzing/`
- `bananapi-schematics/` → `assets/schematics/`

**Arquivos Arquivados:**
- Logs → `archive/logs/`
- Listas de pacotes → `archive/packages/`
- Imagens do sistema → `archive/images/`

#### ➕ Arquivos Adicionados

- `.gitignore` - Controle de arquivos ignorados
- `projects/sirios/README.md` - Documentação do SIRIOS
- `docs/README.md` - Índice da documentação
- `scripts/README.md` - Documentação dos scripts
- `ESTRUTURA.md` - Visão geral da organização
- `ORGANIZACAO.md` - Detalhes da reorganização
- `CHANGELOG.md` - Este arquivo

#### 🔄 Renomeações

**Scripts Python:**
- `BlinkPublishMQTT.py` → `blink_mqtt.py`
- `PublishMQTT.py` → `publish_mqtt.py`

#### 📝 Documentação Atualizada

- README.md principal atualizado com nova estrutura
- Caminhos atualizados em exemplos de código
- Referências corrigidas

#### 🗑️ Limpeza

- Diretórios vazios removidos
- Arquivos duplicados consolidados
- Estrutura otimizada

### 📊 Impacto

- ✅ Melhor organização e navegação
- ✅ Estrutura mais profissional
- ✅ Facilita manutenção e escalabilidade
- ✅ Documentação mais acessível
- ✅ Separação clara entre projetos, scripts e recursos

---

## [1.2.0] - Versão Anterior

- Projetos básicos de GPIO
- Scripts Python iniciais
- Documentação básica
- Projeto SIRIOS inicial

---

**Nota:** Para ver detalhes completos da reorganização, consulte `ORGANIZACAO.md` e `ESTRUTURA.md`.

