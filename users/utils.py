from .models import User

def validate_unique_email(email):
  return User.objects.filter(email=email).exists()

def validate_unique_username(username):
  # print(User.objects.filter(username=username).exists())
  return User.objects.filter(username=username).exists()
