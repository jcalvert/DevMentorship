import json
import pytest

from vendingSimple import VendingMachine



@pytest.fixture
def createVM():
	return VendingMachine()

def test_initialization(createVM):
	assert createVM.coins == 0
	assert createVM.inventory == {'item1': 5, 'item2': 5, 'item3': 5}

def test_insert_coin(createVM):
	assert createVM.coins == 0
	createVM.insert_coin()
	assert createVM.coins == 1
	createVM.insert_coin()
	createVM.insert_coin()
	assert createVM.coins == 3

def test_return_coins(createVM):
	createVM.insert_coin()
	createVM.insert_coin()
	createVM.insert_coin()
	assert createVM.coins == 3
	createVM.return_coins()
	assert createVM.coins == 0

def test_return_correct_number_of_coins(createVM):
    createVM.coins =3
    assert createVM.return_coins() == 3
# when I have 3 coins in the machine and vend a cola, I should get back 1 coin.
# vending = new vending machine
# 3x vending insertcoin
# vending vend "cola"
# assert 1 coin

def test_vend(createVM):
	createVM.coins = 4
	createVM.inventory = {'item1': 0, 'item2': 5, 'item3': 5}

	createVM.vend('item1')
	assert createVM.coins == 4
	assert createVM.inventory == {'item1': 0, 'item2': 5, 'item3': 5}

	createVM.vend('nonExsistingItem')
	assert createVM.coins == 4
	assert createVM.inventory == {'item1': 0, 'item2': 5, 'item3': 5}

	createVM.vend('item2')
	assert createVM.coins == 0
	assert createVM.inventory == {'item1': 0, 'item2': 4, 'item3': 5}

	createVM.coins = 2
	createVM.vend('item2')
	assert createVM.coins == 0
	assert createVM.inventory == {'item1': 0, 'item2': 3, 'item3': 5}
#### added by jc
def test_negative_inventory(createVM):
    createVM.inventory = {'coke': 0, 'sprite': 1, 'lacroix': 3}
    createVM.insert_coin()
    createVM.insert_coin()
    createVM.vend('coke')
    assert createVM.inventory == {'coke': 0, 'sprite': 1, 'lacroix': 3}

def test_coin_return(createVM):
    createVM.insert_coin()
    assert createVM.return_coins() == 1

def test_return_coins_on_vend(createVM):
    createVM.insert_coin()
    createVM.insert_coin()
    createVM.insert_coin()
    assert json.load(createVM.vend("item1")) == {"vended": "item1", "returned_coins": 1}

def test_invalid_beverage(createVM):
    createVM.insert_coin()
    createVM.insert_coin()
    assert json.load(createVM.vend("cola")) == {'error': 'Invalid item!'}

