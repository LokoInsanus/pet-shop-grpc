import tkinter as tk
from tkinter import ttk, messagebox
import grpc
import petshop_pb2
import petshop_pb2_grpc

canal = grpc.insecure_channel('localhost:50051')
stub = petshop_pb2_grpc.PetShopStub(canal)

class AplicativoPetShop:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Shop")

        # Abas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=1, fill="both")

        self.criar_aba_cliente()
        self.criar_aba_pet()
        self.criar_aba_servico()
        self.criar_abas_listar()

    def criar_aba_cliente(self):
        self.aba_cliente = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_cliente, text="Adicionar Cliente")

        campos_cliente = [
            ("Nome", "nome_cliente"),
            ("Email", "email_cliente"),
            ("Rua", "rua_cliente"),
            ("Bairro", "bairro_cliente"),
            ("Número da Casa", "numero_cliente"),
            ("Telefone", "telefone_cliente"),
            ("CPF", "cpf_cliente"),
        ]

        self.entries_cliente = {}

        for i, (label_text, var_name) in enumerate(campos_cliente):
            ttk.Label(self.aba_cliente, text=f"{label_text}:").grid(row=i, column=0)
            entry = ttk.Entry(self.aba_cliente)
            entry.grid(row=i, column=1)
            self.entries_cliente[var_name] = entry

        ttk.Button(self.aba_cliente, text="Adicionar Cliente", command=self.adicionar_cliente).grid(row=len(campos_cliente), column=0, columnspan=2)

    def adicionar_cliente(self):
        dados_cliente = {var_name: entry.get() for var_name, entry in self.entries_cliente.items()}
        cliente = petshop_pb2.Cliente(
            nome=dados_cliente["nome_cliente"],
            email=dados_cliente["email_cliente"],
            rua=dados_cliente["rua_cliente"],
            bairro=dados_cliente["bairro_cliente"],
            numero_casa=dados_cliente["numero_cliente"],
            telefone=dados_cliente["telefone_cliente"],
            cpf=dados_cliente["cpf_cliente"]
        )
        resposta = stub.AddCliente(cliente)
        messagebox.showinfo("Informacao", resposta.message)

    def criar_aba_pet(self):
        self.aba_pet = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_pet, text="Adicionar Pet")

        campos_pet = [
            ("Nome", "nome_pet"),
            ("Tipo de Animal", "animal_pet"),
            ("Raça", "raca_pet"),
            ("RGA", "rga_pet"),
            ("Nome do Dono", "dono_nome_pet"),
        ]

        self.entries_pet = {}

        for i, (label_text, var_name) in enumerate(campos_pet):
            ttk.Label(self.aba_pet, text=f"{label_text}:").grid(row=i, column=0)
            entry = ttk.Entry(self.aba_pet)
            entry.grid(row=i, column=1)
            self.entries_pet[var_name] = entry

        ttk.Button(self.aba_pet, text="Adicionar Pet", command=self.adicionar_pet).grid(row=len(campos_pet), column=0, columnspan=2)

    def adicionar_pet(self):
        dados_pet = {var_name: entry.get() for var_name, entry in self.entries_pet.items()}
        dono = petshop_pb2.Cliente(nome=dados_pet["dono_nome_pet"])  # Apenas o nome do dono
        pet = petshop_pb2.Pet(
            nome=dados_pet["nome_pet"],
            animal=dados_pet["animal_pet"],
            raca=dados_pet["raca_pet"],
            rga=dados_pet["rga_pet"],
            dono=dono
        )
        resposta = stub.AddPet(pet)
        messagebox.showinfo("Informação", resposta.message)

    def criar_aba_servico(self):
        self.aba_servico = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_servico, text="Agendar Serviço")

        ttk.Label(self.aba_servico, text="Nome do Pet:").grid(row=0, column=0)
        self.nome_pet_servico = ttk.Entry(self.aba_servico)
        self.nome_pet_servico.grid(row=0, column=1)

        ttk.Label(self.aba_servico, text="Serviço:").grid(row=1, column=0)
        self.tipo_servico = ttk.Entry(self.aba_servico)
        self.tipo_servico.grid(row=1, column=1)

        ttk.Label(self.aba_servico, text="Data:").grid(row=2, column=0)
        self.data_servico = ttk.Entry(self.aba_servico)
        self.data_servico.grid(row=2, column=1)

        ttk.Button(self.aba_servico, text="Agendar", command=self.agendar_servico).grid(row=3, column=0, columnspan=2)

    def agendar_servico(self):
        nome_pet = self.nome_pet_servico.get()
        servico = self.tipo_servico.get()
        data = self.data_servico.get()
        resposta = stub.AddServico(petshop_pb2.Servico(pet_nome=nome_pet, servico=servico, data=data))
        messagebox.showinfo("Informação", resposta.message)

    def criar_abas_listar(self):
        self.aba_listar_clientes = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_listar_clientes, text="Listar Clientes")

        self.botao_atualizar_clientes = ttk.Button(self.aba_listar_clientes, text="Atualizar", command=self.listar_clientes)
        self.botao_atualizar_clientes.pack()

        self.texto_clientes = tk.Text(self.aba_listar_clientes, height=15, width=50)
        self.texto_clientes.pack()

        self.aba_listar_pets = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_listar_pets, text="Listar Pets")

        self.botao_atualizar_pets = ttk.Button(self.aba_listar_pets, text="Atualizar", command=self.listar_pets)
        self.botao_atualizar_pets.pack()

        self.texto_pets = tk.Text(self.aba_listar_pets, height=15, width=50)
        self.texto_pets.pack()

        self.aba_listar_servicos = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_listar_servicos, text="Listar Serviços")

        self.botao_atualizar_servicos = ttk.Button(self.aba_listar_servicos, text="Atualizar", command=self.listar_servicos)
        self.botao_atualizar_servicos.pack()

        self.texto_servicos = tk.Text(self.aba_listar_servicos, height=15, width=50)
        self.texto_servicos.pack()

    def listar_clientes(self):
        resposta = stub.ListClientes(petshop_pb2.Empty())
        self.texto_clientes.delete(1.0, tk.END)
        for cliente in resposta.clientes:
            self.texto_clientes.insert(
                tk.END,
                f"Nome: {cliente.nome}, Email: {cliente.email}, Rua: {cliente.rua}, Bairro: {cliente.bairro}, "
                f"Número: {cliente.numero_casa}, Telefone: {cliente.telefone}, CPF: {cliente.cpf}\n"
            )

    def listar_pets(self):
        resposta = stub.ListPets(petshop_pb2.Empty())
        self.texto_pets.delete(1.0, tk.END)
        for pet in resposta.pets:
            self.texto_pets.insert(tk.END, f"Nome: {pet.nome}, Animal: {pet.animal}, Dono: {pet.dono.nome}, Raca: {pet.raca}, RGA: {pet.rga}\n")

    def listar_servicos(self):
        resposta = stub.ListServicos(petshop_pb2.Empty())
        self.texto_servicos.delete(1.0, tk.END)
        for servico in resposta.servicos:
            self.texto_servicos.insert(tk.END, f"Nome do Pet: {servico.pet_nome}, Serviço: {servico.servico}, Data: {servico.data}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoPetShop(root)
    root.mainloop()
