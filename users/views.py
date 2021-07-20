from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import filters, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

from .permissions import IsAdmin
from .serializers import EmailCodeTokenObtainPairSerializer, UserSerializer


User = get_user_model()


class EmailCodeTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailCodeTokenObtainPairSerializer
    permission_classes = []


@api_view(['POST'])
@permission_classes((AllowAny, ))
def send_confirmation_code(request):
    serializer = UserSerializer(data=request.data)
    email = request.data.get('email', False)
    serializer.is_valid(raise_exception=True)
    confirmation_code = str(uuid4())
    user, _ = User.objects.get_or_create(email=email)
    user.update(
        confirmation_code=make_password(
            confirmation_code, salt=None, hasher='default')
    )
    mail_subject = 'Код подтверждения на Yamdb.ru'
    message = f'Ваш код подтверждения: {confirmation_code}'
    send_mail(mail_subject, message, 'Yamdb.ru <admin@yamdb.ru>', [email])
    return Response(
        f'Код отправлен на адрес {email}', status=status.HTTP_200_OK)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    lookup_field = 'username'
    permission_classes = [IsAdmin]

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        else:
            serializer = self.get_serializer(request.user)

        return Response(serializer.data)
