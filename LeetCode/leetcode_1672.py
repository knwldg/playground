def max_wealth(accounts: [[int]]) -> int:
    max_result = 0

    for customer in accounts:
        combined_value = 0
        for account in customer:
            combined_value += account
            if combined_value > max_result:
                max_result = combined_value

    return max_result
