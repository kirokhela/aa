import io
from datetime import datetime

from flask import Blueprint, jsonify, request, send_file
from openpyxl import Workbook
from models.evaluation import EvaluationSubmission, db

evaluation_bp = Blueprint('evaluation', __name__)

# Simple authentication - you can change this secret key
ADMIN_SECRET = "kirokhela"  # Admin password


def verify_admin(secret):
    """Simple verification function"""
    return secret == ADMIN_SECRET


@evaluation_bp.route('/submit', methods=['POST'])
def submit_evaluation():
    """Handle form submission"""
    try:
        data = request.form.to_dict()

        # Create new evaluation submission
        submission = EvaluationSubmission(
            participant_name=data.get('participant_name'),
            main_team=data.get('main_team'),
            sub_team=data.get('sub_team'),
            program_rating=int(data.get('program_rating', 0)) if data.get(
                'program_rating') else None,
            program_pros=data.get('program_pros'),
            program_cons=data.get('program_cons'),
            leaders_rating=int(data.get('leaders_rating', 0)) if data.get(
                'leaders_rating') else None,
            leaders_pros=data.get('leaders_pros'),
            leaders_cons=data.get('leaders_cons'),
            games_rating=int(data.get('games_rating', 0)) if data.get(
                'games_rating') else None,
            games_pros=data.get('games_pros'),
            games_cons=data.get('games_cons'),
            goal_delivery_rating=int(data.get('goal_delivery_rating', 0)) if data.get(
                'goal_delivery_rating') else None,
            goal_delivery_pros=data.get('goal_delivery_pros'),
            goal_delivery_cons=data.get('goal_delivery_cons'),
            logo_rating=int(data.get('logo_rating', 0)) if data.get(
                'logo_rating') else None,
            logo_pros=data.get('logo_pros'),
            logo_cons=data.get('logo_cons'),
            gift_rating=int(data.get('gift_rating', 0)) if data.get(
                'gift_rating') else None,
            gift_pros=data.get('gift_pros'),
            gift_cons=data.get('gift_cons'),
            secretary_rating=int(data.get('secretary_rating', 0)) if data.get(
                'secretary_rating') else None,
            secretary_pros=data.get('secretary_pros'),
            secretary_cons=data.get('secretary_cons'),
            media_rating=int(data.get('media_rating', 0)) if data.get(
                'media_rating') else None,
            media_pros=data.get('media_pros'),
            media_cons=data.get('media_cons'),
            emergency_rating=int(data.get('emergency_rating', 0)) if data.get(
                'emergency_rating') else None,
            emergency_pros=data.get('emergency_pros'),
            emergency_cons=data.get('emergency_cons'),
            kitchen_rating=int(data.get('kitchen_rating', 0)) if data.get(
                'kitchen_rating') else None,
            kitchen_pros=data.get('kitchen_pros'),
            kitchen_cons=data.get('kitchen_cons'),
            finance_rating=int(data.get('finance_rating', 0)) if data.get(
                'finance_rating') else None,
            finance_pros=data.get('finance_pros'),
            finance_cons=data.get('finance_cons'),
            custody_rating=int(data.get('custody_rating', 0)) if data.get(
                'custody_rating') else None,
            custody_pros=data.get('custody_pros'),
            custody_cons=data.get('custody_cons'),
            purchase_rating=int(data.get('purchase_rating', 0)) if data.get(
                'purchase_rating') else None,
            purchase_pros=data.get('purchase_pros'),
            purchase_cons=data.get('purchase_cons'),
            transportation_rating=int(data.get('transportation_rating', 0)) if data.get(
                'transportation_rating') else None,
            transportation_pros=data.get('transportation_pros'),
            transportation_cons=data.get('transportation_cons'),
            general_suggestions=data.get('general_suggestions')
        )

        db.session.add(submission)
        db.session.commit()

        return jsonify({'success': True, 'message': 'تم إرسال التقييم بنجاح'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@evaluation_bp.route('/download', methods=['GET'])
def download_excel():
    """Download all evaluations as Excel file - requires admin secret"""
    try:
        # Check for admin secret in query parameters
        secret = request.args.get('secret')
        if not verify_admin(secret):
            return jsonify({'error': 'Unauthorized access'}), 401

        # Get all submissions
        submissions = EvaluationSubmission.query.all()

        if not submissions:
            return jsonify({'error': 'No data available'}), 404

        # Create workbook and worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = "التقييمات"

        # Define headers
        headers = [
            'ID', 'تاريخ الإرسال', 'الاسم الثلاثي', 'الفريق الأساسي', 'الفريق الفرعي',
            'تقييم البرنامج', 'إيجابيات البرنامج', 'سلبيات البرنامج',
            'تقييم توزيع القادة', 'إيجابيات توزيع القادة', 'سلبيات توزيع القادة',
            'تقييم الألعاب', 'إيجابيات الألعاب', 'سلبيات الألعاب',
            'تقييم توصيل الهدف', 'إيجابيات توصيل الهدف', 'سلبيات توصيل الهدف',
            'تقييم الشعار', 'إيجابيات الشعار', 'سلبيات الشعار',
            'تقييم الهدايا', 'إيجابيات الهدايا', 'سلبيات الهدايا',
            'تقييم السكرتارية', 'إيجابيات السكرتارية', 'سلبيات السكرتارية',
            'تقييم الميديا', 'إيجابيات الميديا', 'سلبيات الميديا',
            'تقييم الإسعافات', 'إيجابيات الإسعافات', 'سلبيات الإسعافات',
            'تقييم المطبخ', 'إيجابيات المطبخ', 'سلبيات المطبخ',
            'تقييم المالية', 'إيجابيات المالية', 'سلبيات المالية',
            'تقييم العهدة', 'إيجابيات العهدة', 'سلبيات العهدة',
            'تقييم المشتريات', 'إيجابيات المشتريات', 'سلبيات المشتريات',
            'تقييم الانتقالات', 'إيجابيات الانتقالات', 'سلبيات الانتقالات',
            'الاقتراحات العامة'
        ]

        # Add headers to worksheet
        for col, header in enumerate(headers, 1):
            ws.cell(row=1, column=col, value=header)

        # Add data rows
        for row, submission in enumerate(submissions, 2):
            data = [
                submission.id,
                submission.submission_date.strftime(
                    '%Y-%m-%d %H:%M:%S') if submission.submission_date else '',
                submission.participant_name or '',
                submission.main_team or '',
                submission.sub_team or '',
                submission.program_rating or '',
                submission.program_pros or '',
                submission.program_cons or '',
                submission.leaders_rating or '',
                submission.leaders_pros or '',
                submission.leaders_cons or '',
                submission.games_rating or '',
                submission.games_pros or '',
                submission.games_cons or '',
                submission.goal_delivery_rating or '',
                submission.goal_delivery_pros or '',
                submission.goal_delivery_cons or '',
                submission.logo_rating or '',
                submission.logo_pros or '',
                submission.logo_cons or '',
                submission.gift_rating or '',
                submission.gift_pros or '',
                submission.gift_cons or '',
                submission.secretary_rating or '',
                submission.secretary_pros or '',
                submission.secretary_cons or '',
                submission.media_rating or '',
                submission.media_pros or '',
                submission.media_cons or '',
                submission.emergency_rating or '',
                submission.emergency_pros or '',
                submission.emergency_cons or '',
                submission.kitchen_rating or '',
                submission.kitchen_pros or '',
                submission.kitchen_cons or '',
                submission.finance_rating or '',
                submission.finance_pros or '',
                submission.finance_cons or '',
                submission.custody_rating or '',
                submission.custody_pros or '',
                submission.custody_cons or '',
                submission.purchase_rating or '',
                submission.purchase_pros or '',
                submission.purchase_cons or '',
                submission.transportation_rating or '',
                submission.transportation_pros or '',
                submission.transportation_cons or '',
                submission.general_suggestions or ''
            ]

            for col, value in enumerate(data, 1):
                ws.cell(row=row, column=col, value=value)

        # Save to memory
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)

        # Generate filename with current date
        filename = f"evaluation_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@evaluation_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get basic statistics - requires admin secret"""
    try:
        secret = request.args.get('secret')
        if not verify_admin(secret):
            return jsonify({'error': 'Unauthorized access'}), 401

        total_submissions = EvaluationSubmission.query.count()

        return jsonify({
            'total_submissions': total_submissions,
            'message': f'Total submissions: {total_submissions}'
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
