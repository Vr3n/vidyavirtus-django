from django import forms
from django.forms.widgets import mark_safe


class TailwindTextInput(forms.TextInput):
    """
    Styled Text Input widget.
    """

    def __init__(self, *args, **kwargs):
        tw_class = kwargs.pop(
            'class',
            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        )
        kwargs['attrs'] = {'class': tw_class}
        super().__init__(*args, **kwargs)


class TailwindTextArea(forms.Textarea):
    """
    Styled Text Area widget.
    """

    def __init__(self, *args, **kwargs):
        tw_class = kwargs.pop(
            'class',
            'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        )
        kwargs['attrs'] = {'class': tw_class}
        super().__init__(*args, **kwargs)


class TailwindTomSelectWidget(forms.Select):
    """
    Select with Tailwind styles and Tom select integration.
    """

    class Media:
        css = {
            "all": ["vendors/tomselect.min.css"]
        }
        js = ['vendors/tomselect.min.js']

    def __init__(self, *args, **kwargs):
        """ Default Classes for tailwind and Tom select. """
        tw_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        kwargs.setdefault('attrs', ())
        kwargs['attrs']['class'] = kwargs['attrs'].get(
            'class', '')
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered_op = super().render(name, value, attrs, renderer)

        # TODO: Add configurable options for tomselect object.

        # Inline js to initialize Tom select.
        options = "{ 'create': true }"

        # Inline js to initialize Tom select.
        init_script = f"""
        <script type="text/javascript">
            console.log("This is the js")
            window.addEventListener('DOMContentLoaded', function () {{
                console.log("executed");
                new TomSelect('select[name="{name}"]', {options});
            }})
            htmx.onLoad(function() {{
                console.log("Hello")
                new TomSelect('select[name="{name}"]', {options});
            }})
        </script>
        """

        return mark_safe(rendered_op + init_script)


class TailwindTomSelectChoiceWidget(forms.ChoiceField):
    """
    Select with Tailwind styles and Tom select integration.
    """

    class Media:
        css = {
            "all": ["vendors/tomselect.min.css"]
        }
        js = ['vendors/tomselect.min.js']

    def __init__(self, *args, **kwargs):
        """ Default Classes for tailwind and Tom select. """
        tw_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        kwargs.setdefault('attrs', ())
        kwargs['attrs']['class'] = kwargs['attrs'].get(
            'class', '') + f'{tw_class}'
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered_op = super().render(name, value, attrs, renderer)

        # TODO: Add configurable options for tomselect object.

        # Inline js to initialize Tom select.
        options = "{ 'create': true }"
        # Inline js to initialize Tom select.
        init_script = f"""
        <script type="text/javascript">
            console.log("This is the js")
            window.addEventListener('DOMContentLoaded', function () {{
                console.log("executed");
                new TomSelect('select[name="{name}"]', {options});
            }})
            htmx.onLoad(function() {{
                console.log("Hello")
                new TomSelect('select[name="{name}"]', {options});
            }})
        </script>
        """

        return mark_safe(rendered_op + init_script)


class TailwindTomSelectModelChoiceWidget(forms.ModelChoiceField):
    """
    Select with Tailwind styles and Tom select integration.
    """

    class Media:
        css = {
            "all": ["vendors/tomselect.min.css"]
        }
        js = ['vendors/tomselect.min.js']

    def __init__(self, *args, **kwargs):
        """ Default Classes for tailwind and Tom select. """
        tw_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        kwargs.setdefault('attrs', ())
        kwargs['attrs']['class'] = kwargs['attrs'].get(
            'class', '') + f'{tw_class} tom-select'
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered_op = super().render(name, value, attrs, renderer)

        # TODO: Add configurable options for tomselect object.

        # Inline js to initialize Tom select.
        options = "{ 'create': true }"

        # Inline js to initialize Tom select.
        init_script = f"""
        <script type="text/javascript">
            console.log("This is the js")
            window.addEventListener('DOMContentLoaded', function () {{
                console.log("executed");
                new TomSelect('select[name="{name}"]', {options});
            }})
            htmx.onLoad(function() {{
                console.log("Hello")
                new TomSelect('select[name="{name}"]', {options});
            }})
        </script>
        """

        return mark_safe(rendered_op + init_script)


class TailwindCheckboxInput(forms.CheckboxInput):
    """
    Checkbox with Tailwind Stylings.
    """

    def __init__(self, *args, **kwargs):
        tw_class = kwargs.pop(
            "class",
            "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
        )
        kwargs['attrs'] = {'class': tw_class}

        super().__init__(*args, **kwargs)
