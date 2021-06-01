from otree.api import *

c = Currency

doc = """
Please answer the following questions about yourself. There are no right or wrong answers.
"""


class Constants(BaseConstants):
    name_in_url = 'postexperimental_questions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect)


class Player(BasePlayer):
    q1 = make_q('The contract I was working under was fair')
    q2 = make_q('I think employees working under that contract would be disappointed if they did not achieve a high outcome')
    q3 = make_q('I feel a very high degree of personal ownership of the base salary received per round')
    q4 = make_q('My outcome made me happy')
    q5 = make_q('This questions are repeated intentionally to fill up space for combine scores calculation')
    q6 = make_q('This questions are repeated intentionally to fill up space for combine scores calculation')
    q7 = make_q('This questions are repeated intentionally to fill up space for combine scores calculation')
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
class PostExperimentalQuestions(Page):
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


page_sequence = [PostExperimentalQuestions, Results]
