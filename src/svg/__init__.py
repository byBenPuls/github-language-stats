from src.svg.themes import Gradient, Main, Dark, Monokai, AmbientGradient, OceanBlueGradient, \
    EternalConstanceGradient, ViceCityGradient, PurpinkGradient

themes = {
    'gradient': Gradient,
    'dark': Dark,
    'monokai': Monokai,
    'ambient_gradient': AmbientGradient,
    'ocean_blue_gradient': OceanBlueGradient,
    'eternal_constance_gradient': EternalConstanceGradient,
    'vice_city_gradient': ViceCityGradient,
    'purpink_gradient': PurpinkGradient
}

__all__ = ['themes', 'Main']
