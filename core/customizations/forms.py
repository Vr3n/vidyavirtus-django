from django import forms
from django.db.models import ForeignKey, ManyToManyField

from core.customizations.widgets import (
    TailwindCheckboxInput, TailwindTextArea,
    TailwindTextInput, TailwindTomSelectChoiceWidget,
    TailwindTomSelectModelChoiceWidget, TailwindTomSelectWidget
)


TAILWIND_WIDGETS = {
    forms.TextInput: TailwindTextInput,
    forms.Textarea: TailwindTextArea,
    forms.CheckboxInput: TailwindCheckboxInput,
    forms.ChoiceField: TailwindTomSelectChoiceWidget,
    forms.ModelChoiceField: TailwindTomSelectModelChoiceWidget,
    forms.Select: TailwindTomSelectWidget
}


class TailwindForm(forms.Form):
    """
    Base form with TailwindCSS styling for all the fields.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # the `_` is field_name value.
        for _, field in self.fields.items():
            widget_class = TAILWIND_WIDGETS.get(
                type(field.widget), field.widget.__class__
            )
            field.widget = widget_class(attrs=field.widget.attrs)


class TailwindModelForm(forms.ModelForm):
    """
    Model form with TailwindCSS styling for all the fields.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            model_field = self._meta.model._meta.get_field(field_name)

            if isinstance(model_field, (ForeignKey, ManyToManyField)):
                if not field.queryset:
                    field.queryset = model_field.related_model.objects.all()

            widget_class = TAILWIND_WIDGETS.get(
                type(field.widget), field.widget.__class__
            )
            field.widget = widget_class(attrs=field.widget.attrs)
