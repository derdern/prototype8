from sqlalchemy.sql.sqltypes import Date
from app import db
class AddUserData(db.Model):#create table from db object from app.py
    __tablename__ = "tbl_add_user_data"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    age = db.Column(db.String)

    def __repr__(self):
        return "<artist: {}="">".format(self.name)
        
""" class Album(db.Model):
    """"""
    __tablename__ = "albums"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artist", backref=db.backref(
        "albums", order_by=id), lazy=True)
</artist:> """