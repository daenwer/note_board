"""create_tables

Revision ID: 7cf07989f9c0
Revises: 
Create Date: 2023-09-26 11:47:12.308269

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7cf07989f9c0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "boards",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "view_count", sa.Integer(), server_default="0", nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "note_boards",
        sa.Column("note_id", sa.Integer(), nullable=True),
        sa.Column("board_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["board_id"],
            ["boards.id"],
        ),
        sa.ForeignKeyConstraint(
            ["note_id"],
            ["notes.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("note_boards")
    op.drop_table("notes")
    op.drop_table("boards")
    # ### end Alembic commands ###
