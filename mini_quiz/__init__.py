from otree.api import *
import random

c = Currency

author = 'Sodiq Oyedotun'

doc = """
Before we begin, we would like to ask you some questions regarding your task and your incentive contract to make sure you understand the instructions.
"""


class Constants(BaseConstants):
    name_in_url = 'mini_quiz'
    players_per_group = 3
    num_rounds = 10

    endowment = cu(1000)

    # Bonus / no penalty
    outcome = 0
    bonus_base_salary = 1000
    bonus_low_outcome = 0
    bonus_medium_outcome = 1000
    bonus_high_outcome = 2000

    # No bonus / penalty
    penalty_base_salary = 3000
    penalty_low_outcome = -2000
    penalty_medium_outcome = -1000
    penalty_high_outcome = 0

    # Bonus / penalty
    bonus_penalty_base_salary = 2000
    bonus_penalty_low_outcome = -1000
    bonus_penalty_medium_outcome = 0
    bonus_penalty_high_outcome = 1000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

# Incentive Contract
    # Bonus / no penalty
    outcome = models.CurrencyField()
    bonus_base_salary = models.CurrencyField()
    bonus_low_outcome = models.CurrencyField()
    bonus_medium_outcome = models.CurrencyField()
    bonus_high_outcome = models.CurrencyField()

    # No bonus / penalty
    penalty_base_salary = models.CurrencyField()
    penalty_low_outcome = models.CurrencyField()
    penalty_medium_outcome = models.CurrencyField()
    penalty_high_outcome = models.CurrencyField()

    # Bonus / penalty
    bonus_penalty_base_salary = models.CurrencyField()
    bonus_penalty_low_outcome = models.CurrencyField()
    bonus_penalty_medium_outcome = models.CurrencyField()
    bonus_penalty_high_outcome = models.CurrencyField()

# Mini Quiz questions
    # quiz_1_answer = 'associated with a higher monetary cost to me.'
    quiz_1_answer = models.CharField(initial="associated with a higher probability of me achieving a higher outcome level.")
    quiz_1 = models.StringField(
        choices=['not associated with a monetary cost to me.', 'associated with a lower monetary cost to me.', 'associated with a higher monetary cost to me.'],
        label="1) In each round, a higher effort level is",
        widget=widgets.RadioSelect
    )

    # quiz_2_answer = 'associated with a higher probability of me achieving a higher outcome level.'
    quiz_2_answer = models.CharField(initial="associated with a higher probability of me achieving a higher outcome level.")
    quiz_2 = models.StringField(
        choices=['associated with a lower probability of me achieving a higher outcome level.', 'associated with a higher probability of me achieving a higher outcome level.', 'not associated with the probability of me achieving a higher outcome level.'],
        label="2) In each round, a higher effort level is",
        widget=widgets.RadioSelect
    )

    # quiz_3_bonus_answer = 'a base salary of 1,000 Lira.'
    quiz_3_bonus_answer = models.CharField(initial="a base salary of 1,000 Lira.")
    quiz_3_bonus = models.StringField(
        choices=['no base salary', 'a base salary of 1,000 Lira.', 'a base salary of 2,000 Lira.', 'a base salary of 3,000 Lira.'],
        label="3) For each round, I will be paid",
        widget=widgets.RadioSelect
    )

    # quiz_3_bonus_penalty_answer = 'a base salary of 2,000 Lira.'
    quiz_3_bonus_penalty_answer = models.CharField(initial="a base salary of 2,000 Lira.")
    quiz_3_bonus_penalty = models.StringField(
        choices=['no base salary', 'a base salary of 1,000 Lira.', 'a base salary of 2,000 Lira.', 'a base salary of 3,000 Lira.'],
        label="3) For each round, I will be paid",
        widget=widgets.RadioSelect
    )

    # quiz_3_penalty_answer = 'a base salary of 3,000 Lira.'
    quiz_3_penalty_answer = models.CharField(initial="a base salary of 3,000 Lira.")
    quiz_3_penalty = models.StringField(
        choices=['no base salary', 'a base salary of 1,000 Lira.', 'a base salary of 2,000 Lira.', 'a base salary of 3,000 Lira.'],
        label="3) For each round, I will be paid",
        widget=widgets.RadioSelect
    )

    # quiz_4_bonus_answer = 'My pay will be higher because I will receive a higher bonus.'
    quiz_4_bonus_answer = models.CharField(initial="My pay will be higher because I will receive a higher bonus.")
    quiz_4_bonus = models.StringField(
        choices=['My pay will be higher because I will receive a higher bonus.', 'My pay will not be affected.', 'My pay will be lower because I will receive a lower bonus.'],
        label="4) For each round, without considering the monetary cost of effort, if I achieve a higher outcome level,",
        widget=widgets.RadioSelect
    )

    # quiz_4_penalty_answer = 'My pay will be higher because I will incur a lower bonus.'
    quiz_4_penalty_answer = models.CharField(initial="My pay will be higher because I will incur a lower bonus.")
    quiz_4_penalty = models.StringField(
        choices=['My pay will be higher because I will incur a lower bonus.', 'My pay will not be affected.', 'My pay will be lower because I will incur a higher bonus.'],
        label="4) For each round, without considering the monetary cost of effort, if I achieve a higher outcome level,",
        widget=widgets.RadioSelect
    )

    # quiz_4_bonus_penalty_answer = 'My pay will be higher because I will receive a bonus and avoid a penalty.'
    quiz_4_bonus_penalty_answer = models.CharField(initial="My pay will be higher because I will receive a bonus and avoid a penalty.")
    quiz_4_bonus_penalty = models.StringField(
        choices=['My pay will be higher because I will receive a bonus and avoid a penalty.', 'My pay will not be affected.', 'My pay will be lower because I will not receive a bonus and will incur a penalty.'],
        label="4) For each round, without considering the monetary cost of effort, if I achieve a higher outcome level,",
        widget=widgets.RadioSelect
    )


class Player(BasePlayer):
# Incentive Contract
    # Bonus / no penalty
    outcome = models.CurrencyField()
    bonus_base_salary = models.CurrencyField()
    bonus_low_outcome = models.CurrencyField()
    bonus_medium_outcome = models.CurrencyField()
    bonus_high_outcome = models.CurrencyField()
    # outcome = models.IntegerField(initial=0)
    # bonus_base_salary = models.IntegerField(initial=1000)
    # bonus_low_outcome = models.IntegerField(initial=0)
    # bonus_medium_outcome = models.IntegerField(initial=1000)
    # bonus_high_outcome = models.IntegerField(initial=2000)
    # outcome = 0
    # bonus_base_salary = 1000
    # bonus_low_outcome = 0
    # bonus_medium_outcome = 1000
    # bonus_high_outcome = 2000
    # bonus_low_outcome = bonus_base_salary
    # bonus_medium_outcome = bonus_base_salary + 1000
    # bonus_high_outcome = bonus_base_salary + 2000

    # No bonus / penalty
    penalty_base_salary = models.CurrencyField()
    penalty_low_outcome = models.CurrencyField()
    penalty_medium_outcome = models.CurrencyField()
    penalty_high_outcome = models.CurrencyField()
    # penalty_base_salary = models.IntegerField(initial=3000)
    # penalty_low_outcome = models.IntegerField(initial=-2000)
    # penalty_medium_outcome = models.IntegerField(initial=-1000)
    # penalty_high_outcome = models.IntegerField(initial=0)
    # penalty_base_salary = 3000
    # penalty_low_outcome = -2000
    # penalty_medium_outcome = -1000
    # penalty_high_outcome = 0
    # penalty_low_outcome = penalty_base_salary - 2000
    # penalty_medium_outcome = penalty_base_salary - 1000
    # penalty_high_outcome = penalty_base_salary

    # Bonus / penalty
    bonus_penalty_base_salary = models.CurrencyField()
    bonus_penalty_low_outcome = models.CurrencyField()
    bonus_penalty_medium_outcome = models.CurrencyField()
    bonus_penalty_high_outcome = models.CurrencyField()
    # bonus_penalty_base_salary = models.IntegerField(initial=2000)
    # bonus_penalty_low_outcome = models.IntegerField(initial=-1000)
    # bonus_penalty_medium_outcome = models.IntegerField(initial=0)
    # bonus_penalty_high_outcome = models.IntegerField(initial=1000)
    # bonus_penalty_base_salary = 2000
    # bonus_penalty_low_outcome = -1000
    # bonus_penalty_medium_outcome = 0
    # bonus_penalty_high_outcome = 1000
    # bonus_penalty_low_outcome = bonus_penalty_base_salary - 1000
    # bonus_penalty_medium_outcome = bonus_penalty_base_salary
    # bonus_penalty_high_outcome = bonus_penalty_base_salary + 1000


# Effort Levels


# PAGES
class BonusPage(Page):

    form_model = 'group'
    form_fields = ['quiz_1', 'quiz_2', 'quiz_3_bonus', 'quiz_4_bonus']

    # def before_next_page(self):
    #     """ 
    #         bonus_high_outcome   = 4/4
    #         bonus_medium_outcome = 2/3 and 3/4
    #         bonus_low_outcome    = 0/4 and 1/4
    #     """
    #     if self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus == quiz_3_bonus_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer :
    #         self.player.outcome = self.player.bonus_base_salary + self.player.bonus_high_outcome
    #         return self.player.outcome

    #     elif (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus == quiz_3_bonus_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_3_bonus == quiz_3_bonus_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus == quiz_3_bonus_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer) :
    #         self.player.outcome = self.player.bonus_base_salary + self.player.bonus_medium_outcome
    #         return self.player.outcome

    #     elif (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_3_bonus == quiz_3_bonus_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus == quiz_3_bonus_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer) or (self.player.quiz_3_bonus == quiz_3_bonus_answer and self.player.quiz_4_bonus == quiz_4_bonus_answer) :
    #         self.player.outcome = self.player.bonus_base_salary + self.player.bonus_medium_outcome
    #         return self.player.outcome

    #     else:
    #         self.player.outcome = self.player.bonus_base_salary + self.player.bonus_low_outcome
    #         return self.player.outcome


class PenaltyPage(Page):
    form_model = 'group'
    form_fields = ['quiz_1', 'quiz_2', 'quiz_3_penalty', 'quiz_4_penalty']

    # def before_next_page(self):
    #     """ 
    #         penalty_high_outcome   = 4/4
    #         penalty_medium_outcome = 2/3 and 3/4
    #         penalty_low_outcome    = 0/4 and 1/4
    #     """
    #     if self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_penalty == quiz_3_penalty_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer :
    #         self.player.outcome = self.player.penalty_base_salary + self.player.penalty_high_outcome
    #         return self.player.outcome

    #     elif (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_penalty == quiz_3_penalty_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_3_penalty == quiz_3_penalty_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_penalty == quiz_3_penalty_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer) :
    #         self.player.outcome = self.player.penalty_base_salary + self.player.penalty_medium_outcome
    #         return self.player.outcome

    #     elif (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_3_penalty == quiz_3_penalty_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_penalty == quiz_3_penalty_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer) or (self.player.quiz_3_penalty == quiz_3_penalty_answer and self.player.quiz_4_penalty == quiz_4_penalty_answer) :
    #         self.player.outcome = self.player.penalty_base_salary + self.player.penalty_medium_outcome
    #         return self.player.outcome

    #     else:
    #         self.player.outcome = self.player.penalty_base_salary + self.player.penalty_low_outcome
    #         return self.player.outcome


class BonusPenaltyPage(Page):
    form_model = 'group'
    form_fields = ['quiz_1', 'quiz_2', 'quiz_3_bonus_penalty', 'quiz_4_bonus_penalty']

    # def before_next_page(self):
    #     """ 
    #         bonus_penalty_high_outcome   = 4/4
    #         bonus_penalty_medium_outcome = 2/3 and 3/4
    #         bonus_penalty_low_outcome    = 0/4 and 1/4
    #     """
    #     if self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer :
    #         self.player.outcome = self.player.bonus_penalty_base_salary + self.player.bonus_penalty_high_outcome
    #         return self.player.outcome

    #     elif (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer) :
    #         self.player.outcome = self.player.bonus_penalty_base_salary + self.player.bonus_penalty_medium_outcome
    #         return self.player.outcome

    #     elif (self.player.quiz_1 == quiz_1_answer and self.player.quiz_2 == quiz_2_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer) or (self.player.quiz_1 == quiz_1_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer) or (self.player.quiz_2 == quiz_2_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer) or (self.player.quiz_3_bonus_penalty == quiz_3_bonus_penalty_answer and self.player.quiz_4_bonus_penalty == quiz_4_bonus_penalty_answer) :
    #         self.player.outcome = self.player.bonus_penalty_base_salary + self.player.bonus_penalty_medium_outcome
    #         return self.player.outcome

    #     else:
    #         self.player.outcome = self.player.bonus_penalty_base_salary + self.player.bonus_penalty_low_outcome
    #         return self.player.outcome


class Results(Page):
    def is_displayed(self):
        pass


page_sequence = [BonusPage, Results]
# page_sequence = [BonusPage, PenaltyPage, BonusPenaltyPage, Results]
