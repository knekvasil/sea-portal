// deploy.js

async function main() {
  const nftContractFactory = await hre.ethers.getContractFactory("KajNFT");
  const nftContract = await nftContractFactory.deploy();
  await nftContract.deployed();
  console.log("Contract deployed to:", nftContract.address);

  let txn = await nftContract.generateKajNFT();
  await txn.wait();
  console.log("Minted NFT #1");
}

async function runMain() {
  try {
    await main();
    process.exit(0);
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
}

runMain();
