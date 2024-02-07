from test_routes import router 

api_v1 = APIRouter()

api_v1.include_router(router, prefix="/test", tags=["test"])