from concurrent import futures
import grpc
import petshop_pb2
import petshop_pb2_grpc

clientes = []
pets = []
servicos = []

class ServidorPetShop(petshop_pb2_grpc.PetShopServicer):
    def AddCliente(self, request, context):
        clientes.append({
            "nome": request.nome,
            "email": request.email,
            "rua": request.rua,
            "bairro": request.bairro,
            "numero_casa": request.numero_casa,
            "telefone": request.telefone,
            "cpf": request.cpf
        })
        return petshop_pb2.Response(message="Cliente adicionado com sucesso!")

    def AddPet(self, request, context):
        pets.append({
            "nome": request.nome,
            "animal": request.animal,
            "raca": request.raca,
            "rga": request.rga,
            "dono": {
                "nome": request.dono.nome,
                "email": request.dono.email,
                "rua": request.dono.rua,
                "bairro": request.dono.bairro,
                "numero_casa": request.dono.numero_casa,
                "telefone": request.dono.telefone,
                "cpf": request.dono.cpf
            }
        })
        return petshop_pb2.Response(message="Pet adicionado com sucesso!")

    def AddServico(self, request, context):
        servicos.append({
            "pet_nome": request.pet_nome,
            "servico": request.servico,
            "data": request.data
        })
        return petshop_pb2.Response(message="Serviço agendado com sucesso!")

    def ListClientes(self, request, context):
        lista_clientes = petshop_pb2.ClienteList()
        for cliente in clientes:
            lista_clientes.clientes.add(
                nome=cliente["nome"],
                email=cliente["email"],
                rua=cliente["rua"],
                bairro=cliente["bairro"],
                numero_casa=cliente["numero_casa"],
                telefone=cliente["telefone"],
                cpf=cliente["cpf"]
            )
        return lista_clientes

    def ListPets(self, request, context):
        lista_pets = petshop_pb2.PetList()
        for pet in pets:
            lista_pets.pets.add(
                nome=pet["nome"],
                animal=pet["animal"],
                raca=pet["raca"],
                rga=pet["rga"],
                dono=petshop_pb2.Cliente(
                    nome=pet["dono"]["nome"],
                    email=pet["dono"]["email"],
                    rua=pet["dono"]["rua"],
                    bairro=pet["dono"]["bairro"],
                    numero_casa=pet["dono"]["numero_casa"],
                    telefone=pet["dono"]["telefone"],
                    cpf=pet["dono"]["cpf"]
                )
            )
        return lista_pets
    
    def ListServicos(self, request, context):
        lista_servicos = petshop_pb2.ServicoList()
        for servico in servicos:
            lista_servicos.servicos.add(
                pet_nome=servico["pet_nome"],
                servico=servico["servico"],
                data=servico["data"]
            )
        return lista_servicos

def iniciar_servidor():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    petshop_pb2_grpc.add_PetShopServicer_to_server(ServidorPetShop(), servidor)
    servidor.add_insecure_port('[::]:50051')
    print("Servidor rodando na porta 50051")
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    iniciar_servidor()
