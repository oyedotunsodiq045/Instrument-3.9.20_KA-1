from os import environ


SESSION_CONFIGS = [
    dict(
        name='abcapp', 
        display_name="ABC Survey (Full App)",
        app_sequence=[
            'abcapp', 
            # 'mini_quiz', 
            'postexperimental_questions', 
            'narcissism_questionnaire', 
            'risk_scale', 
            'behavioural_avoidance',
            'entitlement_questionnaire',
            'demographic_questions',   
            'payment_info'
        ], 
        num_demo_participants=3
    ),
    # dict(
    #     name='mini_quiz', 
    #     display_name="Mini Quiz (sub app)",
    #     app_sequence=['mini_quiz', 'payment_info'], 
    #     num_demo_participants=3
    # ),
    dict(
        name='postexperimental_questions', 
        display_name="Post Experimental Questions (sub app)",
        app_sequence=['postexperimental_questions', 'payment_info'], 
        num_demo_participants=3
    ),
    dict(
        name='narcissism_questionnaire', 
        display_name="Narcissism Questionnaire (sub app)",
        app_sequence=['narcissism_questionnaire', 'payment_info'], 
        num_demo_participants=3
    ),
    dict(
        name='risk_scale', 
        display_name="Risk Scale (sub app)",
        app_sequence=['risk_scale', 'payment_info'], 
        num_demo_participants=3
    ),
    dict(
        name='behavioural_avoidance', 
        display_name="Behavioural Avoidance (sub app)",
        app_sequence=['behavioural_avoidance', 'payment_info'], 
        num_demo_participants=3
    ),
    dict(
        name='entitlement_questionnaire', 
        display_name="Entitlement Questionnaire (sub app)",
        app_sequence=['entitlement_questionnaire', 'payment_info'], 
        num_demo_participants=3
    ),
    dict(
        name='demographic_questions', 
        display_name="Demographic Questions (sub app)",
        app_sequence=['demographic_questions', 'payment_info'], 
        num_demo_participants=3
    ),
]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3424299565655'

INSTALLED_APPS = ['otree']
