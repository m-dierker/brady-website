from website import models
import sys 

newTitle = input('Enter post title: ')
newFile = input('Enter post file name: ')
newCat = input('Enter category (passive, active, rf, ms, power, digital): ')
newContent = open(newFile, 'r').read()

cat = models.Category.query.filter_by(name=newCat).first()
newPost = Post(title=newTitle, body=newContent, cat=cat)

models.db.session.add(newPost)
models.db.session.commit()
