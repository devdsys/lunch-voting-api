from datetime import date
from sqlalchemy import func
from app.models.votes import Votes
from app.core.database import SessionLocal
from app.schemas.votes import VoteCreate

class VotesRepository:
    def __init__(self, db: SessionLocal):
        self.db = db

    def create_vote(self, vote: VoteCreate, current_employee_id: int):
        try:
            db_vote = Votes(menu_id=vote.menu_id, employee_id=current_employee_id, stars=vote.stars)
            self.db.add(db_vote)
            self.db.commit()
            self.db.refresh(db_vote)
            return db_vote
        except Exception as e:
            self.db.rollback()
            raise e

    def get_vote(self, menu_id: int, employee_id: int):
        return self.db.query(Votes).filter(Votes.menu_id == menu_id, Votes.employee_id == employee_id).first()

    def get_day_statistic(self, day: date):
        day_statistic = self.db.query(Votes.menu_id, func.avg(Votes.stars).label("avg_stars")) \
            .filter(Votes.date == day) \
            .group_by(Votes.menu_id) \
            .all()
        
        return [{"menu_id": menu_id, "avg_stars": avg_stars} for menu_id, avg_stars in day_statistic]