from app.client import get_account_info


account = get_account_info()

print("\n===== Account Summary =====")
print(f"Can Trade         : {account['canTrade']}")
print(f"Fee Tier          : {account['feeTier']}")
print(f"Available Balance : {account['availableBalance']}")
print(f"Total Wallet      : {account['totalWalletBalance']}")