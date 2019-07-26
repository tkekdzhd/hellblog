from django.db import models

# Create your models here.
class Blog(models.Model): # Blog라는 이름의 객체를 만들겠다
    title = models.CharField(max_length=200) # title이라는 이름으로 최대 200글자의 데이터를 갖겠다
    pub_date = models.DateTimeField('date published') # pub_date라는 이름으로 시간 날짜 데이터를 받겠다
    body = models.TextField() # body라는 줄글 데이터가 포함됩니다.

    def __str__(self):
        return self.title