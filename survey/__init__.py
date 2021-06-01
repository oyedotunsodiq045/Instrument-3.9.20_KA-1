from otree.api import *
c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'survey'
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
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'experience', 'origin']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [
    Demographics, 
    CognitiveReflectionTest
]
