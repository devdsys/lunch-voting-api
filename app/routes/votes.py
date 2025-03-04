from fastapi import APIRouter, Depends, HTTPException
from app.services.votes import VotesService
from app.repositories.votes import VotesRepository
from app.core.database import get_db
from app.schemas.votes import VoteCreate, Vote
from app.core.dependencies import get_current_employee

router = APIRouter()

class VotesController:
    def __init__(self, db=Depends(get_db)):
        self.votes_service = VotesService(VotesRepository(db))

    def get_vote_or_404(self, menu_id: int, current_user_id: int):
        db_vote = self.votes_service.get_vote(menu_id, current_user_id)
        if db_vote is None:
            raise HTTPException(status_code=404, detail="Vote not found")
        return db_vote

    def create_vote(self, menu_id: int, vote: VoteCreate, current_user):
        existing_vote = self.votes_service.get_vote(menu_id, current_user.id)
        if existing_vote:
            raise HTTPException(status_code=400, detail="Vote for this menu already exists")
        return self.votes_service.create_vote(vote, current_user.id)

    def get_vote(self, menu_id: int, current_user):
        return self.get_vote_or_404(menu_id, current_user.id)

def get_controller(db=Depends(get_db)):
    return VotesController(db)

@router.post("/", response_model=VoteCreate)
def create_vote(vote: VoteCreate, controller: VotesController = Depends(get_controller), current_user: dict = Depends(get_current_employee)):
    return controller.create_vote(vote.menu_id, vote, current_user)

@router.get("/{menu_id}", response_model=Vote)
def get_vote(menu_id: int, controller: VotesController = Depends(get_controller), current_user: dict = Depends(get_current_employee)):
    return controller.get_vote(menu_id, current_user)
