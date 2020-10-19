from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""define Pet model """
class Pet(db.Model):

    """define the basic pet model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.Text,
    nullable=False)

    species = db.Column(db.Text,
    nullable=False)

    photo_url =db.Column(db.Text,
    default="https://i.pinimg.com/originals/0b/1e/7b/0b1e7ba376437f80c2c9df3d033d355f.jpg")

    age = db.Column(db.Integer, default=0)

    notes = db.Column(db.Text,nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)

    def get_self(self):
        """get full details"""
        return f"{self.name},{self.species},{self.age},{self.notes},{self.available}"






