from django.contrib import admin
from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        pets = obj.tagged_pets.all()
        if not pets:
            return 'No pets tagged'
        return ', '.join(str(pet) for pet in pets)

