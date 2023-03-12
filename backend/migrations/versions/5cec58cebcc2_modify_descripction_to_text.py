"""modify descripction to Text

Revision ID: 5cec58cebcc2
Revises: 
Create Date: 2023-03-08 15:33:15.383361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cec58cebcc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('event', 'description', type_=sa.Text())

def downgrade():
    op.alter_column('event', 'description', type_=sa.String(length=100))

    # ### end Alembic commands ###
