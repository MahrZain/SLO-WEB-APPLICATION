from django import forms
from django.contrib import admin
from .models import Chapter
from subjects.models import Subjects  # Import Subjects model

class ChapterAdminForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChapterAdminForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subjects.objects.none()  # Start with an empty queryset

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subject'].queryset = Subjects.objects.filter(category_id=category_id).order_by('subject_name')
            except (ValueError, TypeError):
                pass  # Invalid input; fallback to empty queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.category.subjects_set.order_by('subject_name')


class ChapterAdmin(admin.ModelAdmin):
    form = ChapterAdminForm

    class Media:
        js = ('js/admin.js',) 

admin.site.register(Chapter, ChapterAdmin)
