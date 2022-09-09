from brownie import accounts, FundMe
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() * 10000000000
    print(entrance_fee)
    print("Attempting to fund")
    fund_me.fund({"from": account, "value": entrance_fee})
    print("funded!")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
