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