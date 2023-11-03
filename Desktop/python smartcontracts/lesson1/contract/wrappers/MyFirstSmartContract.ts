import { Address, beginCell, Cell, Contract, contractAddress, ContractProvider, Sender, SendMode } from 'ton-core';

export type MyFirstSmartContractConfig = {};

export function myFirstSmartContractConfigToCell(config: MyFirstSmartContractConfig): Cell {
    return beginCell().endCell();
}

export class MyFirstSmartContract implements Contract {
    constructor(readonly address: Address, readonly init?: { code: Cell; data: Cell }) {}

    static createFromAddress(address: Address) {
        return new MyFirstSmartContract(address);
    }

    static createFromConfig(config: MyFirstSmartContractConfig, code: Cell, workchain = 0) {
        const data = myFirstSmartContractConfigToCell(config);
        const init = { code, data };
        return new MyFirstSmartContract(contractAddress(workchain, init), init);
    }

    async sendDeploy(provider: ContractProvider, via: Sender, value: bigint) {
        await provider.internal(via, {
            value,
            sendMode: SendMode.PAY_GAS_SEPARATELY,
            body: beginCell().endCell(),
        });
    }
}
