"""Modelo que representa una temporada de una serie."""

from __future__ import annotations
from src.extensions import db


class Season(db.Model):
    """Temporada asociada a una serie."""

    __tablename__ = "seasons"

    # Columnas principales
    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey("series.id"), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    episodes_count = db.Column(db.Integer, nullable=False)

    # Restricción única: una temporada por número dentro de una misma serie
    __table_args__ = (
        db.UniqueConstraint("series_id", "number", name="unique_series_season"),
    )

    # Relación con Series (bidireccional)
    series = db.relationship("Series", back_populates="seasons")

    def __repr__(self) -> str:
        """Representación legible del modelo."""
        return f"<Season id={self.id} series_id={self.series_id} number={self.number}>"

    def to_dict(self) -> dict:
        """Serializa la temporada en un diccionario."""
        return {
            "id": self.id,
            "series_id": self.series_id,
            "number": self.number,
            "episodes_count": self.episodes_count,
        }
