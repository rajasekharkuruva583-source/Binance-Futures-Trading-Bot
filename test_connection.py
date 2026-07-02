
# # from app.client import get_server_time
# from app.logger import logger


# # def main():
# #     print("Connecting to Binance Futures Testnet...")

# #     logger.info("Application Started")

# #     response = get_server_time()

# #     print(f"Server Time : {response['serverTime']}")

# #     logger.info("Application Finished")


# # if __name__ == "__main__":
# #     main()

# #-----
# # from app.client import get_account_info


# # def main():

# #     print("Connecting to Binance...")

# #     account = get_account_info()

# #     print(account)


# # if __name__ == "__main__":
# #     main()

# #---
# from app.client import get_account_info


# def main():
#     print("Connecting to Binance Futures Testnet...\n")

#     account = get_account_info()

#     print("===== Account Summary =====")
#     print(f"Can Trade        : {account['canTrade']}")
#     print(f"Fee Tier         : {account['feeTier']}")
#     print(f"Available Balance: {account['availableBalance']}")
#     print(f"Total Wallet     : {account['totalWalletBalance']}")


# if __name__ == "__main__":
#     main()