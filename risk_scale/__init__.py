from otree.api import *

c = Currency

author = 'Sodiq Oyedotun'

doc = """
Please indicate the extent to which you agree or disagree with the following statements [RISK SCALE]
"""


class Constants(BaseConstants):
    name_in_url = 'risk_scale'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)


class Player(BasePlayer):
    q1 = make_q('Safety First')
    q2 = make_q('I do not take risks with my health')
    q3 = make_q('I prefer to avoid risks')
    q4 = make_q('I take risks regularly')
    q5 = make_q('I really dislike not knowing what is going to happen')
    q6 = make_q('I usually view risks as a challenge')
    q7 = make_q('I view myself as')
    q8 = make_q('This questions are repeated intentionally to fill up space for combine scores calculation')
    q9 = make_q('This questions are repeated intentionally to fill up space for combine scores calculation')
    q10 = make_q('This questions are repeated intentionally to fill up space for combine scores calculation')

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()


def combine_score(positive, negative):
    return 3 + (positive - negative) / 2


# PAGES
class RiskScale(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.extraversion = combine_score(player.q6, player.q1)
        player.agreeableness = combine_score(player.q2, player.q7)
        player.conscientiousness = combine_score(player.q8, player.q3)
        player.neuroticism = combine_score(player.q9, player.q4)
        player.openness = combine_score(player.q10, player.q5)


class Results(Page):
    pass


page_sequence = [RiskScale, Results]
