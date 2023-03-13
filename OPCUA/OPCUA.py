from asyncua import Client, ua

# https://github.com/FreeOpcUa/opcua-client-gui/tree/master/uaclient
# https://pypi.org/project/asyncua/

class client:
    
    def __init__(
            self, 
            url:str, 
            read_node:str = None, 
            write_node:str = None,
            application_uri:str = "urn:freeopcua:client-gui"
        ):
        self.application_uri = application_uri
        self.url = url
        self.read_node = read_node
        self.write_node = write_node
        self.client = None
        
    async def get_endpoints(self):
        if self.client is not None:
            self.disconnect()
        self.client = Client(url=self.url, timeout=2)
        edps = await self.client.connect_and_get_server_endpoints()
        content = f"{edps}"
        content.split(", ")
        return content

    async def connect(self):

        if self.client is not None:
            self.disconnect()
        self.client = Client(url=self.url)
        await self.client.connect()
        print(f"Connected to OPCUA server in Url: {self.url}")

        return self.client
        
    async def disconnect(self):
        self.checkConnection()
        await self.client.disconnect()
        
        print(f"Disconnected from OPCUA Server in Url: {self.url}")
    
    def checkConnection(self):
        if self.client is None:
            raise ValueError ("Client is not connected.")


    async def read_input_value(self):

        self.checkConnection()

        client_node = self.client.get_node(self.read_node)
        client_node_value = await client_node.get_value()
        print(f"Value of : {str(self.read_node)}' : ' {str(client_node_value)}")
        return client_node_value

    def write_value_int(self):

        self.checkConnection()

        client_node = self.client.get_node(self.read_node)
        client_node_value = self.write_node
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
        client_node.set_value(client_node_dv)

    def write_value_bool(self):

        self.checkConnection()

        client_node = self.client.get_node(self.read_node)
        client_node_value = self.write_node
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
        client_node.set_value(client_node_dv)


              

