import pprint

dict_inventory = {'rope' : 1, 'torch' : 6,'gold coin' : 42,'dagger':1,'arrow':12}

def _printInventory(inventory):
    pprint.pprint("Inventory:")
    total_items = 0
    for k,v in inventory.items():
        pprint.pprint(str(inventory.get(k,0)) +' '+ k )
        total_items = total_items + inventory.get(k,0)
    pprint.pprint('Total Items are : ' + str(total_items) )

_printInventory(dict_inventory)