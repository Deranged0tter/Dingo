from havoc.service import HavocService
from havoc.agent import *

class CommandExit(Command):
    Name = "exit"
    Description = "tells agent to exit"
    Help = "lol no"
    NeedAdmin = False
    Mitr = []
    Params = []

    def job_generate(self, arguments: dict) -> bytes:
        packer = Packer()
        data = {"TaskCommand":"exit", "TaskFile":"", "TaskArgument":""}
        packer.add_data(data)
        return packer.buffer

# Agent Class
class dingo(AgentType):
    Name = "dingo"
    Author = "Deranged0tter"
    Version = "0.1"
    Description = f"""3rd party agent for HavocC2"""
    MagicValue = 0x64696E67

    Arch = [
        "x64",
        "x86",
    ]

    Formats = [
        {
            "Name": "linux binary",
            "Extension": "",
        },
        {
            "Name": "windows executable",
            "Extension": "exe",
        },
    ]

    BuildingConfig = {
        "Sleep": "10"
    }

    Commands = [
        CommandExit(),
    ]

    def generate(self, config: dict) -> None:
        self.builder_send_message(config['ClientID'], "Info", f"test")

def main():
    Havoc_Dingo = dingo()
    Havoc_Service = HavocService(
        endpoint="wss://localhost:40056/service-endpoint",
        password="service-password"
    )

    Havoc_Service.register_agent(Havoc_Dingo)

    return

if __name__ == "__main__":
    main()