
from felicity_site import db

class Piece(db.Model):
    __tablename__ = 'pieces'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(32), nullable=False)
    medium = db.Column(db.String(32), nullable=False)
    dimensions = db.Column(db.String(16), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    descr = content = db.Column(db.Text, nullable=True)
    external = db.Column(db.String(32), nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    thumbnail_file = db.Column(db.String(120), nullable=False, default='default.jpg')