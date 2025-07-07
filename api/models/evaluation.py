import io
import os
from datetime import datetime

import psycopg2
from flask import Blueprint, jsonify, request, send_file
from openpyxl import Workbook

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_NTghsdn72GVb@ep-snowy-cherry-advjbuvm-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"
)


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def create_evaluation_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS evaluation_submissions (
                    id SERIAL PRIMARY KEY,
                    submission_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
                    participant_name TEXT,
                    main_team TEXT,
                    sub_team TEXT,
                    program_rating INTEGER,
                    program_pros TEXT,
                    program_cons TEXT,
                    leaders_rating INTEGER,
                    leaders_pros TEXT,
                    leaders_cons TEXT,
                    games_rating INTEGER,
                    games_pros TEXT,
                    games_cons TEXT,
                    goal_delivery_rating INTEGER,
                    goal_delivery_pros TEXT,
                    goal_delivery_cons TEXT,
                    logo_rating INTEGER,
                    logo_pros TEXT,
                    logo_cons TEXT,
                    gift_rating INTEGER,
                    gift_pros TEXT,
                    gift_cons TEXT,
                    secretary_rating INTEGER,
                    secretary_pros TEXT,
                    secretary_cons TEXT,
                    media_rating INTEGER,
                    media_pros TEXT,
                    media_cons TEXT,
                    emergency_rating INTEGER,
                    emergency_pros TEXT,
                    emergency_cons TEXT,
                    kitchen_rating INTEGER,
                    kitchen_pros TEXT,
                    kitchen_cons TEXT,
                    finance_rating INTEGER,
                    finance_pros TEXT,
                    finance_cons TEXT,
                    custody_rating INTEGER,
                    custody_pros TEXT,
                    custody_cons TEXT,
                    purchase_rating INTEGER,
                    purchase_pros TEXT,
                    purchase_cons TEXT,
                    transportation_rating INTEGER,
                    transportation_pros TEXT,
                    transportation_cons TEXT,
                    general_suggestions TEXT
                );
            """)
            conn.commit()
