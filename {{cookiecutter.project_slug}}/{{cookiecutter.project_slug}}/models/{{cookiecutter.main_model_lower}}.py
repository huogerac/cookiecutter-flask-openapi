from datetime import datetime, timezone

import sqlalchemy as sa

from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.users import User


class {{cookiecutter.main_model}}(db.Model):

    __tablename__ = "{{cookiecutter.main_model_lower}}"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(128), nullable=False)
    description = sa.Column(sa.UnicodeText(), nullable=True)
    created_at = sa.Column(
        sa.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    author_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("users.id", onupdate="CASCADE", ondelete="SET NULL"),
        index=True,
    )

    author = db.relationship(User, backref=db.backref("{{cookiecutter.main_model_lower}}", lazy="dynamic"))

    def __repr__(self):
        return self.title

    def to_dict(self):
        """Convert model to dict"""
        author = self.author.to_dict() if self.author else self.author

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "author": author,
        }
