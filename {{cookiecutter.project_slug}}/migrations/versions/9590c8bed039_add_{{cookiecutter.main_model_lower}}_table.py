"""Create the {{cookiecutter.main_model}} table

Revision ID: 9590c8bed039
Revises: e608b0a91508
Create Date: 2021-10-12 00:29:24.432332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9590c8bed039"
down_revision = "e608b0a91508"
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "{{cookiecutter.main_model_lower}}",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("description", sa.UnicodeText(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"], ["users.id"], onupdate="CASCADE", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_{{cookiecutter.main_model_lower}}_author_id"), "{{cookiecutter.main_model_lower}}", ["author_id"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_{{cookiecutter.main_model_lower}}_author_id"), table_name="{{cookiecutter.main_model_lower}}")
    op.drop_table("{{cookiecutter.main_model_lower}}")
