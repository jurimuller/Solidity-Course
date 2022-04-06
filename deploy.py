# Import needed functions
# needed to: install_solc("0.6.0")
from solcx import compile_standard, install_solc
import json
from web3 import Web3

# -----Open source .sol-----
with open("./SimpleStorage.sol", "r") as myFile:
    simple_storage_file = myFile.read()

# -----Compile SimpleStorage.sol-----
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

# -----Export compiled_sol to .json-----
with open("compiled_code.json", "w") as myFile:
    json.dump(compiled_sol, myFile)

# To deploy to chain, need bytecode & ABI

# Get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# Get ABI
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]

# We want to deploy to an environment --> Ganache (simulated, private blockchain for testing - single node)
