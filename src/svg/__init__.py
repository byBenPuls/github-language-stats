from src.svg.themes import GradientTheme, MainTheme, DarkTheme, MonokaiTheme, AmbientGradientTheme, OceanBlueGradient, \
    EternalConstanceGradientTheme, ViceCityGradientTheme, PurpinkGradientTheme

themes = {
    'gradient': GradientTheme,
    'dark': DarkTheme,
    'monokai': MonokaiTheme,
    'ambient_gradient': AmbientGradientTheme,
    'ocean_blue_gradient': OceanBlueGradient,
    'eternal_constance_gradient': EternalConstanceGradientTheme,
    'vice_city_gradient': ViceCityGradientTheme,
    'purpink_gradient': PurpinkGradientTheme
}

__all__ = ['themes', 'MainTheme']
