from django.contrib import admin
from .models import Quiz, Question, PlayerAnswer, PlayedQuiz, PaidQuiz, Order

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(PlayerAnswer)
admin.site.register(PlayedQuiz)
admin.site.register(PaidQuiz)
admin.site.register(Order)