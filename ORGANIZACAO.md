# Organização do Projeto BananaPi

## ✅ Reorganização Concluída

O projeto foi reorganizado para melhor estrutura e manutenibilidade.

## 📊 Mudanças Realizadas

### ✅ Estrutura de Diretórios

- ✅ Criada estrutura `projects/` para projetos principais
- ✅ Criada estrutura `scripts/` para scripts reutilizáveis
- ✅ Criada estrutura `docs/` para documentação
- ✅ Criada estrutura `assets/` para recursos estáticos
- ✅ Criada estrutura `archive/` para arquivos antigos

### ✅ Arquivos Movidos

#### Projetos
- `project-sirios/` → `projects/sirios/`
  - Scripts Python → `projects/sirios/backend/`
  - Interface web → `projects/sirios/frontend/`

#### Scripts
- `python/` → `scripts/python/`
- `shell/` → `scripts/shell/`

#### Documentação
- `notes/buildroot-*.md` → `docs/guides/`
- `notes/tutorial-sirios.txt` → `docs/guides/`

#### Recursos
- `resources/images/` → `assets/images/`
  - Screenshots → `assets/images/screenshots/`
  - Diagramas → `assets/images/diagrams/`
  - Ícones → `assets/images/icons/`
- `resources/excalidraw/` → `assets/excalidraw/`
- `resources/fritzing/` → `assets/fritzing/`
- `bananapi-schematics/` → `assets/schematics/`

#### Arquivos Arquivados
- `notes/*.txt` (logs) → `archive/logs/`
- `packages-*.txt` → `archive/packages/`
- `*.img` → `archive/images/`
- `images/*.png` → `assets/images/screenshots/`

### ✅ Arquivos Criados

- ✅ `.gitignore` - Para ignorar arquivos grandes
- ✅ `projects/sirios/README.md` - Documentação do SIRIOS
- ✅ `docs/README.md` - Índice da documentação
- ✅ `scripts/README.md` - Documentação dos scripts

### ⚠️ Arquivos a Renomear Manualmente

Alguns arquivos precisam ser renomeados manualmente (devido a permissões):

```bash
# Na pasta scripts/python/
mv BlinkPublishMQTT.py blink_mqtt.py
mv PublishMQTT.py publish_mqtt.py

# Na pasta scripts/shell/
mv BlinkPublishMQTT.sh blink_mqtt.sh
mv SendBlink.sh deploy.sh
```

## 📁 Nova Estrutura

```
bananapi/
├── projects/          # Projetos principais
├── scripts/           # Scripts reutilizáveis
├── docs/              # Documentação
├── assets/            # Recursos estáticos
└── archive/           # Arquivos arquivados
```

## 🎯 Benefícios

1. **Organização Clara** - Cada tipo de arquivo em seu lugar
2. **Fácil Navegação** - Estrutura lógica e intuitiva
3. **Manutenibilidade** - Mais fácil de manter e atualizar
4. **Escalabilidade** - Fácil adicionar novos projetos
5. **Documentação** - READMEs específicos para cada seção

## 📝 Próximos Passos

1. ✅ Renomear arquivos manualmente (se necessário)
2. ✅ Atualizar referências em scripts e documentação
3. ✅ Testar caminhos após reorganização
4. ✅ Atualizar links no README principal

## 🔄 Compatibilidade

Os caminhos nos scripts podem precisar ser atualizados. Verifique:
- Scripts shell que referenciam caminhos antigos
- Documentação com links para arquivos movidos
- READMEs com referências a diretórios antigos

---

**Data da Reorganização:** 2025-01-XX  
**Versão:** 2.0

