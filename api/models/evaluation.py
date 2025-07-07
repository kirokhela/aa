from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EvaluationSubmission(db.Model):
    __tablename__ = 'evaluation_submissions'

    id = db.Column(db.Integer, primary_key=True)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Personal Information
    participant_name = db.Column(db.String(255))
    main_team = db.Column(db.String(100))
    sub_team = db.Column(db.String(100))

    # Program Section
    program_rating = db.Column(db.Integer)
    program_pros = db.Column(db.Text)
    program_cons = db.Column(db.Text)

    # Leaders Distribution Section
    leaders_rating = db.Column(db.Integer)
    leaders_pros = db.Column(db.Text)
    leaders_cons = db.Column(db.Text)

    # Games Section
    games_rating = db.Column(db.Integer)
    games_pros = db.Column(db.Text)
    games_cons = db.Column(db.Text)

    # Goal Delivery Section
    goal_delivery_rating = db.Column(db.Integer)
    goal_delivery_pros = db.Column(db.Text)
    goal_delivery_cons = db.Column(db.Text)

    # Logo Section
    logo_rating = db.Column(db.Integer)
    logo_pros = db.Column(db.Text)
    logo_cons = db.Column(db.Text)

    # Gifts Section
    gift_rating = db.Column(db.Integer)
    gift_pros = db.Column(db.Text)
    gift_cons = db.Column(db.Text)

    # Secretary Section
    secretary_rating = db.Column(db.Integer)
    secretary_pros = db.Column(db.Text)
    secretary_cons = db.Column(db.Text)

    # Media Section
    media_rating = db.Column(db.Integer)
    media_pros = db.Column(db.Text)
    media_cons = db.Column(db.Text)

    # Emergency Section
    emergency_rating = db.Column(db.Integer)
    emergency_pros = db.Column(db.Text)
    emergency_cons = db.Column(db.Text)

    # Kitchen Section
    kitchen_rating = db.Column(db.Integer)
    kitchen_pros = db.Column(db.Text)
    kitchen_cons = db.Column(db.Text)

    # Finance Section
    finance_rating = db.Column(db.Integer)
    finance_pros = db.Column(db.Text)
    finance_cons = db.Column(db.Text)

    # Custody Section
    custody_rating = db.Column(db.Integer)
    custody_pros = db.Column(db.Text)
    custody_cons = db.Column(db.Text)

    # Purchase Section
    purchase_rating = db.Column(db.Integer)
    purchase_pros = db.Column(db.Text)
    purchase_cons = db.Column(db.Text)

    # Transportation Section
    transportation_rating = db.Column(db.Integer)
    transportation_pros = db.Column(db.Text)
    transportation_cons = db.Column(db.Text)

    # General Suggestions
    general_suggestions = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'submission_date': self.submission_date.isoformat() if self.submission_date else None,
            'participant_name': self.participant_name,
            'main_team': self.main_team,
            'sub_team': self.sub_team,
            'program_rating': self.program_rating,
            'program_pros': self.program_pros,
            'program_cons': self.program_cons,
            'leaders_rating': self.leaders_rating,
            'leaders_pros': self.leaders_pros,
            'leaders_cons': self.leaders_cons,
            'games_rating': self.games_rating,
            'games_pros': self.games_pros,
            'games_cons': self.games_cons,
            'goal_delivery_rating': self.goal_delivery_rating,
            'goal_delivery_pros': self.goal_delivery_pros,
            'goal_delivery_cons': self.goal_delivery_cons,
            'logo_rating': self.logo_rating,
            'logo_pros': self.logo_pros,
            'logo_cons': self.logo_cons,
            'gift_rating': self.gift_rating,
            'gift_pros': self.gift_pros,
            'gift_cons': self.gift_cons,
            'secretary_rating': self.secretary_rating,
            'secretary_pros': self.secretary_pros,
            'secretary_cons': self.secretary_cons,
            'media_rating': self.media_rating,
            'media_pros': self.media_pros,
            'media_cons': self.media_cons,
            'emergency_rating': self.emergency_rating,
            'emergency_pros': self.emergency_pros,
            'emergency_cons': self.emergency_cons,
            'kitchen_rating': self.kitchen_rating,
            'kitchen_pros': self.kitchen_pros,
            'kitchen_cons': self.kitchen_cons,
            'finance_rating': self.finance_rating,
            'finance_pros': self.finance_pros,
            'finance_cons': self.finance_cons,
            'custody_rating': self.custody_rating,
            'custody_pros': self.custody_pros,
            'custody_cons': self.custody_cons,
            'purchase_rating': self.purchase_rating,
            'purchase_pros': self.purchase_pros,
            'purchase_cons': self.purchase_cons,
            'transportation_rating': self.transportation_rating,
            'transportation_pros': self.transportation_pros,
            'transportation_cons': self.transportation_cons,
            'general_suggestions': self.general_suggestions
        }
