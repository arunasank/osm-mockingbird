from app import db, models
from openpyxl import Workbook


		
u = models.User(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()
