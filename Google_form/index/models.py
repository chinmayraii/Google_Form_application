from django.db import models
from django.contrib.auth.models import User,AbstractUser
from . choices import QUESTION_CHOICES
from .utils.utility import generate_random_string


class User(AbstractUser, models.Model):
    email=models.EmailField(unique=True)


class BaseModel(models.Model):
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True


class Choices(BaseModel):
    choice=models.CharField(max_length=100)

    class Meta:
        db_table='choices'
        ordering=['-choice']


class Questions(BaseModel):
    question=models.CharField(max_length=100)
    question_type=models.CharField(choices=QUESTION_CHOICES, max_length=100)
    required=models.BooleanField(default=True)
    choices=models.ManyToManyField(Choices, related_name="question_choices", blank=True)        

class Form(BaseModel):
    code=models.CharField(max_length=50, unique=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    background_color=models.CharField(max_length=50,default='#272124')
    collect_email=models.BooleanField(default=True)
    questions=models.ManyToManyField(Questions, related_name='questions')

    @staticmethod
    def create_blank_form(user):
        form_token=generate_random_string()
        choices=Choices.objects.create(choice='Option 1')
        question=Questions.objects.create(question_type='multiple choice', question='Untitled questions')
        question.choices.add(choices)
        form =Form(code=form_token , title='Untitiled Form', creator=user)
        form.save()
        form.questions.add(question)
        return form



class Answers(BaseModel):
    answer=models.CharField(max_length=100)
    answer_to=models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answer_to")

class Reaponses(BaseModel):
    response_code=models.CharField(max_length=100, unique=True)
    response_to=models.ForeignKey(Form, on_delete=models.CASCADE)
    responder_ip=models.CharField(max_length=100)
    responder_email=models.EmailField(null=True)
    response=models.ManyToManyField(Answers, related_name="answers")        


