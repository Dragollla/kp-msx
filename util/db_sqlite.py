import sqlite3
import config

connection = sqlite3.connect(config.SQLITE_URL, autocommit=True)

connection.execute(
  '''
  CREATE TABLE IF NOT EXISTS devices (
    id TEXT PRIMARY KEY,
    code TEXT,
    refresh TEXT,
    token TEXT
  )
  '''
)

def get_device_by_id(device_id):
    cursor = connection.execute(
        '''
        SELECT id, code, refresh, token
        FROM devices
        WHERE id = ?1
        ''', [device_id])
    return to_dict(cursor.fetchone())


def create_device(entry):
    cursor = connection.execute(
        '''
        INSERT INTO devices (id, code, refresh, token)
        VALUES (?1, ?2, ?3, ?4)
        RETURNING id, code, refresh, token
        ''',
        [
            entry.get('id'),
            entry.get('code'),
            entry.get('refresh'),
            entry.get('token'),
        ]
    )
    return to_dict(cursor.fetchone())


def update_device_code(id, code):
    cursor = connection.execute(
        '''
        UPDATE devices SET code = ?2
        WHERE id = ?1
        RETURNING id, code, refresh, token
        ''',
        [ id, code ]
    )
    return to_dict(cursor.fetchone())


def update_device_tokens(id, token, refresh):
    cursor = connection.execute(
        '''
        UPDATE devices SET token = ?2, refresh = ?3
        WHERE id = ?1
        RETURNING id, code, refresh, token
        ''',
        [
            id, token, refresh
        ]
    )
    return to_dict(cursor.fetchone())


def update_tokens(token, newToken, refresh):
    cursor = connection.execute(
        '''
        UPDATE devices SET token = ?2, refresh = ?3
        WHERE token = ?1
        RETURNING id, code, refresh, token
        ''',
        [token, newToken, refresh]
    )
    return to_dict(cursor.fetchone())


def delete_device(id):
    cursor = connection.execute(
        '''
        DELETE FROM devices
        WHERE id = ?1
        RETURNING id, code, refresh, token
        ''', [id]
    )
    return to_dict(cursor.fetchone())

def to_dict(row):
    return None if row is None else {
        'id': row[0],
        'code': row[1],
        'refresh': row[2],
        'token': row[3],
    }
