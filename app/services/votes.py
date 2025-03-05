from app.repositories.votes import VotesRepository
from app.schemas.votes import VoteCreate
from datetime import date

class VotesService:
    def __init__(self, votes_repository: VotesRepository):
        self.votes_repository = votes_repository

    def create_vote(self, vote: VoteCreate, current_employee_id: int):
        return self.votes_repository.create_vote(vote, current_employee_id)

    def get_vote(self, menu_id: int, employee_id: int):
        return self.votes_repository.get_vote(menu_id, employee_id)
    
    def get_day_statistic(self, day: date):
        return self.votes_repository.get_day_statistic(day)
    