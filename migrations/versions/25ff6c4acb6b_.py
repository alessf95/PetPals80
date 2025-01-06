"""empty message

Revision ID: 25ff6c4acb6b
Revises: 3c3606b6499f
Create Date: 2024-12-26 22:24:04.808591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25ff6c4acb6b'
down_revision = '3c3606b6499f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=25), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.drop_column('created_at')
        batch_op.drop_column('username')

    # ### end Alembic commands ###