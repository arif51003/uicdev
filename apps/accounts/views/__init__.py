from .author_crud import AuthorCreateAPIView,AuthorDeleteAPIView,AuthorListAPIView,AuthorRetriveAPIView,AuthorUpdateAPIView
from .education_crud import EducationCreateAPIView,EducationDeleteAPIView,EducationListAPIView,EducationRetriveAPIView,EducationUpdateAPIView
from .user import UserProfileAPIView,UserRegisterAPIView

__all__=[
    AuthorCreateAPIView,
    AuthorDeleteAPIView,
    AuthorListAPIView,
    AuthorRetriveAPIView,
    AuthorUpdateAPIView,
    EducationCreateAPIView,
    EducationDeleteAPIView,
    EducationListAPIView,
    EducationRetriveAPIView,
    EducationUpdateAPIView,
    UserProfileAPIView,
    UserRegisterAPIView
]