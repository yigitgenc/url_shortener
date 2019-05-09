"""Application models module."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Url(db.Model):
    """
    Url model.
    """
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False, unique=True)
    code = db.Column(db.String(8), nullable=False, unique=True, index=True)
    visits = db.relationship("Visit", back_populates="url")
    created = db.Column(db.DateTime, server_default=db.func.now())


class Visit(db.Model):
    """
    Visit model.
    """
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey(Url.id), nullable=False, index=True)
    url = db.relationship("Url", back_populates="visits")
    ip_address = db.Column(db.String(50), nullable=False)
    user_agent = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
