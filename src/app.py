import pandas  as pand
import numpy as np
import sys

# went for multi dimension array dataframe to represent our data in a table form 
# -list of lists would of also worked, MD Array sounds cooler tbh.
def preparecheckOutData() :
    checkoutDummyData = {'ItemSku': ['A','B','C'], 
                         'ItemPrice': [50,30,10], 
                         'SpecialItemQty': [3,2,0],
                         'SpecialItemsCosts': [130,45,0]}
    dataFrame = pand.DataFrame(data=checkoutDummyData)

    #add a calc column to make our lives ezier for function logic
    dataFrame['SpecialItemPrice'] = dataFrame.SpecialItemQty * dataFrame.SpecialItemsCosts
    #i dont want Math errors from 0 values so i am going to NaN the 0s
    dataFrame.replace(0, np.NaN, inplace=True)

    return dataFrame

class Checkout:
   def __init__(self):
     self.checkoutData = preparecheckOutData()     
   def calculateCost(self, qty, itemSku):
    recordByItemSku = self.checkoutData.query(f"ItemSku=='{itemSku}'")
    itemsIncludedInDiscount = qty / recordByItemSku['SpecialItemQty'].values[0]
    itemsAtFullPrice = qty % recordByItemSku['SpecialItemQty'].values[0]
    total = round(itemsIncludedInDiscount) * recordByItemSku['SpecialItemsCosts'].values[0] 
    + (round(itemsAtFullPrice) * recordByItemSku['ItemPrice'].values[0])
    return total
    
checkout = Checkout()

print(checkout.calculateCost(7,'A'))