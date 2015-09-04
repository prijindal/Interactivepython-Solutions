def moveTower(height, fromPole,toPole, withPole):
    if height>=1:
        moveTower(height-1, fromPole, withPole, toPole)
        print('Moving from', fromPole,'to', toPole)
        moveTower(height-1, withPole, toPole, fromPole)

moveTower(20, 'A', 'B', 'C')
