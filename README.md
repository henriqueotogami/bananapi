# BananaPi - Sistemas Embarcados e IoT

> Repositório com projetos, scripts e tutoriais desenvolvidos para estudos de sistemas embarcados e Internet das Coisas (IoT) utilizando o microcomputador Banana Pi M2 Zero e P2 Zero.

<div align="center">
<img width="500" src="https://github.com/henriqueotogami/project-sirios/blob/main/resources/images/rounded-header-otogami.png?raw=true">
</div>
<br>
<div align="center">
<img src="https://img.shields.io/github/release-date/henriqueotogami/bananapi">
</div>
<br>
<div align="center">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/henriqueotogami/bananapi">
<img src="https://img.shields.io/github/checks-status/henriqueotogami/bananapi/main">
<img src="https://img.shields.io/github/issues/henriqueotogami/bananapi">
</div>
<br>
<div align="center">
<img src="https://img.shields.io/github/forks/henriqueotogami/bananapi?style=flat">
<img src="https://img.shields.io/github/stars/henriqueotogami/bananapi?style=flat">
<img src="https://img.shields.io/github/license/henriqueotogami/bananapi">
</div>
<div align="center">
<br>
<a href="https://wakatime.com/badge/user/1e53636e-c916-4d50-9ce1-f3ac75a883e3/project/3ae4b915-02bd-437c-8c03-071716563261"><img src="https://wakatime.com/badge/user/1e53636e-c916-4d50-9ce1-f3ac75a883e3/project/3ae4b915-02bd-437c-8c03-071716563261.svg" alt="wakatime"></a>
</div>

## 📋 Sobre o Projeto

Este repositório contém uma coleção de projetos práticos e tutoriais para desenvolvimento de sistemas embarcados e aplicações IoT utilizando as placas Banana Pi M2 Zero e P2 Zero. Os projetos incluem controle de GPIO, servidores web, integração MQTT, e configuração de sistemas Linux customizados com Buildroot.

## 📁 Estrutura do Projeto

### Projetos Principais (`projects/`)
- **sirios/** - Sistema de Acionamento Remoto de LED via Web
  - `backend/` - Scripts Python CGI (gpio_on.py, gpio_off.py)
  - `frontend/` - Interface web (index.html, style.css)
  - `README.md` - Documentação do projeto

### Scripts Reutilizáveis (`scripts/`)
- **python/** - Scripts Python para GPIO e MQTT
  - `blink.py` - Piscar LED básico
  - `blink_mqtt.py` - Blink com publicação MQTT
  - `publish_mqtt.py` - Publicar mensagens MQTT
- **shell/** - Scripts Shell para automação
  - `Blink.sh` - Executar blink.py
  - `BlinkPublishMQTT.sh` - Executar blink_mqtt.py
  - `SendBlink.sh` - Enviar arquivos via SCP

### Documentação (`docs/`)
- **guides/** - Guias e tutoriais
  - `buildroot-banana-pi-p2-zero-guide.md` - Guia completo Buildroot
  - `buildroot-boot-travado-solucao.md` - Solução problemas de boot
  - `buildroot-erro-analise-solucao.md` - Análise de erros
  - `sirios-tutorial.txt` - Tutorial do projeto SIRIOS
- **articles/** - Artigos técnicos e análises

### Recursos (`assets/`)
- **images/** - Imagens do projeto
  - `screenshots/` - Screenshots das interfaces
  - `diagrams/` - Diagramas de arquitetura
  - `icons/` - Ícones e logos
- **schematics/** - Esquemáticos das placas (PDF)
- **fritzing/** - Arquivos Fritzing para circuitos
- **excalidraw/** - Diagramas editáveis

### Arquivos Arquivados (`archive/`)
- **logs/** - Logs de instalação e erros
- **packages/** - Listas de pacotes instalados
- **images/** - Imagens antigas do sistema

## 📂 Estrutura do Repositório

```
bananapi/
├── LICENSE
├── README.md
├── .gitignore
│
├── projects/                 # Projetos principais
│   └── sirios/              # Projeto SIRIOS
│       ├── backend/         # Scripts Python CGI
│       │   ├── gpio_on.py
│       │   └── gpio_off.py
│       ├── frontend/        # Interface web
│       │   ├── index.html
│       │   └── style.css
│       └── README.md
│
├── scripts/                  # Scripts reutilizáveis
│   ├── python/              # Scripts Python
│   │   ├── blink.py
│   │   ├── blink_mqtt.py
│   │   └── publish_mqtt.py
│   ├── shell/               # Scripts Shell
│   │   ├── Blink.sh
│   │   ├── BlinkPublishMQTT.sh
│   │   └── SendBlink.sh
│   └── README.md
│
├── docs/                     # Documentação
│   ├── guides/              # Guias e tutoriais
│   │   ├── buildroot-banana-pi-p2-zero-guide.md
│   │   ├── buildroot-boot-travado-solucao.md
│   │   ├── buildroot-erro-analise-solucao.md
│   │   └── sirios-tutorial.txt
│   ├── articles/            # Artigos técnicos
│   └── README.md
│
├── assets/                   # Recursos estáticos
│   ├── images/
│   │   ├── screenshots/     # Screenshots
│   │   ├── diagrams/        # Diagramas
│   │   └── icons/           # Ícones
│   ├── schematics/          # Esquemáticos PDF
│   ├── fritzing/            # Arquivos Fritzing
│   └── excalidraw/          # Diagramas editáveis
│
└── archive/                  # Arquivos arquivados
    ├── logs/                # Logs antigos
    ├── packages/            # Listas de pacotes
    └── images/              # Imagens do sistema
```

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem de programação para scripts de controle
- **Apache2** - Servidor web para hospedar interface
- **CGI (Common Gateway Interface)** - Interface para executar scripts Python via web
- **MQTT** - Protocolo de mensageria para IoT
- **GPIO (General Purpose Input/Output)** - Controle de pinos da placa
- **Buildroot** - Sistema para construir imagens Linux customizadas
- **HTML/CSS** - Interface web frontend
- **Linux/Raspbian** - Sistema operacional embarcado
- **SSH** - Acesso remoto à placa

## 📝 Funcionalidades Principais

### Controle de GPIO
Os scripts em `python/` e `project-sirios/` implementam controle de GPIO para:
- Ligar e desligar LEDs
- Piscar LEDs em intervalos configuráveis
- Manipular pinos de entrada/saída digital

### Interface Web (Projeto SIRIOS)
O projeto SIRIOS oferece:
- Interface web moderna e responsiva
- Controle remoto de LED via navegador
- Integração com Apache e módulo CGI
- Feedback visual em tempo real

### Integração MQTT
Scripts para comunicação IoT:
- Publicar eventos de acionamento de LED
- Integração com brokers MQTT (HiveMQ, Mosquitto, etc.)
- Notificações em tempo real

### Buildroot e Sistemas Customizados
Documentação completa para:
- Compilar imagens Linux customizadas
- Configurar Buildroot para Banana Pi
- Solucionar problemas de boot e compilação

## 🚀 Como Usar

### Pré-requisitos

- Banana Pi M2 Zero ou P2 Zero
- Cartão SD com Raspbian/Debian instalado
- Conexão SSH configurada
- LED e resistores (para projetos de GPIO)
- Python 3 instalado

### Instalação Básica

1. **Clone o repositório:**
```bash
git clone https://github.com/henriqueotogami/bananapi.git
cd bananapi
```

2. **Envie os arquivos para a Banana Pi:**
```bash
# Via SCP
scp scripts/python/blink.py pi@banana.local:~
scp projects/sirios/backend/* pi@banana.local:~
scp projects/sirios/frontend/* pi@banana.local:~
```

3. **Execute os scripts:**
```bash
# Na Banana Pi via SSH
ssh pi@banana.local
python3 blink.py
```

### Projeto SIRIOS - Controle Web de LED

Para configurar o projeto SIRIOS completo:

1. **Instalar Apache e habilitar CGI:**
```bash
sudo apt-get install apache2
sudo a2enmod cgi
sudo systemctl restart apache2
```

2. **Configurar permissões:**
```bash
sudo visudo
# Adicionar: www-data ALL=(ALL) NOPASSWD: /usr/bin/tee, /bin/echo
```

3. **Copiar scripts CGI:**
```bash
sudo cp projects/sirios/backend/gpio_on.py /usr/lib/cgi-bin/
sudo cp projects/sirios/backend/gpio_off.py /usr/lib/cgi-bin/
sudo chmod +x /usr/lib/cgi-bin/gpio_*.py
```

4. **Copiar interface web:**
```bash
sudo cp projects/sirios/frontend/index.html /var/www/html/
sudo cp projects/sirios/frontend/style.css /var/www/html/
sudo cp assets/images/icons/icon-otogami.svg /var/www/html/
```

5. **Acessar interface:**
```
http://seu-ip-banana-pi/
```

### Integração MQTT

1. **Instalar biblioteca MQTT:**
```bash
pip3 install paho-mqtt
```

2. **Configurar broker MQTT:**
```python
# Editar PublishMQTT.py ou BlinkPublishMQTT.py
BROKER = "seu-broker-mqtt.com"
PORT = 1883
```

3. **Executar:**
```bash
python3 BlinkPublishMQTT.py
```

### Buildroot - Compilar Imagem Linux

Para compilar uma imagem Linux customizada:

1. **Instalar dependências:**
```bash
sudo apt-get install build-essential git wget cpio unzip rsync bc bzip2
```

2. **Clonar e configurar Buildroot:**
```bash
git clone https://github.com/xqdzn/buildroot.git
cd buildroot
make bananapi_p2_zero_defconfig
```

3. **Compilar:**
```bash
make
```

4. **Gravar imagem:**
```bash
sudo dd if=output/images/sdcard.img of=/dev/sdX bs=4M status=progress
```

**📖 Para mais detalhes, consulte:** `docs/guides/buildroot-banana-pi-p2-zero-guide.md`

## 📚 Conteúdos Abordados

- ✅ Controle de GPIO em sistemas embarcados
- ✅ Programação Python para hardware
- ✅ Configuração de servidor web Apache
- ✅ Interface CGI para execução de scripts
- ✅ Protocolo MQTT para IoT
- ✅ Desenvolvimento de interfaces web
- ✅ Compilação de sistemas Linux customizados
- ✅ Buildroot e cross-compilation
- ✅ Troubleshooting de sistemas embarcados
- ✅ Documentação técnica de projetos

## 🎯 Projetos Principais

### Projeto SIRIOS
Sistema de acionamento remoto de LED via interface web, utilizando Apache, Python e CGI. Permite controlar LEDs conectados à Banana Pi através de uma página web acessível na rede local.

**Características:**
- Interface web moderna e responsiva
- Controle via botões (Ligar/Desligar)
- Feedback visual em tempo real
- Arquitetura modular e escalável

### Controle Básico de LED
Scripts Python simples para piscar e controlar LEDs, ideais para aprendizado de GPIO e sistemas embarcados.

### Integração MQTT
Projetos que demonstram como integrar dispositivos IoT com brokers MQTT para comunicação em tempo real.

## ⚙️ Como Funciona

### Controle de GPIO
Os scripts Python manipulam os pinos GPIO através do sistema de arquivos `/sys/class/gpio/`:
1. Exporta o pino GPIO desejado
2. Configura como saída (output)
3. Define valor alto (1) ou baixo (0) para ligar/desligar
4. Unexporta o pino após uso

### Projeto SIRIOS - Fluxo
1. Usuário acessa interface web no navegador
2. Clica em botão "Ligar" ou "Desligar"
3. Formulário HTML envia requisição GET para script CGI
4. Apache executa script Python via módulo CGI
5. Script Python manipula GPIO
6. Resposta é exibida na interface via iframe

### MQTT Integration
1. Script Python conecta ao broker MQTT
2. Publica mensagens em tópicos específicos
3. Clientes MQTT podem se inscrever e receber notificações
4. Permite comunicação bidirecional entre dispositivos

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📖 Referências

- [Documentação Banana Pi](http://www.banana-pi.org/)
- [Documentação Apache CGI](https://httpd.apache.org/docs/2.4/howto/cgi.html)
- [GPIO Interface SysFS](https://www.kernel.org/doc/Documentation/gpio/sysfs.txt)
- [Buildroot Manual](https://buildroot.org/downloads/manual/manual.html)
- [MQTT Protocol](https://mqtt.org/)
- [Raspbian Documentation](https://www.raspberrypi.org/documentation/)

## 📝 Artigos e Tutoriais

### Artigos Publicados
- [Artigos no Medium](https://medium.com/@henriqueotogami)
- [Artigos no Dev.to](https://dev.to/henriqueotogami)

### Wiki do Repositório
- [Desafio 01 - Piscar um LED na BananaPi utilizando Python via SSH](https://github.com/henriqueotogami/bananapi/wiki/Desafio-01-%E2%80%90-Piscar-um-LED-na-BananaPi-utilizando-Python-via-SSH)
- [Desafio 02 - Notificar o acionamento do LED utilizando Python para um Web Client MQTT](https://github.com/henriqueotogami/bananapi/wiki)

## 💼 Conecte-se

- [Perfil no LinkedIn](https://www.linkedin.com/in/henrique-matheus-alves-pereira)
- [GitHub](https://github.com/henriqueotogami)

## 🙏 Apoie o Projeto

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/henriqueotogami)

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um **fork** deste repositório
2. Crie um **branch** para sua feature (`git checkout -b feature/nova-feature`)
3. Faça **commit** das suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça **push** para o branch (`git push origin feature/nova-feature`)
5. Abra um **Pull Request**

## 📝 Changelog

### Versão 1.2
- Adicionado projeto SIRIOS
- Documentação de Buildroot
- Guias de troubleshooting
- Integração MQTT

### Versão 1.0
- Projetos básicos de GPIO
- Scripts Python iniciais
- Documentação básica

---

### Hashtags
#BananaPi #IoT #EmbeddedSystems #Python #Apache #CGI #MQTT #GPIO #Buildroot #Linux #RaspberryPi #SistemasEmbarcados #InternetOfThings #OpenSource #GitHub #HardwareProgramming #WebDevelopment #Tutorial #Learning

### Meta Keywords
```
banana pi, sistemas embarcados, IoT, internet das coisas, python, apache, 
CGI, MQTT, GPIO, buildroot, linux, raspbian, controle remoto, LED, 
hardware programming, web development, tutorial, aprendizado, projetos práticos,
sistemas embarcados, microcomputador, single board computer, SBC
```

<br>
<div align="center">
<img width="auto" src="https://github.com/henriqueotogami/learning-c-language/blob/master/images/kofi-henrique-otogami.jpg?raw=true">
</div>

---

<div align="center">

<br>

> ### **Muito obrigado, e que a força esteja com você.**
>
> ### Desenvolvido por **Henrique Otogami** 🦁

</div>
