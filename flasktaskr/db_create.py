from project import db


#creates the database and db tables
db.create_all()




#commit the changes
db.session.commit()