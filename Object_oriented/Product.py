import uuid
class Product:
    
    def __init__(self,name,price,categories,comment=[]):
        self.name=name
        self.price=price
        self.categories=categories
        self.id=self.id_generator()
        self.comment=comment
    @staticmethod
    def id_generator():
        return uuid.uuid1()
        
    def addComment(self,comments:list):
        return self.comment.append(comments)

class User:
    username_list=[]
    def __init__(self,username):
        self.purchase_hist_id=[]
        self.purchase_hist={}
        if username not in User.username_list:
            self.username=username
            User.username_list.append(username)
        else:
            raise ValueError('username has already taken')
    def purchase(self,stuffs:dict):
        total=0
        for stuff in stuffs.keys():
            self.purchase_hist_id.append(stuff.id)
            self.purchase_hist[stuff]=stuffs[stuff]
            total=total+stuff.price*stuffs[stuff]
        self.purchase_hist['total']=total
            
        # return self.purchase_hist
    def purchaseHistory_id(self):
        return self.purchase_hist_id
    def purchaseHistory(self):
        return self.purchase_hist

class Comment():
    users_comments={}
    
    users_rating={}
    # def __init__(self,user,rating=0,text=''):
    #     self.username=user.username
    #     self.rating=rating
    #     self.comment=text
    # def get_comment(self):
    #     Comment.users_comments[self.username]=self.comment
    #     return Comment.users_comments[self.username]
    def add_comment(user,product,rating=0,text=''):
        Comment.users_comments[(user.username,product.name)]=text
        # Comment.users_rating[user.username]=rating
        Comment.users_rating[(user.username,product.name)]=rating
        # return (Comment.users_comments[user.username],Comment.users_rating[user.username])
    def get_comment_of_users(user,product):
        return Comment.users_comments[(user.username,product.name)]
        
    def get_rating_of_users(user,product):
        return (Comment.users_rating[(user.username,product.name)])
        
        