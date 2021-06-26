from otree.api import *

c = Currency

doc = """
Please state your level of agreement with the following questions (Behavioral avoidance /inhibition (BIS/BAS) scale)
"""


class Constants(BaseConstants):
    name_in_url = 'behavioural_avoidance'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4], widget=widgets.RadioSelect)


class Player(BasePlayer):
    q1 = make_q('A person’s family is the most import thing in life')
    q2 = make_q('Even if something bad is about to happen to me, I rarely experience fear or nervousness.')
    q3 = make_q('I go out of my way to get things I want')
    q4 = make_q('When I am doing well at something I love to keep at it.')
    q5 = make_q('I am always willing to try something new  if I think it will be fun.')
    q6 = make_q('How I dress is important to me')
    q7 = make_q('When I get something I want, I feel excited and energized')
    q8 = make_q('Criticism or scoling hurts me quite a bit.')
    q9 = make_q('When I want something I usually go all-out to get it.')
    q10 = make_q('I will often do things for no other reason than that they might be fun.')
    q11 = make_q('It\'s hard for me to find the time to do things such as get a haircut.')
    q12 = make_q('If I see a chance to get something I want I move on right away.')
    q13 = make_q('I feel pretty worried or upset when I think or know somebody is angry at me.')
    q14 = make_q('When I see an opportunity for something I like I get excited right away.')
    q15 = make_q('I often act on the spur of the moment.')
    q16 = make_q('If I think something unpleasant is going to happen I usually get pretty "worked up."')
    q17 = make_q('I often wonder why people act the way they do.')
    q18 = make_q('When good things happen to me, it affects me strongly.')
    q19 = make_q('I feel worried when I think I have done poorly at something important.')
    q20 = make_q('I crave excitement and new sensations.')
    q21 = make_q('When I go after something I use a "no holds barred" approach.')
    q22 = make_q('I have very few fears compared to my friends.')
    q23 = make_q('It would excite me to win a contest.')
    q24 = make_q('I worry about making mistakes.')

    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()


def combine_score(positive, negative):
    return 3 + (positive - negative) / 2


# PAGES
class BehaviouralAvoidance(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 
        'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.extraversion = combine_score(player.q6, player.q1)
        player.agreeableness = combine_score(player.q2, player.q7)
        player.conscientiousness = combine_score(player.q8, player.q3)
        player.neuroticism = combine_score(player.q9, player.q4)
        player.openness = combine_score(player.q10, player.q5)


class Results(Page):
    pass


page_sequence = [BehaviouralAvoidance, Results]
