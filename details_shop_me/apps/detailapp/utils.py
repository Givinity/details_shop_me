from .models import Category

menu = [
    {'title': 'Главная', "url_name": 'index'},
    {'title': 'Каталог', "url_name": 'catalog'},
    {'title': 'О нас', "url_name": 'info'},
    {'title': 'Контакты', "url_name": 'contacts'},
]


class DataMixin:
    """
    Дублирующий код для представлений
    """

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        return context
