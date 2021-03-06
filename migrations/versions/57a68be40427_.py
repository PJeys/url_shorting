"""empty message

Revision ID: 57a68be40427
Revises: 269c17ff5c79
Create Date: 2022-03-15 20:57:13.978783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57a68be40427'
down_revision = '269c17ff5c79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('urls', sa.Column('domain', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('urls', 'domain')
    # ### end Alembic commands ###
