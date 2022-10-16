<h2 align="center">⭐️ ETH-BSC Web3 bot 2022-V1 (MAC WINDOWS ANDROID LINUX)⭐️ </h2>
<h3 align="center">⭐️ AUTO BUY TOKEN ON LAUNCH AFTER ADD LIQUIDITY ⭐️</h3>

<h3 align="center">⭐️ First SNIPER BOT for MAC & ANDROID & WINDOWS with honeypot detector ⭐️</h3>
 
#### VERSION 2 CHANGES : 
#### 4X Faster with cython
#### Fix bug BUY token After add LIQUIDITY
#### Fix bug on android 11 (bug:close after start)
#### Now you can set SLIPPAGE 0.1 
#### ADD Auto SLIPPAGE

<h3 align="center">⭐️ Support Uniswap Matic BSC ⭐️</h3>


 
[![Version](https://img.shields.io/badge/Codename-WHITEHAT-blue.svg?maxAge=259200)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-MAC-red.svg)]()
[![Available](https://img.shields.io/badge/Available-WIN-yellow.svg?maxAge=259200)]()
[![Documentation](https://img.shields.io/badge/BSC-SNIPER-red.svg?maxAge=259200)]()
[![Contributions Welcome](https://img.shields.io/badge/Type-FREE-green.svg?style=flat)]()
 
 
#### BSC SNIPER protocol is developed based on awesome open source research by Zcash team with the help of amazing Ethereum community
#### Web3 Pancakeswap Sniper & honeypot detector Take Profit/StopLose bot written in python3, For ANDROID WIN MAC & LINUX
#### Sniper bot that watches when taxes/anti buy are removed from a contract, then quick snipes, with honeypot detector, and also keybinding for fair launches




### Install
First of all, you need install Python3+
Run on Android you need Install [Termux](https://termux.com/)  
```shell
termux: $ pkg install python git
Debian/Ubuntu: $ sudo apt install python3 git make gcc
Windows: Need to install Visual Studio BuildTools & Python3
```
Install Requirements:  
```python3
python -m pip install -r requirements.txt
```  

### START BSC SNIPER BOT : 

```python3
python3 Sniper.py -t <TOKEN_ADDRESS> -a <AMOUNT> -tx <TXAMOUNT> -hp -wb <BLOCKS WAIT BEFORE BUY> -tp <TAKE PROFIT IN PERCENT> -sl <STOP LOSE IN PERCENT>
python3 bsc-sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 -a 0.001 -tx 2 -hp  -wb 10 -tp 50
python3 bsc-sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 --sellonly
python3 bsc-sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 -a 0.001 --buyonly
python3 bsc-sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 -tsl 10 -nb
```  


<H2>HOW TO USE</H2>

#### Setup your wallet Address and private key in Settings.json
1. An ethereum/bsc address.
2. Open "Settings.json" (with notepad) on line 2 and 3 add wallet address and phrase or private key.
3. Run python3 sniper.py
 
(Also you can use phrase key just use space between words)

<H2>How Find Private Key</H2>
https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key



## BSC SNIPER options with infos:  

```python3
'-t' or '--token', Token for snipe e.g. "-t 0x34faa80fec0233e045ed4737cc152a71e490e2e3"
'-a' or '--amount', float, Amount in Bnb to snipe e.g. "-a 0.1"

'-tx' or '--txamount', how mutch tx you want to send? It split your BNB amount in e.g. "-tx 5"

'-wb' or '--awaitBlocks', default=0, Await Blocks before sending BUY Transaction. e.g. "-ab 50" 

'-hp' or '--honeypot', if you use this Flag, your token get checks if token is honypot before buy!

'-nb' or '--nobuy', No Buy, Skipp buy, if you want to use only TakeProfit/StopLoss/TrailingStopLoss
'-tp' or '--takeprofit', Percentage TakeProfit from your input BNB amount. e.g. "-tp 50" 
'-tsl'or '--trailingstoploss', 'Percentage Trailing-Stop-loss from your first Quote "-tsl 50"

'-so' or '--sellonly', Sell ALL your Tokens from given token address
'-bo' or '--buyonly', Buy Tokens with your given amount

* = require every time its runs!
```

<H3>WHAT IS UNIQUE TOKEN TRADERS</h3>

- fully decentralized protocol for private transactions
- AUTO BUY TOKEN ON LAUNCH AFTER ADD LIQUIDITY
- Support ANDROID ,Windows 10 ,Linux and Mac OS
- Add uniswap V3 & pancakeswap v2 
- Added multiple DEXs
- Force Buy and Force Sell buttons, when clicked it will buy or sell with your chosen settings (excluding limit price)
- set manual SLIPPAGE 
- set stop-less price
- Speed adjustable
- The program determines the name and decimals of the token automatically


## Trailing-Stop-Loss:
<img src="http://www.financial-spread-betting.com/community/wp-content/uploads/2011/11/trailing-stop-buy.jpg" height="400">
