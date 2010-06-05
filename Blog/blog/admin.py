from django.contrib import admin


from blog.models import Artigo
from blog.models import Autor

admin.site.register (Artigo)
admin.site.register (Autor)



