from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255, default = '[1,2,3,4,5,6]')
    text = models.CharField(max_length = 255)
    num_lotto = models.IntegerField(default = 5)
    update_date = models.DateField()

    #로또 번호를 생성하고 데이터베이스에 저장
    def generate(self):
        self.lottos = ""

        origin = list(range(1, 46))
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()

            self.lottos += str(guess)+ '\n'
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        #GuessNumbers Object --> 한상윤 1등 만세!
        return "%s %s" % (self.name, self.text)
