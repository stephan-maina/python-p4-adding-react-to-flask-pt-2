from app import db

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.Integer)
    genre = db.Column(db.String(255))

    def __repr__(self):
        return f'<Movie: {self.title}>'
