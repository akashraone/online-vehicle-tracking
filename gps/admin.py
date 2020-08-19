from django.contrib import admin
from .models import tracking #this line added
admin.site.register(tracking)#this line added
from .models import day #this line added
admin.site.register(day)#this line added
from .models import vehicle #this line added
admin.site.register(vehicle)#this line added
from .models import single #this line added
admin.site.register(single)#this line added 
from .models import person #this line added
admin.site.register(person)#this line added
from .models import companytable #this line added
admin.site.register(companytable)#this line added
from .models import akash #this line added
admin.site.register(akash)#this line added
from .models import driver #this line added
admin.site.register(driver)#this line added
