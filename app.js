var api = require('etherscan-api').init('api-token');
var balance = api.account.balance('0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae');
balance.then(function(balanceData){
  console.log(balanceData);
});

//1 Make mongodb containing all the ether addresses from https://docs.google.com/spreadsheets/d/1eOh_lT8vKj0IuUFxOftiSjcItViv0ZGHphYApXHJhoM/edit#gid=0
//2 Retrieve balances of all addresses and save them into db
//3 Rither pull balances every x times or watch for new transactions
//4 Make a tweet