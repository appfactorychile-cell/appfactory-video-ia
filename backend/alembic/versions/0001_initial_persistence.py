"""create initial persistence tables

Revision ID: 0001_initial_persistence
Revises:
Create Date: 2026-06-28
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial_persistence"
down_revision = None
branch_labels = None
depends_on = None


def _timestamps():
    return [
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(length=40), nullable=False),
    ]


def upgrade() -> None:
    op.create_table("users", *_timestamps(), sa.Column("email", sa.String(length=255), nullable=False), sa.Column("full_name", sa.String(length=180), nullable=False), sa.Column("role", sa.String(length=80), nullable=False), sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("email"))
    op.create_index("ix_users_email", "users", ["email"])
    op.create_table("projects", *_timestamps(), sa.Column("name", sa.String(length=180), nullable=False), sa.Column("description", sa.Text(), nullable=False), sa.Column("primary_language", sa.String(length=80), nullable=False), sa.Column("country", sa.String(length=120), nullable=False), sa.Column("project_type", sa.String(length=80), nullable=False), sa.Column("is_active", sa.Boolean(), nullable=False), sa.PrimaryKeyConstraint("id"))
    op.create_index("ix_projects_name", "projects", ["name"])
    op.create_table("channels", *_timestamps(), sa.Column("name", sa.String(length=180), nullable=False), sa.Column("target_country", sa.String(length=120), nullable=False), sa.Column("language", sa.String(length=80), nullable=False), sa.Column("timezone", sa.String(length=120), nullable=False), sa.Column("niche", sa.String(length=120), nullable=False), sa.Column("visual_style", sa.String(length=180), nullable=False), sa.Column("ai_voice", sa.String(length=180), nullable=False), sa.Column("daily_video_count", sa.Integer(), nullable=False), sa.Column("publishing_times", sa.JSON(), nullable=False), sa.Column("connected_platforms", sa.JSON(), nullable=False), sa.Column("content_rules", sa.JSON(), nullable=False), sa.PrimaryKeyConstraint("id"))
    op.create_index("ix_channels_name", "channels", ["name"])
    op.create_table("documents", *_timestamps(), sa.Column("project_id", sa.String(length=36), nullable=False), sa.Column("filename", sa.String(length=255), nullable=False), sa.Column("file_type", sa.String(length=60), nullable=False), sa.Column("size_bytes", sa.Integer(), nullable=False), sa.Column("authorized_for_ai", sa.Boolean(), nullable=False), sa.Column("parser_status", sa.Text(), nullable=False), sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"), sa.PrimaryKeyConstraint("id"))
    op.create_index("ix_documents_project_id", "documents", ["project_id"])
    op.create_table("ideas", *_timestamps(), sa.Column("project_id", sa.String(length=36), nullable=True), sa.Column("title", sa.String(length=240), nullable=False), sa.Column("niche", sa.String(length=120), nullable=False), sa.Column("language", sa.String(length=80), nullable=False), sa.Column("score", sa.Integer(), nullable=False), sa.Column("summary", sa.Text(), nullable=False), sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="SET NULL"), sa.PrimaryKeyConstraint("id"))
    op.create_table("storyboards", *_timestamps(), sa.Column("idea_id", sa.String(length=36), nullable=True), sa.Column("title", sa.String(length=240), nullable=False), sa.Column("hook", sa.Text(), nullable=False), sa.Column("scenes", sa.JSON(), nullable=False), sa.ForeignKeyConstraint(["idea_id"], ["ideas.id"], ondelete="SET NULL"), sa.PrimaryKeyConstraint("id"))
    op.create_table("production_plans", *_timestamps(), sa.Column("storyboard_id", sa.String(length=36), nullable=True), sa.Column("narrator", sa.String(length=180), nullable=False), sa.Column("visual_style", sa.String(length=180), nullable=False), sa.Column("format", sa.String(length=80), nullable=False), sa.Column("platforms", sa.JSON(), nullable=False), sa.Column("settings", sa.JSON(), nullable=False), sa.ForeignKeyConstraint(["storyboard_id"], ["storyboards.id"], ondelete="SET NULL"), sa.PrimaryKeyConstraint("id"))
    op.create_table("workflow_sessions", *_timestamps(), sa.Column("channel_id", sa.String(length=36), nullable=True), sa.Column("current_step", sa.String(length=120), nullable=False), sa.Column("data", sa.JSON(), nullable=False), sa.PrimaryKeyConstraint("id"))
    op.create_table("ai_agents", *_timestamps(), sa.Column("name", sa.String(length=180), nullable=False), sa.Column("specialty", sa.String(length=180), nullable=False), sa.Column("objective", sa.Text(), nullable=False), sa.Column("confidence_level", sa.Integer(), nullable=False), sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("name"))
    op.create_table("settings", *_timestamps(), sa.Column("key", sa.String(length=180), nullable=False), sa.Column("value", sa.Text(), nullable=False), sa.Column("scope", sa.String(length=80), nullable=False), sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("key"))


def downgrade() -> None:
    for table in ["settings", "ai_agents", "workflow_sessions", "production_plans", "storyboards", "ideas", "documents", "channels", "projects", "users"]:
        op.drop_table(table)
