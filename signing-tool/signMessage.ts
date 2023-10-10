const web3_1 = require("web3");
const web3 = new web3_1("https://bsc-dataseed1.defibit.io/");

export const signMessage = async (message: string, privateKey: string) => {

    const signature = await web3.eth.accounts.sign(message,privateKey);
    return signature
}

signMessage('Welcome to DeXy Trading Platform, User! Click "Sign" to sign in. No password is needed!', "5d0e02a3a62df6cdb1b2d47cf70fc642cbcbdb716740cd4e6d59c82c0b18302d")
    .then(console.log)