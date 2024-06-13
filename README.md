# Account Balancing Code Task (1hr time limit)

## Contents

1. [Task Description](#task-description)
2. [My Solution](#my-solution)
3. [Future Improvements](#future-improvements)

## Task Description

- We have a number of different bank accounts that we use to fund transfers.
- From time-to-time, we need to "rebalance" these accounts.
- Rebalancing involves transferring funds from one or more accounts to another account.

### Current State

```json
[
  {
    "account_id": 1,
    "balance": 1000000
  },
  {
    "account_id": 2,
    "balance": 2000000
  },
  {
    "account_id": 3,
    "balance": 1000000
  },
  {
    "account_id": 4,
    "balance": 2000000
  }
]
```

### Target State

```json
[
  {
    "account_id": 1,
    "balance": 800000
  },
  {
    "account_id": 2,
    "balance": 2500000
  },
  {
    "account_id": 3,
    "balance": 1200000
  },
  {
    "account_id": 4,
    "balance": 1500000
  }
]
```

### Goal

- Write a function that takes an input (current_state, target_state) and returns money_movements.
- The primary objective of the task is to write a working and correct solution.
- Any optimisations are nice to have and can be added later.

#### Money Movements

```json
[
  {
    "from_account": 1,
    "to_account": 2,
    "amount": 200000
  }
]
```

### Limitations

- The algorithm must not send money to and from the same account.
- The algorithm must not output more than 1 money movement from and to the same pair of accounts.

## My Solution

```bash
$ python main.py 
[{'amount': 200000, 'from_account': 1, 'to_account': 2},
 {'amount': 300000, 'from_account': 4, 'to_account': 2},
 {'amount': 200000, 'from_account': 4, 'to_account': 3}]
```

## Future Improvements

- Prevent the for loop within the for loop