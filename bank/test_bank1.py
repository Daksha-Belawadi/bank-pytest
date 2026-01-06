from bank import bank_details

def test_bank_details():
    expected_output = (
        "Account Number : 12345\n"
        "Account Holder Name : Anil\n"
        "Account Type : Savings\n"
        "Balance : 10000"
    )
    assert bank_details(12345, "Anil", "Savings", 10000) == expected_output
