# Importando Bibliotecas
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import datetime
import re

# Configuração inicial de vagas
TOTAL_VAGAS = 10
vagas_disponiveis = TOTAL_VAGAS

# Banco de dados simulado para armazenar as informações dos veículos
banco_de_dados = {}

# Função para validar a placa do veículo (formato básico: 3 letras e 4 números)
def validar_placa(placa):
    padrao = r'^[A-Z]{3}[0-9]{4}$'  # Exemplo: ABC1234
    return re.match(padrao, placa) is not None

# Função para atualizar a exibição das vagas disponíveis
def atualizar_vagas():
    vagas_label.configure(text=f"Vagas disponíveis: {vagas_disponiveis}")

# Função para atualizar a tabela de registros
def atualizar_tabela():
    # Limpa a tabela antes de inserir novos dados
    for item in tabela.get_children():
        tabela.delete(item)

    # Adiciona os registros do banco de dados à tabela
    for placa, dados in banco_de_dados.items():
        tabela.insert('', 'end', values=(dados['nome'], placa, dados['entrada'].strftime('%H:%M:%S')))

# Função para registrar a entrada do veículo
def registrar_entrada():
    global vagas_disponiveis
    placa = entry_placa.get().upper()
    nome_proprietario = entry_nome.get().strip()
    agora = datetime.datetime.now()  # Pega o momento da entrada
    
    if not placa or not nome_proprietario:
        resultado_label.configure(text="Por favor, insira a placa e o nome do proprietário.")
    elif not validar_placa(placa):
        resultado_label.configure(text="Placa inválida! Use o formato ABC1234.")
    elif placa in banco_de_dados:
        resultado_label.configure(text=f"O veículo com placa {placa} já está no estacionamento.")
    elif vagas_disponiveis == 0:
        resultado_label.configure(text="Estacionamento lotado! Não há vagas disponíveis.")
    else:
        banco_de_dados[placa] = {'nome': nome_proprietario, 'entrada': agora}
        vagas_disponiveis -= 1
        resultado_label.configure(text=f"Entrada registrada para {nome_proprietario} (Placa: {placa}) às {agora.strftime('%H:%M:%S')}.")
        atualizar_vagas()
        atualizar_tabela()
    
    entry_placa.delete(0, ctk.END)
    entry_nome.delete(0, ctk.END)

# Função para registrar a saída e calcular o valor a ser pago
def registrar_saida():
    placa = entry_placa.get().upper()
    taxa_por_hora = 5.0  # Define a taxa por hora
    agora = datetime.datetime.now()  # Pega o momento da saída
    
    if not placa:
        resultado_label.configure(text="Por favor, insira a placa do veículo.")
    elif placa not in banco_de_dados:
        resultado_label.configure(text=f"Veículo com placa {placa} não encontrado.")
    else:
        hora_entrada = banco_de_dados[placa]['entrada']
        nome_proprietario = banco_de_dados[placa]['nome']
        tempo_permanencia = (agora - hora_entrada).total_seconds() / 3600  # Tempo em horas
        valor_total = tempo_permanencia * taxa_por_hora
        
        recibo = (f"\n=== Recibo ===\n"
                  f"Nome: {nome_proprietario}\n"
                  f"Placa: {placa}\n"
                  f"Entrada: {hora_entrada.strftime('%H:%M:%S')}\n"
                  f"Saída: {agora.strftime('%H:%M:%S')}\n"
                  f"Tempo: {tempo_permanencia:.2f} horas\n"
                  f"Valor a pagar: R$ {valor_total:.2f}\n"
                  f"==============================")
        
        # Abre a janela de pagamento
        abrir_janela_pagamento(valor_total, placa)
        
        entry_placa.delete(0, ctk.END)

# Função para exibir uma notificação de "Pagamento realizado com sucesso"
def exibir_notificacao_sucesso():
    # Cria uma janela modal
    janela_notificacao = ctk.CTkToplevel(app)
    janela_notificacao.geometry("300x150")
    janela_notificacao.title("Sucesso")

    # Rótulo com a mensagem de sucesso
    label_sucesso = ctk.CTkLabel(janela_notificacao, text="Pagamento realizado com sucesso!", font=("Arial", 16))
    label_sucesso.pack(pady=40)

    # Fecha a janela automaticamente após 3 segundos
    janela_notificacao.after(3000, janela_notificacao.destroy)

# Seção Pagamento - Sistema que simula Pagamentos

# Função para simular o pagamento
def abrir_janela_pagamento(valor_total, placa):
    janela_pagamento = ctk.CTkToplevel(app)
    janela_pagamento.geometry("300x250")
    janela_pagamento.title("Pagamento")
    
    label_pagamento = ctk.CTkLabel(janela_pagamento, text=f"Valor a pagar: R$ {valor_total:.2f}", font=("Arial", 16))
    label_pagamento.pack(pady=20)
    
    forma_pagamento_var = ctk.StringVar(value="Cartão")
    
    # Opção de pagamento
    pagamento_label = ctk.CTkLabel(janela_pagamento, text="Forma de pagamento:", font=("Arial", 14))
    pagamento_label.pack(pady=10)
    
    botao_cartao = ctk.CTkRadioButton(janela_pagamento, text="Cartão", variable=forma_pagamento_var, value="Cartão")
    botao_cartao.pack(pady=5)
    
    botao_dinheiro = ctk.CTkRadioButton(janela_pagamento, text="Dinheiro", variable=forma_pagamento_var, value="Dinheiro")
    botao_dinheiro.pack(pady=5)
    
    # Botão para finalizar o pagamento
    botao_finalizar = ctk.CTkButton(janela_pagamento, text="Finalizar Pagamento", command=lambda: finalizar_pagamento(janela_pagamento, forma_pagamento_var.get(), valor_total, placa))
    botao_finalizar.pack(pady=20)

# Função que simula a finalização do pagamento
def finalizar_pagamento(janela_pagamento, forma_pagamento, valor_total, placa):
    global vagas_disponiveis
    resultado_pagamento = f"Pagamento de R$ {valor_total:.2f} realizado com {forma_pagamento}."
    resultado_label.configure(text=resultado_pagamento)
    
    # Aumenta o número de vagas disponíveis e remove o veículo do banco de dados
    if placa in banco_de_dados:
        vagas_disponiveis += 1
        del banco_de_dados[placa]
        atualizar_vagas()
        atualizar_tabela()

    # Fecha a janela de pagamento
    janela_pagamento.destroy()
    
    # Exibe a notificação de sucesso
    exibir_notificacao_sucesso()

# Função para encerrar o sistema
def sair():
    app.quit()

# Seção Interface - Configuração da interface customtkinter

# Configuração da interface gráfica
app = ctk.CTk()
app.geometry("600x600")
app.title("Sistema de Estacionamento")

ctk.set_appearance_mode("dark")  # Modo de aparência
ctk.set_default_color_theme("blue")  # Tema de cor

# Rótulo para o título
titulo_label = ctk.CTkLabel(app, text="Sistema de Estacionamento", font=("Arial", 24, "bold"))
titulo_label.pack(pady=20)

# Exibição das vagas disponíveis
vagas_label = ctk.CTkLabel(app, text=f"Vagas disponíveis: {vagas_disponiveis}", font=("Arial", 16))
vagas_label.pack(pady=10)

# Frame para organizar a entrada e os botões
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Rótulo e campo de entrada para o nome do proprietário
nome_label = ctk.CTkLabel(frame, text="Nome do Proprietário:", font=("Arial", 16))
nome_label.pack(pady=10)

entry_nome = ctk.CTkEntry(frame, width=250)
entry_nome.pack(pady=10)

# Rótulo e campo de entrada para a placa do veículo
placa_label = ctk.CTkLabel(frame, text="Placa do Veículo:", font=("Arial", 16))
placa_label.pack(pady=10)

entry_placa = ctk.CTkEntry(frame, width=250)
entry_placa.pack(pady=10)

# Botões para registrar entrada e saída
botao_entrada = ctk.CTkButton(frame, text="Registrar Entrada", width=150, command=registrar_entrada)
botao_entrada.pack(pady=10)

botao_saida = ctk.CTkButton(frame, text="Registrar Saída", width=150, command=registrar_saida)
botao_saida.pack(pady=10)

# Rótulo para mostrar os resultados
resultado_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
resultado_label.pack(pady=20)

# Tabela para exibir os registros de entrada
tabela = ttk.Treeview(app, columns=("Nome", "Placa", "Hora de Entrada"), show="headings")
tabela.heading("Nome", text="Nome")
tabela.heading("Placa", text="Placa")
tabela.heading("Hora de Entrada", text="Hora de Entrada")
tabela.pack(pady=20)

# Botão para sair do aplicativo
botao_sair = ctk.CTkButton(app, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Executando a interface gráfica
app.mainloop()
