"""Modelo para series disponibles en el catálogo."""

from __future__ import annotations
from datetime import datetime
from src.extensions import db


class Series(db.Model):
    """Representa una serie cargada por los usuarios."""

    __tablename__ = "series"

    # Columnas principales
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    total_seasons = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Columnas opcionales
    synopsis = db.Column(db.Text, nullable=True)
    genres = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)

    # Relaciones
    seasons = db.relationship("Season", back_populates="series", cascade="all, delete-orphan", lazy="joined")
    watch_entries = db.relationship("WatchEntry", backref="series", lazy=True)

    def __repr__(self) -> str:
        """Devuelve una representación legible del modelo."""
        return f"<Series id={self.id} title='{self.title}'>"

    def to_dict(self, include_seasons: bool = False) -> dict:
        """Serializa la serie y opcionalmente sus temporadas."""
        data = {
            "id": self.id,
            "title": self.title,
            "total_seasons": self.total_seasons,
            "synopsis": self.synopsis,
            "genres": self.genres,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        if include_seasons:
            data["seasons"] = [season.to_dict() for season in self.seasons]
        return data
