import io
import os
import sys
from datetime import datetime
from models.evaluation import get_connection

from flask import (Blueprint, Flask, jsonify, request, send_file,
                   send_from_directory)
from flask_cors import CORS
from models.evaluation import create_evaluation_table, get_connection
from openpyxl import Workbook

evaluation_bp = Blueprint('evaluation', __name__)
ADMIN_SECRET = os.environ.get("ADMIN_SECRET", "kirokhela")


def verify_admin(secret):
    return secret == ADMIN_SECRET


@evaluation_bp.route('/submit', methods=['POST'])
def submit_evaluation():
    data = request.form.to_dict()
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO evaluation_submissions (
                        participant_name, main_team, sub_team,
                        program_rating, program_pros, program_cons,
                        leaders_rating, leaders_pros, leaders_cons,
                        games_rating, games_pros, games_cons,
                        goal_delivery_rating, goal_delivery_pros, goal_delivery_cons,
                        logo_rating, logo_pros, logo_cons,
                        gift_rating, gift_pros, gift_cons,
                        secretary_rating, secretary_pros, secretary_cons,
                        media_rating, media_pros, media_cons,
                        emergency_rating, emergency_pros, emergency_cons,
                        kitchen_rating, kitchen_pros, kitchen_cons,
                        finance_rating, finance_pros, finance_cons,
                        custody_rating, custody_pros, custody_cons,
                        purchase_rating, purchase_pros, purchase_cons,
                        transportation_rating, transportation_pros, transportation_cons,
                        general_suggestions
                    ) VALUES (
                        %(participant_name)s, %(main_team)s, %(sub_team)s,
                        %(program_rating)s, %(program_pros)s, %(program_cons)s,
                        %(leaders_rating)s, %(leaders_pros)s, %(leaders_cons)s,
                        %(games_rating)s, %(games_pros)s, %(games_cons)s,
                        %(goal_delivery_rating)s, %(goal_delivery_pros)s, %(goal_delivery_cons)s,
                        %(logo_rating)s, %(logo_pros)s, %(logo_cons)s,
                        %(gift_rating)s, %(gift_pros)s, %(gift_cons)s,
                        %(secretary_rating)s, %(secretary_pros)s, %(secretary_cons)s,
                        %(media_rating)s, %(media_pros)s, %(media_cons)s,
                        %(emergency_rating)s, %(emergency_pros)s, %(emergency_cons)s,
                        %(kitchen_rating)s, %(kitchen_pros)s, %(kitchen_cons)s,
                        %(finance_rating)s, %(finance_pros)s, %(finance_cons)s,
                        %(custody_rating)s, %(custody_pros)s, %(custody_cons)s,
                        %(purchase_rating)s, %(purchase_pros)s, %(purchase_cons)s,
                        %(transportation_rating)s, %(transportation_pros)s, %(transportation_cons)s,
                        %(general_suggestions)s
                    )
                """, data)
                conn.commit()
        return jsonify({'success': True, 'message': 'تم إرسال التقييم بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@evaluation_bp.route('/stats', methods=['GET'])
def get_stats():
    secret = request.args.get('secret')
    if not verify_admin(secret):
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM evaluation_submissions")
                total = cur.fetchone()[0]

        return jsonify({'total_submissions': total})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
