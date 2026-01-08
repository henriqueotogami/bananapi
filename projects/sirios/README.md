# Projeto SIRIOS

Sistema de Acionamento Remoto de LED via Interface Web

## 📋 Descrição

O SIRIOS é um projeto completo que permite controlar LEDs conectados à Banana Pi através de uma interface web moderna e responsiva. Utiliza Apache com módulo CGI para executar scripts Python que manipulam os pinos GPIO.

## 🏗️ Arquitetura

```
[Browser] → HTTP → [Apache/CGI] → [Python GPIO] → [LED]
```

## 📁 Estrutura

```
sirios/
├── backend/          # Scripts Python (CGI)
│   ├── gpio_on.py   # Script para ligar LED
│   └── gpio_off.py  # Script para desligar LED
└── frontend/         # Interface Web
    ├── index.html    # Página principal
    └── style.css    # Estilos
```

## 🚀 Instalação

### Pré-requisitos

- Banana Pi M2 Zero ou P2 Zero
- Apache2 instalado
- Módulo CGI habilitado
- Python 3

### Passos

1. **Instalar Apache e habilitar CGI:**
```bash
sudo apt-get install apache2
sudo a2enmod cgi
sudo systemctl restart apache2
```

2. **Configurar permissões sudo:**
```bash
sudo visudo
# Adicionar: www-data ALL=(ALL) NOPASSWD: /usr/bin/tee, /bin/echo
```

3. **Copiar scripts CGI:**
```bash
sudo cp backend/gpio_on.py /usr/lib/cgi-bin/
sudo cp backend/gpio_off.py /usr/lib/cgi-bin/
sudo chmod +x /usr/lib/cgi-bin/gpio_*.py
```

4. **Copiar interface web:**
```bash
sudo cp frontend/index.html /var/www/html/
sudo cp frontend/style.css /var/www/html/
sudo cp ../../assets/images/icons/icon-otogami.svg /var/www/html/
```

5. **Acessar:**
```
http://seu-ip-banana-pi/
```

## 📚 Documentação

Para mais detalhes, consulte:
- [Tutorial Completo](../../docs/guides/sirios-tutorial.txt)
- [Guia de Instalação do Apache](../../docs/guides/)

## 🔧 Funcionalidades

- ✅ Interface web moderna e responsiva
- ✅ Controle remoto via navegador
- ✅ Feedback visual em tempo real
- ✅ Suporte para múltiplos dispositivos
- ✅ Arquitetura modular e escalável

## 📝 Licença

MIT License - veja [LICENSE](../../../LICENSE) para detalhes.

