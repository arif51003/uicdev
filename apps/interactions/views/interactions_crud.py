from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.interactions.models import (
    Enrollment,
    LessonAnswer,
    LessonQuestion,
    LessonRate,
    LessonResource,
    UserHomeworkAttempt,
)
from apps.interactions.serializers import (
    EnrollmentSerializer,
    LessonAnswerSerializer,
    LessonQuestionSerializer,
    LessonRateSerializer,
    LessonResourceSerializer,
    UserHomeworkAttemptSerializer,
)


class EnrollmentCreateAPIView(CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentRetrieveAPIView(RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentListAPIView(ListAPIView):
    queryset = Enrollment.objects.all().order_by("-started_at")
    serializer_class = EnrollmentSerializer


class EnrollmentUpdateAPIView(UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDeleteAPIView(DestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class LessonQuestionCreateAPIView(CreateAPIView):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer


class LessonQuestionRetrieveAPIView(RetrieveAPIView):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer


class LessonQuestionListAPIView(ListAPIView):
    queryset = LessonQuestion.objects.all().order_by("-created_at")
    serializer_class = LessonQuestionSerializer


class LessonQuestionUpdateAPIView(UpdateAPIView):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer


class LessonQuestionDeleteAPIView(DestroyAPIView):
    queryset = LessonQuestion.objects.all()
    serializer_class = LessonQuestionSerializer


class LessonAnswerCreateAPIView(CreateAPIView):
    queryset = LessonAnswer.objects.all()
    serializer_class = LessonAnswerSerializer


class LessonAnswerRetrieveAPIView(RetrieveAPIView):
    queryset = LessonAnswer.objects.all()
    serializer_class = LessonAnswerSerializer


class LessonAnswerListAPIView(ListAPIView):
    queryset = LessonAnswer.objects.all().order_by("-created_at")
    serializer_class = LessonAnswerSerializer


class LessonAnswerUpdateAPIView(UpdateAPIView):
    queryset = LessonAnswer.objects.all()
    serializer_class = LessonAnswerSerializer


class LessonAnswerDeleteAPIView(DestroyAPIView):
    queryset = LessonAnswer.objects.all()
    serializer_class = LessonAnswerSerializer


class LessonResourceCreateAPIView(CreateAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer


class LessonResourceRetrieveAPIView(RetrieveAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer


class LessonResourceListAPIView(ListAPIView):
    queryset = LessonResource.objects.all().order_by("-created_at")
    serializer_class = LessonResourceSerializer


class LessonResourceUpdateAPIView(UpdateAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer


class LessonResourceDeleteAPIView(DestroyAPIView):
    queryset = LessonResource.objects.all()
    serializer_class = LessonResourceSerializer


class LessonRateCreateAPIView(CreateAPIView):
    queryset = LessonRate.objects.all()
    serializer_class = LessonRateSerializer


class LessonRateRetrieveAPIView(RetrieveAPIView):
    queryset = LessonRate.objects.all()
    serializer_class = LessonRateSerializer


class LessonRateListAPIView(ListAPIView):
    queryset = LessonRate.objects.all().order_by("-created_at")
    serializer_class = LessonRateSerializer


class LessonRateUpdateAPIView(UpdateAPIView):
    queryset = LessonRate.objects.all()
    serializer_class = LessonRateSerializer


class LessonRateDeleteAPIView(DestroyAPIView):
    queryset = LessonRate.objects.all()
    serializer_class = LessonRateSerializer


class UserHomeworkAttemptCreateAPIView(CreateAPIView):
    queryset = UserHomeworkAttempt.objects.all()
    serializer_class = UserHomeworkAttemptSerializer


class UserHomeworkAttemptRetrieveAPIView(RetrieveAPIView):
    queryset = UserHomeworkAttempt.objects.all()
    serializer_class = UserHomeworkAttemptSerializer


class UserHomeworkAttemptListAPIView(ListAPIView):
    queryset = UserHomeworkAttempt.objects.all().order_by("-created_at")
    serializer_class = UserHomeworkAttemptSerializer


class UserHomeworkAttemptUpdateAPIView(UpdateAPIView):
    queryset = UserHomeworkAttempt.objects.all()
    serializer_class = UserHomeworkAttemptSerializer


class UserHomeworkAttemptDeleteAPIView(DestroyAPIView):
    queryset = UserHomeworkAttempt.objects.all()
    serializer_class = UserHomeworkAttemptSerializer