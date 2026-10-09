from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        tags_count = 0
        for form in self.forms:
            data = getattr(form, 'cleaned_data', None)
            if not data or data.get('DELETE'):
                continue
            tags_count += 1
            if data.get('is_main'):
                main_count += 1
        if tags_count and main_count == 0:
            raise ValidationError('Укажите основной раздел')
        if main_count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
