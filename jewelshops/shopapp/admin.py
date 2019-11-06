from django.contrib import admin

# Register your models here.
from shopapp.models import Profile
from shopapp.models import Store

from shopapp.models import Jewel
from shopapp.models import Checkout

admin.site.register(Profile)
admin.site.register(Store)	
#admin.site.register(Cart)
admin.site.register(Jewel)
admin.site.register(Checkout)