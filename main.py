from pprint import pprint

current_state = [
    {"account_id": 1, "balance": 1000000},
    {"account_id": 2, "balance": 2000000},
    {"account_id": 3, "balance": 1000000},
    {"account_id": 4, "balance": 2000000}
]

target_state = [
    {"account_id": 1, "balance": 800000},
    {"account_id": 2, "balance": 2500000},
    {"account_id": 3, "balance": 1200000},
    {"account_id": 4, "balance": 1500000}
]


def create_money_movements(current_state: list, target_state: list) -> list:
    # Key current_state by account_id
    current_state_dict = {}
    for account in current_state:
        current_state_dict[account["account_id"]] = account["balance"]

    # Key target_state by account_id
    target_state_dict = {}
    for account in target_state:
        target_state_dict[account["account_id"]] = account["balance"]

    # Determine if account needs to gain or lose money
    accounts_gainers = {}
    accounts_losers = {}
    for account_id in current_state_dict:
        difference = current_state_dict[account_id] - target_state_dict[account_id]

        if difference > 0:
            accounts_losers[account_id] = {"delta": difference}
        else:
            accounts_gainers[account_id] = {"delta": -difference}

    # Create money movements
    money_movements = []
    for gainer in accounts_gainers:
        for loser in accounts_losers:
            result = min(accounts_gainers[gainer]["delta"], accounts_losers[loser]["delta"])

            if result == 0:
                continue

            money_movements.append({
                "from_account": loser,
                "to_account": gainer,
                "amount": result
            })

            accounts_gainers[gainer]["delta"] -= result
            accounts_losers[loser]["delta"] -= result

    return money_movements


if __name__ == "__main__":
    money_movements = create_money_movements(current_state, target_state)
    pprint(money_movements)
