import psycopg2
from db_config import config

def get_or_create_user(username):
    conn = psycopg2.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT id, level FROM game_user WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        user_id, level = result
    else:
        cur.execute("INSERT INTO game_user (username, level) VALUES (%s, %s) RETURNING id", (username, 1))
        user_id = cur.fetchone()[0]
        level = 1
        conn.commit()
    cur.close()
    conn.close()
    return user_id, level

def save_score(user_id, score, level):
    conn = psycopg2.connect(**config)
    cur = conn.cursor()

    # 💾 Сохраняем в таблицу user_score
    cur.execute(
        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )

    # 🔼 Если уровень стал выше — обновляем game_user.level
    cur.execute("SELECT level FROM game_user WHERE id = %s", (user_id,))
    saved_level = cur.fetchone()[0]
    if level > saved_level:
        cur.execute("UPDATE game_user SET level = %s WHERE id = %s", (level, user_id))

    conn.commit()
    cur.close()
    conn.close()
