from app import db

class Node(db.Model):
	ID = db.Column(db.BigInteger, primary_key=True)
	latitude = db.Column(db.Float, index=True)
	longitude = db.Column(db.Float, index=True)
	nameTag = db.Column(db.String(500), index=True)
	language = db.Column(db.String(120), index=True)
	translation = db.Column(db.String(1000), index=True)
	translationCount = db.Column(db.Integer)
	transliteration = db.Column(db.String(1000), index=True)
	transliterationCount = db.Column(db.Integer)


	def __repr__(self):
		return '<Place %r>' % (self.nameTag)
