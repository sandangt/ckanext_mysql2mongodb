"""Create validator logs database

Revision ID: a159239bcc31
Revises: 
Create Date: 2022-04-16 01:21:06.101082

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a159239bcc31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('validator_logs',
    sa.Column('log_id', sa.VARCHAR(length=100), nullable=False),
    sa.Column('resource_id', sa.VARCHAR(length=100), nullable=False),
    sa.Column('package_id', sa.VARCHAR(length=100), nullable=False),
    sa.Column('database', sa.VARCHAR(length=250), nullable=False),
    sa.Column('table', sa.VARCHAR(length=250), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('created_time', postgresql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('log_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('validator_logs')
    # ### end Alembic commands ###
