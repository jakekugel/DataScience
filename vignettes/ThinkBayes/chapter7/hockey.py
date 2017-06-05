''' This contains code that demonstrates solutions to problems from
chapter 7 of Allen Downey's book 'Think Bayes'.
'''

import thinkbayes2
from thinkbayes2 import Suite
import thinkplot


class Team(Suite):
    '''Models the long-term distribution of goals for a team'''
    def __init__(self, label):
        pmf = thinkbayes2.MakeNormalPmf(2.7, 0.3, 4, n=10)
        Suite.__init__(self, pmf)
        self.label = label

    def Likelihood(self, data, hypo):
        '''Likelihood of '''
        lam = hypo
        k = data
        like = thinkbayes2.EvalPoissonPmf(k, lam)
        return like

def MakeGoalPmf(suite, label):
    '''Given a PMF with team long-term average goals, creates
       an aggregate of Poisson PMF for each long-term average goal 'bucket'.'''
    metapmf = thinkbayes2.Pmf()

    for lam, prob in suite.Items():
        pmf = thinkbayes2.MakePoissonPmf(lam, 10)
        metapmf.Set(pmf, prob)

    mix = thinkbayes2.MakeMixture(metapmf)
    mix.label = label
    return mix

def main():
    '''Main entry point'''
    bruins = Team('Bruins')
    bruins.Update(0)
    bruins.Update(2)
    bruins.Update(8)
    bruins.Update(4)
    # bruins.UpdateSet([0, 2, 8, 4])

    canucks = Team('Canucks')
    canucks.Update(1)
    canucks.Update(3)
    canucks.Update(1)
    canucks.Update(0)
    # canucks.UpdateSet([1, 3, 1, 0])

    # Use Allen Downey's thinkplot module to create a graph
    thinkplot.PrePlot(1)
    thinkplot.Plot(bruins)
    thinkplot.Plot(canucks)
    thinkplot.Save(root='hockey',
                   xlabel='Average goals per game',
                   ylabel='Probability',
                   formats=['pdf'])

    # Compute distribution of goals for next game
    bruins_next_game = MakeGoalPmf(bruins, 'Bruins')
    canucks_next_game = MakeGoalPmf(canucks, 'Canucks')
    
    # Use Allen Downey's thinkplot module to create a graph
    thinkplot.PrePlot(1)
    thinkplot.Plot(bruins_next_game)
    thinkplot.Plot(canucks_next_game)
    thinkplot.Save(root='hockey-next-game',
                   xlabel='Goals in next game',
                   ylabel='Probability',
                   formats=['pdf'])

    diff = bruins_next_game - canucks_next_game

    p_win = diff.ProbGreater(0)
    p_loss = diff.ProbLess(0)
    p_tie = diff.Prob(0)

    print('Probability of Bruins win: {0}'.format(str(p_win)))
    print('Probability of Bruins loss: {0}'.format(str(p_loss)))
    print('Probability of tie: {0}'.format(str(p_tie)))

if __name__ == "__main__":
    main()
