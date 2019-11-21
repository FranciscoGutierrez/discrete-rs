
from durable.lang import *

with ruleset('test'):
    # antecedent
    @when_all(m.subject == 'out-of-bed')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'leakage')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'urine-detection')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'time-day')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'wet-sheets')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'decubitus')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'wandering')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'feces-detection')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'check-timing')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'check-micturition')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'fall-risk')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'perm-extra-attention')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'check-falls')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'san-call')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'nor-call')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'call-history')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'check-todos')
    def say_hello(c):
        # consequent
        print ('Subject is {0}'.format(c.m.subject))

    @when_all(m.subject == 'planned-todo')
    def say_hello(c):
            # consequent
            print ('Subject is {0}'.format(c.m.subject))


post('test', { 'subject': 'out-of-bed' })
