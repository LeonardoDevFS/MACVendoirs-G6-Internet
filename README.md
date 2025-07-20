# Buscador de Fabricante de MAC - G6 Internet

Este é um software utilitário de desktop desenvolvido para agilizar o processo de identificação de fabricantes de equipamentos de rede (como roteadores, ONUs, etc.) a partir de seus endereços MAC.

O programa foi criado para otimizar as operações diárias da equipe da **G6 Internet**, fornecendo uma ferramenta rápida, leve e sempre à mão.

## Funcionalidades Principais

* **Busca Rápida:** Basta colar o endereço MAC e clicar em "Buscar Fabricante" para obter o nome da empresa responsável pelo hardware.
* **Interface Compacta:** Projetado para ocupar pouco espaço na tela, ideal para o uso no dia a dia sem atrapalhar outras janelas.
* **Fixar no Topo:** Possui uma opção para manter a janela do programa sempre visível, por cima de todas as outras, facilitando a consulta enquanto se trabalha em outros sistemas.
* **Portátil e Leve:** Não requer instalação complexa e consome poucos recursos do sistema.

## Como Usar

1.  Execute o programa através do atalho `iniciar.bat`.
2.  A janela principal do aplicativo será aberta.
3.  Digite ou cole o endereço MAC do equipamento no campo de texto.
4.  Clique no botão **"Buscar Fabricante"**.
5.  O nome do fabricante será exibido logo abaixo.

## Estrutura do Projeto

Este projeto foi desenvolvido em Python e está organizado nos seguintes arquivos:

* `mac_lookupG6.py`: Ponto de entrada principal da aplicação.
* `gui.py`: Responsável por construir e gerenciar toda a interface gráfica.
* `api_client.py`: Módulo que faz a comunicação com a API externa `macvendors.com` para buscar os dados.
* `config.py`: Armazena o token e a URL da API.
* `iniciar.bat`: Atalho para iniciar o programa de forma rápida, sem a necessidade de abrir um terminal.
* `requirements.txt`: Lista as dependências Python necessárias para o projeto.
