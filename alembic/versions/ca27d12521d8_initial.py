"""Initial

Revision ID: ca27d12521d8
Revises: 
Create Date: 2025-03-04 16:44:07.556779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca27d12521d8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('restaurant',
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('working_hours', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('menu',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('day', sa.Enum('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', name='day_of_week_enum'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('restaurant_id', 'day', name='unique_menu_per_day')
    )
    op.create_table('votes',
    sa.Column('menu_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.CheckConstraint('stars BETWEEN 1 AND 5', name='valid_stars'),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['menu_id'], ['menu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('menu_id', 'employee_id', 'date', name='unique_vote_per_menu_per_day')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_table('menu')
    op.drop_table('restaurant')
    op.drop_table('employee')
    # ### end Alembic commands ###
