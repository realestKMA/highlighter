from rest_framework import serializers
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

#--initialize variables
# get all lexers in list format
LEXERS = [lexer for lexer in get_all_lexers()]
# organize all lexers in tuples with two values ('lexer', 'LEXER')
LANGUAGES = sorted([(lexer[1][0], lexer[0]) for lexer in LEXERS])
# get and organize all styles in tuples 
STYLES = sorted([(style, style) for style in get_all_styles()])
# available formatters as @ version 0.1.1 (not released).
FORMATTERS = sorted((
    ('bbcode', 'bbcode'),
    ('html', 'html'),
    ('irc', 'irc'),
    ('rtf', 'rtf'),
    ('svg', 'svg'),
    ('text', 'text'),
    ('terminal', 'terminal'),
    ('terminal256', 'terminal256'),
))
# what kind of line number is required?
LINENUMBER = (
    ('none', 'none'),
    ('table', 'table'),
    ('inline', 'inline'),
)
# css inline styling or class names?
STYLINGS = (('inline', 'inline'), ('class', 'class'))


class HighlighterSerializer(serializers.Serializer):
    """
    Serializer for the api post request.
    """
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    language = serializers.ChoiceField(choices=LANGUAGES, default='python')
    style = serializers.ChoiceField(choices=STYLES, default='default')
    formatter = serializers.ChoiceField(choices=FORMATTERS, default='html')
    linenos = serializers.ChoiceField(choices=LINENUMBER, required=False, default='none')
    styling = serializers.ChoiceField(choices=STYLINGS, required=False, default='inline')
    divclass = serializers.CharField(required=False, default='highlighter')
    hl_lines = serializers.ListField(
        required=False,
        default=[],
        # child=serializers.IntegerField(min_value=1) #validator
    )
    nobackground = serializers.BooleanField(required=False, default=False)
    full = serializers.BooleanField(required=False, default=False)
    title = serializers.CharField(required=False)
    separate = serializers.BooleanField(required=False, default=False)
    classprefix = serializers.CharField(required=False, max_length=10, default='')

    # This serializer does not create nor updates any model instance.
