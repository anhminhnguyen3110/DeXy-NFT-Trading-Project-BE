contract = [
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "owners",
                "type": "address[]",
            },
            {
                "internalType": "uint32[]",
                "name": "products",
                "type": "uint32[]",
            },
            {
                "internalType": "uint256[]",
                "name": "prices",
                "type": "uint256[]",
            },
        ],
        "name": "batchBuy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "uint32", "name": "product", "type": "uint32"},
            {"internalType": "uint256", "name": "price", "type": "uint256"},
        ],
        "name": "buy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
    },
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint32",
                "name": "transactionId",
                "type": "uint32",
            },
            {
                "indexed": False,
                "internalType": "uint32",
                "name": "item",
                "type": "uint32",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "buyer",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
        ],
        "name": "TransactionAccepted",
        "type": "event",
    },
    {
        "inputs": [
            {
                "internalType": "uint32[]",
                "name": "transactionsIds",
                "type": "uint32[]",
            }
        ],
        "name": "getTransactions",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "from",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "to",
                        "type": "address",
                    },
                    {
                        "internalType": "uint32",
                        "name": "product",
                        "type": "uint32",
                    },
                    {
                        "internalType": "uint256",
                        "name": "price",
                        "type": "uint256",
                    },
                    {
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256",
                    },
                ],
                "internalType": "struct Purchasing.TransactionDetails[]",
                "name": "transactionList",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
]
