from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal
from typing import List
import pytest

def create_sms_message(text: str, author: str, sent_at: datetime.datetime) -> SmsMessage:
    return SmsMessage(text=text, author=author, sent_at=sent_at)

def create_bank_card(last_digits: str, owner: str) -> BankCard:
    return BankCard(last_digits=last_digits, owner=owner)

def test_parse_ineco_expense_sunny_case_single_card():
    # arrange
    cards: List[BankCard] = [
        create_bank_card('1234', 'Owner1'),
    ]
    sms = create_sms_message('1500.99 руб, 888888881234 16.09.24 12:30 cafe authcode 888', 'Bank', datetime.datetime.now())

    # act
    expense = parse_ineco_expense(sms, cards)
    
    # assert
    assert expense.amount == decimal.Decimal('1500.99')
    assert expense.card.last_digits == '1234'
    assert expense.spent_in == 'cafe'
    assert expense.spent_at == datetime.datetime.strptime('16.09.24 12:30', '%d.%m.%y %H:%M')

def test_parse_ineco_expense_sunny_case_multiple_cards():
    # arrange
    cards: List[BankCard] = [
        create_bank_card('1234', 'Owner1'),
        create_bank_card('5678', 'Owner2'),
    ]
    sms = create_sms_message('1500.99 руб, 888888885678 16.09.24 12:30 shop authcode 888', 'Bank', datetime.datetime.now())

    # act
    expense = parse_ineco_expense(sms, cards)
    
    # assert
    assert expense.amount == decimal.Decimal('1500.99')
    assert expense.card.last_digits == '5678'
    assert expense.spent_in == 'shop'
    assert expense.spent_at == datetime.datetime.strptime('16.09.24 12:30', '%d.%m.%y %H:%M')

def test_parse_ineco_expense_no_matching_card():
    # arrange
    cards: List[BankCard] = [
        create_bank_card('1234', 'Owner1'),
        create_bank_card('5678', 'Owner2'),
    ]
    sms = create_sms_message('1500.99 руб, 888888889999 16.09.24 12:30 shop authcode 888', 'Bank', datetime.datetime.now())
  
    # act & assert
    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards)

def test_parse_ineco_expense_empty_cards():
    # arrange
    cards: List[BankCard] = []
    sms = create_sms_message('1500.99 руб, 888888889999 16.09.24 12:30 shop authcode 888', 'Bank', datetime.datetime.now())
  
    # act & assert
    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards)

def test_parse_ineco_expense_no_authcode():
    # arrange
    cards: List[BankCard] = [
        create_bank_card('1234', 'Owner1'),
        create_bank_card('5678', 'Owner2'),
    ]
    sms = create_sms_message('100 руб, 888888885678 16.09.24 12:30 shop', 'Bank', datetime.datetime.now())

    # act
    expense = parse_ineco_expense(sms, cards)
    
    # assert
    assert expense.amount == decimal.Decimal('100')
    assert expense.card.last_digits == '5678'
    assert expense.spent_in == 'shop'
    assert expense.spent_at == datetime.datetime.strptime('16.09.24 12:30', '%d.%m.%y %H:%M')    