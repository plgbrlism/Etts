from app.db import get_db

def get_all_snippets():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT id, title, language, code, description FROM snippets ORDER BY id DESC')
    # Convert list of tuples to list of dicts for easier use in templates
    rows = cur.fetchall()
    snippets = []
    for row in rows:
        snippets.append({
            "id": row[0], "title": row[1], "language": row[2], 
            "code": row[3], "description": row[4]
        })
    return snippets

def get_snippet_by_id(snippet_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT id, title, language, code, description FROM snippets WHERE id = %s', (snippet_id,))
    row = cur.fetchone()
    if row:
        return {
            "id": row[0], "title": row[1], "language": row[2], 
            "code": row[3], "description": row[4]
        }
    return None