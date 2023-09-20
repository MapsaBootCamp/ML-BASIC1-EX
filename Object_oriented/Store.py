
import Product
from functools import reduce
productlds={}
def addProduct(product_name,count=0):
    
    # name=product_name.name
    global productlds
    if product_name.name in productlds:
        old_count=productlds.get(product_name.name)
        new_count=old_count+count
        productlds[product_name.name]=new_count
    else:
        productlds[product_name.name]=count
    return productlds

def removeProduct(product_name,count=0):
    global productlds
    if product_name.name in productlds:
        old_count=productlds.get(product_name.name)
        if old_count<count:
            raise ValueError('the count you entered is less than provided')
        else:
            new_count=old_count-count
            productlds[product_name.name]=new_count
    else:
        raise ValueError('this item is not in the products')
    return productlds

def addUser(username_input):
    globals()[username_input] = Product.User(username=username_input)

def getTotalInventoryCount():
    # [sum(x) for x in productlds.values()]
    lis=[x for x in productlds.values()]
    all_of_things=reduce(lambda a,b:a+b , lis)
    list_of_products=(f'The number of Products Variety: {len(productlds.keys())}',f'all of the Products Counts:{all_of_things}' )
    return list_of_products

def add_comment_rating(user,product,comment='',rating=10):
    Product.Comment.add_comment(user,product=product,text=comment,rating=rating)
    
def getCommentsOfUser(user,product):
    comment_of_user=Product.Comment.get_comment_of_users(user,product)
    return comment_of_user

def purchase(user,stuffs:dict):
    Product.User.purchase(globals()[user],stuffs)
  
def getRating(product):
    product_rating=0
    i=0
    for (user,p) in Product.Comment.users_comments.keys():
        if p==product.name:
            product_rating=product_rating+Product.Comment.get_rating_of_users(globals()[user],product=product)
            i+=1
    return (product_rating/i)

  
def getTotalProfit():
    total_profit=0
    for user in Product.User.username_list:
        if Product.User.purchaseHistory(globals()[user]):
            total_profit = total_profit + Product.User.purchaseHistory(globals()[user])['total']
    return total_profit
            
        
    