from justpy import BasicHTMLParser


def justpy_parser_to_wp(html_string, **kwargs):
    parser = BasicHTMLParser(**kwargs)
    parser.feed(html_string)
    if len(parser.root.components) == 1:
        parser_result = parser.root.components[0]
    else:
        parser_result = parser.root
    parser_result.name_dict = parser.name_dict
    parser_result.initialize(**kwargs)
    wp = parser.wp
    wp.add_component(parser_result)
    wp.name_dict = parser.name_dict
    return wp
