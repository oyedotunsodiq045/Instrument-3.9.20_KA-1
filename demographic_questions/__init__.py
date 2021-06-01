from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'demographic_questions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='1. What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[
            ['Male', 'Male'], 
            ['Female', 'Female'], 
            ['Other', 'Other'], 
            ['Prefer not to answer', 'Prefer not to answer']
        ],
        label='2. What is your gender?',
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        choices=[
            ['Less than high school', 'Less than high school'], 
            ['High school or equivalent', 'High school or equivalent'], 
            ['Associate degree', 'Associate degree'], 
            ['Bachelor’s degree', 'Bachelor’s degree'],
            ['Master’s degree', 'Master’s degree'],
            ['Doctorate degree', 'Doctorate degree']
        ],
        label='3. What is the highest education level you have completed?',
        widget=widgets.RadioSelect,
    )
    experience = models.IntegerField(
        label='4. How many years of full-time work experience do you have?', 
        min=0, max=125
    )
    origin = models.StringField(
        label='5. What is your country of origin? (Not a forced response)'
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'experience', 'origin']


class Results(Page):
    pass


page_sequence = [Demographics, Results]
