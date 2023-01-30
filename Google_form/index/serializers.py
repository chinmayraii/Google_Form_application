from rest_framework import serializers
from . models import (Form,Choices,Questions,Answers, Reaponses)


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        models =  Form
        field = ['__all__']

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        models =  Choices
        field = ['__all__'] 

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        models =  Questions
        field = ['__all__']

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        models =  Answers
        field = ['__all__']

class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        models =  Reaponses
        field = ['__all__']                               