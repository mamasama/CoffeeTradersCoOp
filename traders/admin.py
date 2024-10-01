from django.contrib import admin

# We want to register our models, so need to import the models
from . import models

class ProductAdmin(admin.ModelAdmin):
    '''
 		The NotesAdmin defines the interface to "Admin" - manage the notes app.
		Django already knows how to manage things in the admin.ModelAdmin Class.
		So all we are really doing, it telling it to use that class to manage it.
		
  	Hence, the "pass" - as in - do nothing.
		This will work perfectily, but display the note objects - not anything meaningful.
  
		Removing or commenting away the pass and using 
  		"list_display=('title', )" - display the title of the note, 
    	gives you a more meaningful list of note titles
    '''
    
    #pass
    list_display=('name', 'price',)


# register the Notes.Admin to manage the model.note
# as in - use the built in interface to manage "models.note" as defined in "NotesAdmin".
admin.site.register(models.Product, ProductAdmin)