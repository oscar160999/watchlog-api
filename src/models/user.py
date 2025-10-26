__tablename__ = "users"

# TODO: definir columnas (id, name, email opcional, created_at).
# TODO: agregar relacion con WatchEntry (one-to-many).

def __repr__(self) -> str:
    """Devuelve una representacion legible del usuario."""
    return f"<User id={getattr(self, 'id', None)} name={getattr(self, 'name', None)}>"

def to_dict(self) -> dict:
    """Serializa al usuario para respuestas JSON."""
    # TODO: reemplazar esta implementacion por serializacion real.
    return {
        "id": getattr(self, "id", None),
        "name": getattr(self, "name", None),
        "email": getattr(self, "email", None),
        "created_at": getattr(self, "created_at", datetime.utcnow()),
    }
