from django import forms
from dragdrop.models import UploadFile
 
# a little intuition on forms.ModelForm
# 
# ModelForms render Model fields as HTML.
# ModelForms select validators based off of Model field definitions.
# ModelForms don't have to display/change all available fields.
# ModelForms save dictionaries to SQL tables.
# 
# Forms are "just" Python constructs. (covered previous)
# 
# 	Construct is a python library for the construction and deconstruction of 
# 	data structures in a declarative fashion. In this context, construction, or 
# 	building, refers to the process of converting (serializing) a programmatic 
# 	object into a binary representation. 
# 	
# Forms validate Python dictionaries. (covered previous)
# 
class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile