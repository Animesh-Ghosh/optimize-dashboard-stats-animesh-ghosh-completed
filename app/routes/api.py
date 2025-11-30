from fastapi import APIRouter, HTTPException, Query
from app.database import get_connection, put_connection
from app.schemas.schemas import StatsResponse, ActivityItem, ActivityListResponse
from typing import List

router = APIRouter(prefix="/api/dashboard")

@router.get("/stats", response_model=StatsResponse)
def get_stats():
    conn = get_connection()
    cur = conn.cursor()
    try:
        users_count_query = cur.execute("SELECT COUNT(id) FROM users")
        users_count = users_count_query.fetchone()[0]
        posts_count_query = cur.execute("SELECT COUNT(id) FROM posts")
        posts_count = posts_count_query.fetchone()[0]
        comments_count_query = cur.execute("SELECT COUNT(id) FROM comments")
        comments_count = comments_count_query.fetchone()[0]
        sessions_count_query = cur.execute("SELECT COUNT(id) FROM sessions")
        sessions_count = sessions_count_query.fetchone()[0]
        return {
            "users": users_count,
            "posts": posts_count,
            "comments": comments_count,
            "sessions": sessions_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        put_connection(conn)

@router.get("/recent-activity", response_model=ActivityListResponse)
def recent_activity(offset: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=100)):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT id, user_id, action, created_at FROM activities ORDER BY created_at DESC, id DESC OFFSET {offset} LIMIT {limit}")
        rows = cur.fetchall()
        activities = [
            {"id": row[0], "user_id": row[1], "action": row[2], "created_at": row[3].isoformat()} for row in rows
        ]
        return {"activities": activities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        put_connection(conn)
