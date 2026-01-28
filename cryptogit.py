from encodings.punycode import T
from locale import currency
from pydoc import text
import random
import time

wallet = {
    "USD": 1000,
    "BTC": 0.0,
    "ETH": 0.0
    }
coins = ["btc", "eth"]

def get_prices():
   return{
       "BTC": round(random.randint(20000, 30000), 1),
       "ETH": round(random.randint(2000, 3000), 1)
       }

def log_transaction(text):
    with open("history.txt", "a") as file:
        file.write(f"{time.ctime()} : {text} \n")
    print("Transaction saved into the history.")
    return text

def show_history():
    try:
        print("==============================")
        with open("history.txt", "r") as file:
            print(file.read())
        print("==============================")
    except FileNotFoundError:
        return "File Not Found."

def clean_history():
    with open("history.txt", "w") as file:
        pass
    print("History were cleared.")

while True:
    current_price = get_prices()
    print("==============================")
    print("Your Balance: ")
    for wcoins, amount in wallet.items():
        print(f"{wcoins} : {(amount):.6f}")
    print("==============================")
    print("Current Price:")
    for coin, price in current_price.items():
        print(f"{coin} : ${price} USD")
    print("==============================")
    input("Press any button to continue. . .")



    print("==============================")
    print("1. Buy")
    print("2. Sell")
    print("3. Show History")
    print("4. Clear History")
    print("5. Exit")
    print("==============================")
    select = input("Enter your choice: ")

    if select == "1":
        prices = current_price
        btc_price = prices["BTC"]
        eth_price = prices["ETH"]
        while True:
            crypto = input("Enter which crypto you would like to buy: ").strip()
            if crypto.lower() in coins:
                usd_amount = float(input(f"How much USD do you want to spend on {crypto}: "))
                if usd_amount < 0:
                    print("Access for the purchase DENIED.")
                    log_transaction("Access for the purchase DENIED.")
                    input("Press any button to continue. . . .")
                    break
                if usd_amount > wallet["USD"]:
                    print("Not enough money on your wallet")
                    log_transaction("Access for the purchase DENIED.")
                    input("Press any button to continue. . . .")
                    break
                else:
                    if crypto.lower() == "btc":
                        btc_amount = usd_amount / btc_price
                        wallet["USD"] -= usd_amount
                        wallet["BTC"] += btc_amount
                        print("Your purchase was Successfull:")
                        text = f"Bought: {btc_amount} {crypto} for ${usd_amount}"
                        print(f"Bought: {btc_amount} {crypto} for ${usd_amount}")
                        log_transaction(text)
                        input("Press any button to continue. . . .")
                        break
                    elif crypto.lower() == "eth":
                        eth_amount = usd_amount / eth_price
                        wallet["ETH"] += eth_amount
                        wallet["USD"] -= usd_amount
                        print("Your purchase was Successfull:")
                        text = f"Bought: ({eth_amount}) {crypto} for ${usd_amount}"
                        print(f"Bought: ({eth_amount}) {crypto} for ${usd_amount}")
                        log_transaction(text)
                        input("Press any button to continue. . . .")
                        break
                    else:
                        print("Error! There is no crypto that you are looking for. . . .")
                        log_transaction("Access for the purchase DENIED.")
                        input("Press any button to continue. . . .")
                        continue
            else:
                print("Error! There is no crypto that you are looking for. . . .")
                log_transaction("Access for the purchase DENIED.")
                input("Press any button to continue. . . .")
                continue
    elif select == "2":
        prices = current_price
        btc_price = prices["BTC"]
        eth_price = prices["ETH"]
        while True:
            crypto = input("Enter which crypto you want to sell: ").strip()
            if crypto.lower() in coins:
                if crypto.lower() == "btc":
                    ask = input("Sell every BTC on your wallet (Yes/No): ").strip()
                    while True:
                        if ask.lower() == "no":
                            btcsell = float(input("Enter how much BTC you want to sell*:  "))
                            if btcsell > wallet["BTC"]:
                                print(f"Not enough BTC on your wallet.")
                                log_transaction("Not enough BTC on the wallet. Purschase was not successful.")
                                input("Press any button to continue. . . . ")
                                break                    
                            else:
                                usd_amount = btcsell * btc_price
                                wallet["BTC"] -= btcsell
                                wallet["USD"] += usd_amount
                                print(f"Your purchase was Successfull:")
                                print(f"Sell {btcsell} BTC for {usd_amount}")
                                text = f"Sell {btcsell} BTC for {usd_amount}"
                                log_transaction(text)
                                break
                        elif ask.lower() == "yes":
                            if wallet["BTC"] == 0.0:
                                print("Not enough BTC on your wallet.")
                                input("Press any button to continue. . . . .")
                                break
                            else:
                                btc_amount = wallet["BTC"]
                                usd_amount = btc_price * btc_amount
                                wallet["BTC"] -= btc_amount
                                wallet["USD"] += usd_amount
                                print(f"Your purchase was Successfull:")
                                print(f"Sell {btc_amount} BTC for {usd_amount}")
                                text = f"Sell {btc_amount} BTC for {usd_amount}"
                                log_transaction(text)
                                break
                    break
                elif crypto.lower() == "eth":
                    ask = input("Sell every ETH on your walet (Yes/No): ").strip()
                    while True:
                        if ask.lower() == "no":
                            ethsell = float(input("Enter much ETH you want to sell*: "))
                            if ethsell > wallet["ETH"]:
                                print("Not enough ETH on your balance.")
                                text = f"Unsuccessful attempt to sell {ethsell} ETH !"
                                log_transaction(text)
                                input("Press any button to continue. . . .")
                                break
                            else:
                                usd_amount = ethsell * eth_price
                                wallet["ETH"] -= ethsell
                                wallet["USD"] += usd_amount
                                print(f"Your purchase was Successfull:")
                                print(f"Sell {ethsell} ETH for ${usd_amount}")
                                text = f"Sell {ethsell} ETH for ${usd_amount}"
                                log_transaction(text)
                                break
                        elif ask.lower() == "yes":
                            if wallet["ETH"] == 0.0:
                                print("Not enough ETH on your wallet.")
                                input("Press any button to continue. . . . .")
                                break
                            else:
                                eth_amount = wallet["ETH"]
                                usd_amount = eth_price * eth_amount
                                wallet["ETH"] -= eth_amount
                                wallet["USD"] += usd_amount
                                print(f"Your purchase was Successfull:")
                                print(f"All your ETH were sold for ${usd_amount}")
                                text = f"All your ETH were sold for ${usd_amount}"
                                log_transaction(text)
                                break
                    break
                else:
                    print("There is no {crypto} that you are looking for.")
                    continue
    elif select == "3":
        show_history()
        input("Press any button to continue. . . .")
    elif select == "4":
        clean_history()
        input("Press any button to continue. . . .")
    elif select == "5":
        print("Logging out. . . . ")
        time.sleep(0.5)
        exit()
    else:
        continue