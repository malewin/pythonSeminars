import { toNano } from 'ton-core';
import { MyFirstSmartContract } from '../wrappers/MyFirstSmartContract';
import { compile, NetworkProvider } from '@ton-community/blueprint';

export async function run(provider: NetworkProvider) {
    const myFirstSmartContract = provider.open(MyFirstSmartContract.createFromConfig({}, await compile('MyFirstSmartContract')));

    await myFirstSmartContract.sendDeploy(provider.sender(), toNano('0.05'));

    await provider.waitForDeploy(myFirstSmartContract.address);

    // run methods on `myFirstSmartContract`
}
