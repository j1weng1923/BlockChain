// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract LuckyDrawWinnerOnly {
    address public owner;
    mapping(uint => string) public winners;
    uint public currentRound;

    event WinnerSet(string winnerName, uint round);
    event NewRoundStarted(uint round);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        currentRound = 1;
    }

    // Hàm lưu người thắng vòng hiện tại và tự tăng vòng mới
    function setWinnerAndNextRound(string calldata winnerName) public onlyOwner {
        require(bytes(winners[currentRound]).length == 0, "Winner already set");
        winners[currentRound] = winnerName;
        emit WinnerSet(winnerName, currentRound);

        currentRound++;
        emit NewRoundStarted(currentRound);
    }

    function getWinnerOfRound(uint round) public view returns (string memory) {
        return winners[round];
    }

    function getCurrentRound() public view returns (uint) {
        return currentRound;
    }
}
