pragma solidity ^0.7.0;

contract Bank {
    struct client_details {
        uint client_id;
        address client_address;
        uint client_balance;
    }

    client_details[] clients;
    address payable manager;
    uint counter = 0;

    modifier onlyManager {
        require(msg.sender == manager, "Only for manager");
        _;
    }

    modifier onlyClient {
        bool isClient = false;
        for (uint i = 0; i < clients.length; i++) {
            if (clients[i].client_address == msg.sender) {
                isClient = true;
            }
        }
        require(isClient, "Only for clients");
        _;
    }

    receive() external payable { }

    function setManager(address payable manaddr) public {
        manager = manaddr;
    }

    function joinClient() public payable {
        clients.push(client_details(counter, msg.sender, address(msg.sender).balance));
    }

    function deposit() public payable {
        payable(address(this)).transfer(msg.value);
    }

    function withdraw(uint amount) public payable {
        payable(address(msg.sender)).transfer(amount * 1 ether);
    }

    function getBalanceContract() public view returns(uint) {
        return address(this).balance;
    }
}
