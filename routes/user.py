from fastapi import APIRouter

user = APIRouter()


@user.get('/users')
def hello():
    return 'tfuigyioyu9o'
