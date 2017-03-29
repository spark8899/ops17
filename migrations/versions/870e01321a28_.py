"""empty message

Revision ID: 870e01321a28
Revises: 
Create Date: 2017-03-29 09:18:20.294000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '870e01321a28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('software',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('version', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_software_name'), 'software', ['name'], unique=True)
    op.create_index(op.f('ix_software_version'), 'software', ['version'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('mobile', sa.INTEGER(), nullable=True),
    sa.Column('department', sa.String(length=32), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('allow_login', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_allow_login'), 'users', ['allow_login'], unique=False)
    op.create_index(op.f('ix_users_department'), 'users', ['department'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_mobile'), 'users', ['mobile'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('department', sa.String(length=32), nullable=True),
    sa.Column('pm_id', sa.Integer(), nullable=True),
    sa.Column('sla', sa.String(length=32), nullable=True),
    sa.Column('check_point', sa.String(length=64), nullable=True),
    sa.Column('domain', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['pm_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_projects_department'), 'projects', ['department'], unique=False)
    op.create_table('modules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('department', sa.String(length=32), nullable=True),
    sa.Column('svn', sa.String(length=128), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('dev_id', sa.Integer(), nullable=True),
    sa.Column('qa_id', sa.Integer(), nullable=True),
    sa.Column('ops_id', sa.Integer(), nullable=True),
    sa.Column('software_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['dev_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['ops_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['modules.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['qa_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_modules_department'), 'modules', ['department'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_modules_department'), table_name='modules')
    op.drop_table('modules')
    op.drop_index(op.f('ix_projects_department'), table_name='projects')
    op.drop_table('projects')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_mobile'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_department'), table_name='users')
    op.drop_index(op.f('ix_users_allow_login'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_software_version'), table_name='software')
    op.drop_index(op.f('ix_software_name'), table_name='software')
    op.drop_table('software')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    # ### end Alembic commands ###
