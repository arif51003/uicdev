from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.courses.models import Category, Tag, Course, CourseTag, Module, Lesson
from apps.courses.serializers import (
    CategorySerializer,
    TagSerializer,
    CourseSerializer,
    CourseTagSerializer,
    ModuleSerializer,
    LessonSerializer,
)


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer


class TagUpdateAPIView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDeleteAPIView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all().order_by("name")
    serializer_class = CourseSerializer


class CourseUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseTagCreateAPIView(CreateAPIView):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer


class CourseTagRetrieveAPIView(RetrieveAPIView):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer


class CourseTagListAPIView(ListAPIView):
    queryset = CourseTag.objects.all().order_by("id")
    serializer_class = CourseTagSerializer


class CourseTagUpdateAPIView(UpdateAPIView):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer


class CourseTagDeleteAPIView(DestroyAPIView):
    queryset = CourseTag.objects.all()
    serializer_class = CourseTagSerializer


class ModuleCreateAPIView(CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleRetrieveAPIView(RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleListAPIView(ListAPIView):
    queryset = Module.objects.all().order_by("course_order")
    serializer_class = ModuleSerializer


class ModuleUpdateAPIView(UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleDeleteAPIView(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all().order_by("lesson_order")
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer