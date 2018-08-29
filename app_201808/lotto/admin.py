from django.contrib import admin
from .models import GuessNumbers
#from lottos.models import GuessNumbers
# 같은 위치이기 때문에 lottos를 삭제해도 된다.


# Register your models here.
admin.site.register(GuessNumbers)# class 이름을 넣어주어야 한다.
