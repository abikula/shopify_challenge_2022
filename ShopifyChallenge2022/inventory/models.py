from inventory import db
class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    stock = db.Column(db.Integer(), default=1)
    description = db.Column(db.String(length=1024), default = None)
    isDeleted = db.Column(db.Boolean, default=False, nullable=False)
    delete_comment = db.Column(db.String(length=100))

    def __repr__(self):
        return f'Item {self.name}'