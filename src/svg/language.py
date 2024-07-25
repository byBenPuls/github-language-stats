from xml.etree import ElementTree as Et


def header():
    header_ = Et.Element('text', x='0', y='0', fill='black',
                         id='header')
    header_.text = 'Most Used Languages'
    return header_


def create_language(name: str, color: str):
    def language_name():
        element = Et.Element('text', x='15', y='10', fill='black',
                             id='lang-name')
        element.text = name
        return element

    root = Et.Element('g')

    root.append(
        Et.Element('circle', cx='5', cy='6',
                   fill=color, r='5'))
    root.append(language_name())

    return root


def languages_group(*languages):
    root = Et.Element('g', transform="translate(0, 0)")

    header_g = Et.Element("g", transform="translate(25, 35)")
    root.append(header_g)

    header_g.append(header())

    main_g = Et.Element("g", transform="translate(0, 55)")
    root.append(main_g)

    svg_ = Et.Element('svg', x='25')
    main_g.append(svg_)

    animation_delay = 450

    t_x, t_y = 0, 0
    counts = 0
    for language in languages:
        counts += 1
        if counts > 3:
            if counts == 4:
                animation_delay = 450
                t_y = 0
            t_x = 150
        g_animation = Et.Element('g', id="stagger", style=f'animation-delay: {animation_delay}ms')

        language_group = Et.Element('g',
                                    transform=f'translate({t_x}, {t_y})')
        g_animation.append(language_group)

        language_group.append(language)
        svg_.append(g_animation)
        t_y += 25
        animation_delay += 150
    return root


def no_language_data():
    root = Et.Element('g',
                      transform="translate(0, 0)")

    header_g = Et.Element("g", transform="translate(25, 35)")
    root.append(header_g)

    header_g.append(header())

    main_g = Et.Element("g", transform="translate(0, 55)")
    root.append(main_g)

    svg_ = Et.Element('svg', x='25')
    main_g.append(svg_)

    g_animation = Et.Element('g', id="stagger",
                             style=f'animation-delay: 450ms')

    language_group = Et.Element('g',
                                transform=f'translate(0, 0)')
    g_animation.append(language_group)

    message = Et.Element('text', x='0', y='11', fill='#434d58',
                         id='stat')
    message.text = 'No Languages Found'

    language_group.append(message)
    svg_.append(g_animation)

    return root
