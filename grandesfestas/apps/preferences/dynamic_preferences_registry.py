from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences import user_preferences_registry, global_preferences_registry


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = 'general'
    name = 'title'
    default = 'Grandes festas do Sonhar Acordado'
    verbose_name = 'Título do site'


@global_preferences_registry.register
class SiteUrl(StringPreference):
    section = 'general'
    name = 'site_url'
    default = 'http://localhost:8000'
    verbose_name = 'URL base do site'
