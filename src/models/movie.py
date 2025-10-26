"""Modelo principal para las películas."""

from __future__ import annotations
from datetime import datetime
from src.extensions import db


class Movie(db.Model):
    """Representa una película dentro del catálogo."""

    __tablename__ = "movies"

    # Columnas principales
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relación con WatchEntry (uno a muchos)
    watch_entries = db.relationship("WatchEntry", backref="movie", lazy=True)

    def __repr__(self) -> str:
        """Devuelve una representación legible del modelo."""
        return f"<Movie id={self.id} title='{self.title}' genre='{self.genre}' release_year={self.release_year}>"

    def to_dict(self) -> dict:
        """Serializa la instancia para respuestas JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "release_year": self.release_year,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
