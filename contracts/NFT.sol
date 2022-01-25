// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "hardhat/console.sol";

contract KajNFT is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("KajNFT", "KAJ") {
        console.log("This is a KajNFT contract");
    }

    function generateKajNFT() public {
        uint256 newItemId = _tokenIds.current();

        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, "https://jsonkeeper.com/b/DLLY");
        _tokenIds.increment();
        console.log(
            "A KajNFT w/ ID %s has been minted to %s",
            newItemId,
            msg.sender
        );
    }
}
