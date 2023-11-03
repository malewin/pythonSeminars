import { Blockchain, SandboxContract } from '@ton-community/sandbox';
import { Cell, toNano } from 'ton-core';
import { MyFirstSmartContract } from '../wrappers/MyFirstSmartContract';
import '@ton-community/test-utils';
import { compile } from '@ton-community/blueprint';

describe('MyFirstSmartContract', () => {
    let code: Cell;

    beforeAll(async () => {
        code = await compile('MyFirstSmartContract');
    });

    let blockchain: Blockchain;
    let myFirstSmartContract: SandboxContract<MyFirstSmartContract>;

    beforeEach(async () => {
        blockchain = await Blockchain.create();

        myFirstSmartContract = blockchain.openContract(MyFirstSmartContract.createFromConfig({}, code));

        const deployer = await blockchain.treasury('deployer');

        const deployResult = await myFirstSmartContract.sendDeploy(deployer.getSender(), toNano('0.05'));

        expect(deployResult.transactions).toHaveTransaction({
            from: deployer.address,
            to: myFirstSmartContract.address,
            deploy: true,
            success: true,
        });
    });

    it('should deploy', async () => {
        // the check is done inside beforeEach
        // blockchain and myFirstSmartContract are ready to use
    });
});
