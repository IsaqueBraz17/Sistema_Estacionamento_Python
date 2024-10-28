# Sistema_Estacionamento_Python

Apresentação do Projeto: Sistema de Estacionamento em Python

Introdução
O projeto consiste em um sistema de estacionamento desenvolvido em Python, utilizando a biblioteca CustomTkinter para a criação de uma interface gráfica amigável e intuitiva. O sistema tem como objetivo facilitar o registro e a gestão das entradas e saídas de veículos, permitindo aos usuários um controle eficiente das vagas disponíveis e a realização de pagamentos.

Funcionalidades
    1. Registro de Entrada: O sistema permite registrar a entrada de veículos através da inserção da placa e do nome do proprietário. As placas são validadas para garantir que estão no formato correto (ex: ABC1234).
    2. Controle de Vagas: O sistema inicia com um número pré-definido de vagas (10 no total), e a quantidade de vagas disponíveis é atualizada em tempo real à medida que as entradas e saídas são registradas.
    3. Tabela de Registros: Uma tabela exibe os registros de veículos, mostrando o nome do proprietário, a placa do veículo e a hora de entrada, permitindo uma visualização clara das informações dos veículos no estacionamento.
    4. Registro de Saída: Ao registrar a saída de um veículo, o sistema calcula automaticamente o tempo de permanência e o valor a ser pago, baseado em uma taxa fixa por hora. Um recibo detalhado é gerado para o usuário.
    5. Simulação de Pagamento: O sistema oferece uma interface para simulação de pagamento, permitindo ao usuário escolher entre diferentes formas de pagamento (cartão ou dinheiro). Após a finalização do pagamento, uma notificação de sucesso é exibida.
    6. Interface Gráfica: A interface foi desenvolvida para ser clara e responsiva, utilizando temas personalizados para melhorar a experiência do usuário.
    
Tecnologias Utilizadas
    • Python: Linguagem de programação utilizada para o desenvolvimento do sistema.
    • CustomTkinter: Biblioteca utilizada para a criação da interface gráfica, permitindo um design mais moderno e atrativo.
    • Datetime: Biblioteca para manipulação de data e hora, essencial para o registro de entradas e saídas.
    • Expressões Regulares (re): Utilizadas para a validação do formato das placas de veículos.
    
Conclusão
Este sistema de estacionamento em Python representa uma solução prática e eficiente para o gerenciamento de veículos em estacionamentos. Com uma interface amigável e funcionalidades completas, o projeto visa otimizar o processo de registro e pagamento, proporcionando uma melhor experiência para os usuários e uma administração mais eficaz para os proprietários de estacionamentos.
