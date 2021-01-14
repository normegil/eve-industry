import sqlite3
import logging

from db.versions import load_versions


def connect(file):
    conn = sqlite3.connect(file)
    logging.info(f"connected to database: {file}")
    updateToCurrentVersion(conn)
    return conn


def updateToCurrentVersion(conn):
    nb_informations_table_result = conn.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='informations'")
    nb_informations_table_row = nb_informations_table_result.fetchone()

    current_version = 0
    if nb_informations_table_row[0] != 0:
        db_version_result = conn.execute("SELECT version FROM informations ORDER BY change_date DESC LIMIT 1")
        db_version_row = db_version_result.fetchone()
        current_version = db_version_row[0]

    all_versions = load_versions()
    logging.info(f"DB schema version: {current_version}; Required: {len(all_versions)}")
    for i in range(current_version, len(all_versions)):
        logging.info(f"Upgrading schema to version: {i}")
        cursor = conn.cursor()
        all_versions[i].upgrade(cursor)
        conn.execute("INSERT INTO informations(version, change_date) VALUES (?, CURRENT_TIMESTAMP);", (i,))
        conn.commit()
