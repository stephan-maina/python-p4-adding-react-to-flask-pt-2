#!/usr/bin/env python3

from app import db
from models import Movie

if __name__ == '__main__':
    db.create_all()

    # Create and add sample movie entries
    movies_data = [
        {'title': 'Equiliser 3', 'release_year': 2021, 'genre': 'Action'},
        {'title': 'Expandaples 4', 'release_year': 2022, 'genre': 'Comedy'},
        {'title': 'Anabelle 4', 'release_year': 2025, 'genre': 'Horror'}
        
        ]
    


    for movie_data in movies_data:
        movie = Movie(**movie_data)
        db.session.add(movie)

    db.session.commit()

    print("Sample movie entries added to the database.")
