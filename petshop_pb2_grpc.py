# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import petshop_pb2 as petshop__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in petshop_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PetShopStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddCliente = channel.unary_unary(
                '/PetShop/AddCliente',
                request_serializer=petshop__pb2.Cliente.SerializeToString,
                response_deserializer=petshop__pb2.Response.FromString,
                _registered_method=True)
        self.AddPet = channel.unary_unary(
                '/PetShop/AddPet',
                request_serializer=petshop__pb2.Pet.SerializeToString,
                response_deserializer=petshop__pb2.Response.FromString,
                _registered_method=True)
        self.AddServico = channel.unary_unary(
                '/PetShop/AddServico',
                request_serializer=petshop__pb2.Servico.SerializeToString,
                response_deserializer=petshop__pb2.Response.FromString,
                _registered_method=True)
        self.ListClientes = channel.unary_unary(
                '/PetShop/ListClientes',
                request_serializer=petshop__pb2.Empty.SerializeToString,
                response_deserializer=petshop__pb2.ClienteList.FromString,
                _registered_method=True)
        self.ListPets = channel.unary_unary(
                '/PetShop/ListPets',
                request_serializer=petshop__pb2.Empty.SerializeToString,
                response_deserializer=petshop__pb2.PetList.FromString,
                _registered_method=True)
        self.ListServicos = channel.unary_unary(
                '/PetShop/ListServicos',
                request_serializer=petshop__pb2.Empty.SerializeToString,
                response_deserializer=petshop__pb2.ServicoList.FromString,
                _registered_method=True)
        self.GetGrupo = channel.unary_unary(
                '/PetShop/GetGrupo',
                request_serializer=petshop__pb2.Empty.SerializeToString,
                response_deserializer=petshop__pb2.Grupo.FromString,
                _registered_method=True)


class PetShopServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddCliente(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddServico(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListClientes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListServicos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGrupo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PetShopServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddCliente': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCliente,
                    request_deserializer=petshop__pb2.Cliente.FromString,
                    response_serializer=petshop__pb2.Response.SerializeToString,
            ),
            'AddPet': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPet,
                    request_deserializer=petshop__pb2.Pet.FromString,
                    response_serializer=petshop__pb2.Response.SerializeToString,
            ),
            'AddServico': grpc.unary_unary_rpc_method_handler(
                    servicer.AddServico,
                    request_deserializer=petshop__pb2.Servico.FromString,
                    response_serializer=petshop__pb2.Response.SerializeToString,
            ),
            'ListClientes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListClientes,
                    request_deserializer=petshop__pb2.Empty.FromString,
                    response_serializer=petshop__pb2.ClienteList.SerializeToString,
            ),
            'ListPets': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPets,
                    request_deserializer=petshop__pb2.Empty.FromString,
                    response_serializer=petshop__pb2.PetList.SerializeToString,
            ),
            'ListServicos': grpc.unary_unary_rpc_method_handler(
                    servicer.ListServicos,
                    request_deserializer=petshop__pb2.Empty.FromString,
                    response_serializer=petshop__pb2.ServicoList.SerializeToString,
            ),
            'GetGrupo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGrupo,
                    request_deserializer=petshop__pb2.Empty.FromString,
                    response_serializer=petshop__pb2.Grupo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PetShop', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('PetShop', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PetShop(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddCliente(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/AddCliente',
            petshop__pb2.Cliente.SerializeToString,
            petshop__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddPet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/AddPet',
            petshop__pb2.Pet.SerializeToString,
            petshop__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddServico(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/AddServico',
            petshop__pb2.Servico.SerializeToString,
            petshop__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListClientes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/ListClientes',
            petshop__pb2.Empty.SerializeToString,
            petshop__pb2.ClienteList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListPets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/ListPets',
            petshop__pb2.Empty.SerializeToString,
            petshop__pb2.PetList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListServicos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/ListServicos',
            petshop__pb2.Empty.SerializeToString,
            petshop__pb2.ServicoList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetGrupo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PetShop/GetGrupo',
            petshop__pb2.Empty.SerializeToString,
            petshop__pb2.Grupo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
