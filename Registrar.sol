// Be name Khoda
// Bime Abolfazl
// SPDX-License-Identifier: MIT

// Primary Author(s)
// Hassan Abbasi: https://github.com/mikoronjoo


pragma solidity ^0.8.16;


contract Registrar {

    struct Document {
        string title;
        address author;
        uint256 timestamp;
    }

    mapping(bytes32 => Document) public documents;

    event documentRegistered(bytes32 fileHash, string title, address author);
    event titleChanged(bytes32 fileHash, string newTitle);

    constructor() {
    }

    function register(bytes32 hash_, address author, string memory title) public {
        require(documents[hash_].timestamp == 0, "Registrar.register :: This hash is already registered");
        documents[hash_] = Document(title, author, block.timestamp);
        emit documentRegistered(hash_, title, author);
    }

    function selfRegister(bytes32 hash_, string memory title) external {
        register(hash_, msg.sender, title);
    }

    function updateTitle(bytes32 hash_, string memory newTitle) external {
        require(documents[hash_].timestamp != 0, "Registrar.register :: The hash is not found");
        documents[hash_].title = newTitle;
        emit titleChanged(hash_, newTitle);
    }
}

// Dar panah Khoda
