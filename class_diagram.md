
# Python Banking System - Class Diagram

## Architecture

```mermaid
classDiagram

    class BankAccount {
        <<abstract>>
        +account_holder
        -_account_number
        -_balance
        -_transactions
        +deposit(amount)
        +withdraw(amount)
        +show_details()
        +transaction_history()
    }

    class SavingsAccount {
        +withdraw(amount)
    }

    class CurrentAccount {
        +withdraw(amount)
    }

    class BankingSystem {
        +accounts
        +next_account_number
        +create_account()
        +find_account()
        +deposit_money()
        +withdraw_money()
        +check_balance()
        +show_history()
        +run()
    }

    BankAccount <|-- SavingsAccount
    BankAccount <|-- CurrentAccount
    BankingSystem o-- BankAccount
```

## Class Descriptions

### BankAccount
The base abstract class that stores common account information and provides deposit, balance and transaction history methods.

### SavingsAccount
Inherits from BankAccount and implements withdrawal functionality.

### CurrentAccount
Inherits from BankAccount and implements withdrawal functionality.

### BankingSystem
Manages account creation, deposits, withdrawals, account details and transaction history.

## OOP Relationships

- Inheritance: SavingsAccount and CurrentAccount inherit from BankAccount.
- Encapsulation: Account information is controlled through class attributes and methods.
- Abstraction: BankAccount defines a common abstract withdrawal method.
- Polymorphism: Different account classes implement their own withdrawal methods.
