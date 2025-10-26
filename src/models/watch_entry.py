
"""Modelo puente que guarda el progreso del usuario."""

from __future__ import annotations
from datetime import datetime
from src.extensions import db


class WatchEntry(db.Model):
    """Relación entre un usuario y un contenido (película o serie)."""

    __tablename__ = "watch_entries"

    # Columnas básicas
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content_type = db.Column(db.String(10), nullable=False)  # 'movie' o 'series'
    content_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="in_progress")  # 'in_progress', 'completed', etc.

    # Progreso
    current_season = db.Column(db.Integer, nullable=True)
    current_episode = db.Column(db.Integer, nullable=True)
    watched_episodes = db.Column(db.Integer, default=0)
    total_episodes = db.Column(db.Integer, default=1)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones condicionales
    movie = db.relationship("Movie", primaryjoin="and_(WatchEntry.content_id==Movie.id, WatchEntry.content_type=='movie')", backref="watch_entries", viewonly=True)
    series = db.relationship("Series", primaryjoin="and_(WatchEntry.content_id==Series.id, WatchEntry.content_type=='series')", backref="watch_entries", viewonly=True)
    user = db.relationship("User", back_populates="watch_entries")

    def percentage_watched(self) -> float:
        """Calcula el porcentaje completado para el contenido asociado."""
        if self.total_episodes and self.total_episodes > 0:
            return round((self.watched_episodes / self.total_episodes) * 100, 2)
        return 0.0

    def mark_as_watched(self) -> None:
        """Marca el contenido como completado."""
        self.status = "completed"
        self.watched_episodes = self.total_episodes
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> dict:
        """Serializa la entrada para respuestas JSON."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content_type": self.content_type,
            "content_id": self.content_id,
            "status": self.status,
            "current_season": self.current_season,
            "current_episode": self.current_episode,
            "watched_episodes": self.watched_episodes,
            "total_episodes": self.total_episodes,
            "percentage_watched": self.percentage_watched(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
