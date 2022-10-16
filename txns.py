from web3 import Web3
import json
from style import style


class TXN():
    def __init__(self, token_address, quantity):
        self.w3 = self.connect()
        self.address, self.private_key = self.setup_address()
        self.token_address = Web3.toChecksumAddress(token_address)
        self.token_contract = self.setup_token()
        self.swapper_address, self.swapper = self.setup_swapper()
        self.slippageBUY, self.slippageSELL = self.setupSlippage()
        self.quantity = quantity 
        self.gas_price = self.setupGas()

    def connect(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        if keys["RPC"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["RPC"]))
        else:
            w3 = Web3(Web3.HTTPProvider(keys["RPC"]))
        return w3

    def setupGas(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        return int(keys['GAS'] * (10**9))

    def setup_address(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        if len(keys["metamask_address"]) <= 41:
            print(style.RED +"Set your Address in the keys.json file!" + style.RESET)
        if len(keys["metamask_private_key"]) <= 42:
            print(style.RED +"Set your PrivateKey in the keys.json file!"+ style.RESET)
        return keys["metamask_address"], keys["metamask_private_key"]

    def setupSlippage(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        return keys['MaxBuyTax'], keys['MaxSellTax']

    def get_token_decimals(self):
        return self.token_contract.functions.decimals().call()

    def getBlockHigh(self):
        return self.w3.eth.block_number

    def setup_swapper(self):
        swapper_address = Web3.toChecksumAddress("0x1Ba0c582354c628Ab621b1bd0328528Fbb8d80fC") 
        with open("./abis/BSC_Swapper.json") as f:
            contract_abi = json.load(f)
        swapper = self.w3.eth.contract(address=swapper_address, abi=contract_abi)
        return (swapper_address, swapper)

    def setup_token(self):
        with open("./abis/bep20_abi_token.json") as f:
            contract_abi = json.load(f)
        token_contract = self.w3.eth.contract(address=self.token_address, abi=contract_abi)
        return token_contract

    def get_token_balance(self): 
        return self.token_contract.functions.balanceOf(self.address).call() / (10 ** self.token_contract.functions.decimals().call())

    def checkToken(self):
        tokenInfos = self.swapper.functions.getTokenInfos(self.token_address).call()
        buy_tax = round((tokenInfos[0] - tokenInfos[1]) / tokenInfos[0] * 100) 
        sell_tax = round((tokenInfos[2] - tokenInfos[3]) / tokenInfos[2] * 100)
        if tokenInfos[5] and tokenInfos[6] == True:
            honeypot = False
        else:
            honeypot = True
        return buy_tax, sell_tax, honeypot

    def estimateGas(self, txn):
        gas = self.w3.eth.estimateGas({
                    "from": txn['from'],
                    "to": txn['to'],
                    "value": txn['value'],
                    "data": txn['data']})
        gas = gas + (gas / 10) # Adding 1/10 from gas to gas!
        return gas

    def getOutputfromBNBtoToken(self):
        call = self.swapper.functions.getOutputfromBNBtoToken(
            self.token_address,
            int(self.quantity * (10**18)),
            ).call()
        Amount = call[0]
        Way = call[1]
        return Amount, Way

    def getOutputfromTokentoBNB(self):
        call = self.swapper.functions.getOutputfromTokentoBNB(
            self.token_address,
            int(self.token_contract.functions.balanceOf(self.address).call()),
            ).call()
        Amount = call[0]
        Way = call[1]
        return Amount , Way

    def buy_token(self):
        self.quantity = self.quantity * (10**18)
        txn = self.swapper.functions.fromBNBtoToken(
            self.token_address,
            self.slippageBUY
        ).buildTransaction(
            {'from': self.address, 
            'gas': 480000,
            'gasPrice': self.gas_price,
            'nonce': self.w3.eth.getTransactionCount(self.address), 
            'value': int(self.quantity)}
            )
        txn.update({ 'gas' : int(self.estimateGas(txn))})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.private_key
        )
        txn = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(style.GREEN + "\nBUY Hash:",txn.hex() + style.RESET)
        txn_receipt = self.w3.eth.waitForTransactionReceipt(txn)
        if txn_receipt["status"] == 1: return True,style.GREEN +"\nBUY Transaction Successfull!" + style.RESET
        else: return False, style.RED +"\nBUY Transaction Faild!" + style.RESET

    def is_approve(self):
        Approve = self.token_contract.functions.allowance(self.address ,self.swapper_address).call()
        Aproved_quantity = self.token_contract.functions.balanceOf(self.address).call()
        if int(Approve) <= int(Aproved_quantity):
            return False
        else:
            return True

    def approve(self):
        if self.is_approve() == False:
            txn = self.token_contract.functions.approve(
                self.swapper_address,
                115792089237316195423570985008687907853269984665640564039457584007913129639935 # Max Approve
            ).buildTransaction(
                {'from': self.address, 
                'gas': 100000,
                'gasPrice': self.gas_price,
                'nonce': self.w3.eth.getTransactionCount(self.address), 
                'value': 0}
                )
            txn.update({ 'gas' : int(self.estimateGas(txn))})
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.private_key
            )
            txn = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print(style.GREEN + "\nApprove Hash:",txn.hex()+style.RESET)
            txn_receipt = self.w3.eth.waitForTransactionReceipt(txn)   
            if txn_receipt["status"] == 1: return True,style.GREEN +"\nApprove Successfull!"+ style.RESET
            else: return False, style.RED +"\nApprove Transaction Faild!"+ style.RESET
        else:
            return True, style.GREEN +"\nAllready approved!"+ style.RESET

    def sell_tokens(self):
        self.approve()
        txn = self.swapper.functions.fromTokentoBNB(
            self.token_address,
            int(self.token_contract.functions.balanceOf(self.address).call()),
            self.slippageSELL
        ).buildTransaction(
            {'from': self.address, 
            'gas': 550000,
            'gasPrice': self.gas_price,
            'nonce': self.w3.eth.getTransactionCount(self.address), 
            'value': 0}
            )
        txn.update({ 'gas' : int(self.estimateGas(txn))})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.private_key
        )
        txn = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(style.GREEN + "\nSELL Hash :",txn.hex() + style.RESET)
        txn_receipt = self.w3.eth.waitForTransactionReceipt(txn)
        if txn_receipt["status"] == 1: return True,style.GREEN +"\nSELL Transaction Successfull!" + style.RESET
        else: return False, style.RED +"\nSELL Transaction Faild!" + style.RESET
