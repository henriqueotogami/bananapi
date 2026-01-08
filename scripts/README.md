# Scripts do Projeto BananaPi

Coleção de scripts Python e Shell para controle de GPIO e integração IoT.

## 📁 Estrutura

```
scripts/
├── python/          # Scripts Python
│   ├── blink.py            # Piscar LED básico
│   ├── blink_mqtt.py       # Blink com publicação MQTT
│   └── publish_mqtt.py     # Publicar mensagens MQTT
└── shell/           # Scripts Shell
    ├── blink.sh            # Executar blink.py
    ├── blink_mqtt.sh       # Executar blink_mqtt.py
    └── deploy.sh           # Enviar arquivos via SCP
```

## 🐍 Scripts Python

### `blink.py`
Script básico para piscar um LED conectado ao GPIO 7.

**Uso:**
```bash
python3 scripts/python/blink.py
```

### `blink_mqtt.py`
Pisca LED e publica eventos no broker MQTT.

**Uso:**
```bash
python3 scripts/python/blink_mqtt.py
```

**Configuração:**
Edite as variáveis no início do arquivo:
- `BROKER` - Endereço do broker MQTT
- `PORT` - Porta do broker (padrão: 1883)
- `TOPIC` - Tópico MQTT

### `publish_mqtt.py`
Publica mensagens no broker MQTT.

**Uso:**
```bash
python3 scripts/python/publish_mqtt.py
```

## 🐚 Scripts Shell

### `blink.sh`
Script para executar `blink.py` na Banana Pi.

### `blink_mqtt.sh`
Script para executar `blink_mqtt.py` na Banana Pi.

### `deploy.sh`
Script para enviar arquivos para a Banana Pi via SCP.

**Uso:**
```bash
./scripts/shell/deploy.sh
```

## 📝 Requisitos

### Python
```bash
pip3 install paho-mqtt
```

### Permissões
Os scripts que manipulam GPIO precisam de permissões sudo. Configure:
```bash
sudo visudo
# Adicionar: seu_usuario ALL=(ALL) NOPASSWD: /usr/bin/tee, /bin/echo
```

## 🔧 Configuração

1. **Ajustar GPIO:** Edite o número do pino nos scripts (padrão: GPIO 7)
2. **Configurar MQTT:** Edite as variáveis de conexão nos scripts MQTT
3. **Ajustar hostname:** Nos scripts shell, altere `banana.local` para o hostname da sua placa

## 📚 Mais Informações

- [Documentação Principal](../../README.md)
- [Projeto SIRIOS](../projects/sirios/README.md)

