import turtle
from PycharmProjects.ModelsGragh.graphics import *
import math
import random


def staticModels(win, lhXY, mhXY, rhXY, lmXY, mmXY, rmXY, ldXY, mdXY, rdXY, k):
    board = [lhXY, mhXY, rhXY, rmXY, rdXY, mdXY, ldXY, lmXY]
    for i in range(len(board)):
        Line(board[i], board[(i + 1) % len(board)]).draw(win)

    pK = 36 * k
    dis = 50 * k
    cirRad = 60 * k
    rad = 5 * k
    hsliv = 25 * k
    PlaceforBall = 23 * k
    # Баки для воды
    Rectangle(lhXY, Point(lhXY.getX() + pK, lhXY.getY() - pK)).draw(win)
    Rectangle(rhXY, Point(rhXY.getX() - pK, rhXY.getY() - pK)).draw(win)

    # Cтратовые зоны
    Rectangle(lhXY, Point(lhXY.getX() + pK, lhXY.getY() + 2 * pK)).draw(win)
    Rectangle(rhXY, Point(rhXY.getX() - pK, rhXY.getY() + 2 * pK)).draw(win)

    # Зоны для маячков слева
    Rectangle(lhXY, Point(lhXY.getX() - pK / 3, lhXY.getY() + pK / 3)).draw(win)
    Rectangle(lmXY, Point(lmXY.getX() - pK / 3, lmXY.getY() - pK / 3)).draw(win)
    Rectangle(ldXY, Point(ldXY.getX() - pK / 3, ldXY.getY() - pK / 3)).draw(win)

    # Зоны для маячков справа
    Rectangle(rhXY, Point(rhXY.getX() + pK / 3, rhXY.getY() + pK / 3)).draw(win)
    Rectangle(rmXY, Point(rmXY.getX() + pK / 3, rmXY.getY() - pK / 3)).draw(win)
    Rectangle(rdXY, Point(rdXY.getX() + pK / 3, rdXY.getY() - pK / 3)).draw(win)

    # Сливы для воды слева\справа
    Circle(Point(lmXY.getX() + cirRad / 4, lmXY.getY() - cirRad / 4), rad).draw(win)
    Circle(Point(rmXY.getX() - cirRad / 4, rmXY.getY() - cirRad / 4), rad).draw(win)

    # Сливы для воды снизу - слева\справа
    Circle(Point(ldXY.getX() + cirRad, ldXY.getY() - cirRad / 4), rad).draw(win)
    Circle(Point(rdXY.getX() - cirRad, rdXY.getY() - cirRad / 4), rad).draw(win)

    # Место для грязных водных шаров
    Rectangle(mdXY, Point(mdXY.getX() + cirRad, mdXY.getY() - hsliv)).draw(win)
    Rectangle(mdXY, Point(mdXY.getX() - cirRad, mdXY.getY() - hsliv)).draw(win)

    # Место "цветка"
    Rectangle(mdXY, Point(mdXY.getX() - PlaceforBall, mdXY.getY() + PlaceforBall)).draw(win)
    Rectangle(mdXY, Point(mdXY.getX() + PlaceforBall, mdXY.getY() + PlaceforBall)).draw(win)

    # Зона пчелки
    StartPointForBeeLeftXY = Point(ldXY.getX(), ldXY.getY() + PlaceforBall / 2)
    StartPointForBeeRightXY = Point(rdXY.getX(), rdXY.getY() + PlaceforBall / 2)

    Line(ldXY, StartPointForBeeLeftXY).draw(win)
    Line(rdXY, StartPointForBeeRightXY).draw(win)

    Line(StartPointForBeeLeftXY, Point(mdXY.getX() - PlaceforBall, mdXY.getY() + PlaceforBall / 2)).draw(win)
    Line(StartPointForBeeRightXY, Point(mdXY.getX() + PlaceforBall, mdXY.getY() + PlaceforBall / 2)).draw(win)

    mlhmhXY = Point(mhXY.getX() - dis, mhXY.getY())
    mmhrlXY = Point(mhXY.getX() + dis, mhXY.getY())
    Rectangle(mlhmhXY, Point(mmhrlXY.getX(), mmhrlXY.getY() - 20 * k)).draw(win)

    # Линии езды

    Line(Point(lhXY.getX(), lhXY.getY() + pK), Point(rhXY.getX(), rhXY.getY() + pK)).draw(win)

    Line(Point(ldXY.getX() + cirRad, rdXY.getY() - pK), Point(ldXY.getX() + cirRad, lhXY.getY() + pK)).draw(win)
    Line(Point(rdXY.getX() - cirRad, rdXY.getY() - pK), Point(rdXY.getX() - cirRad, rhXY.getY() + pK)).draw(win)

    Line(Point(lmXY.getX() + cirRad / 2, lmXY.getY() - cirRad / 4),
         Point(mmXY.getX() - cirRad, lmXY.getY() - cirRad / 4)).draw(win)

    Line(Point(rmXY.getX() - 0.5 * cirRad, rmXY.getY() - cirRad / 4),
         Point(rmXY.getX() - 1.5 * cirRad, rmXY.getY() - cirRad / 4)).draw(win)

    # полукруги
    rad1 = 35 * k
    Circle(Point(ldXY.getX() + cirRad, rdXY.getY()), rad1).draw(win)
    Circle(Point(rdXY.getX() - cirRad, rdXY.getY()), rad1).draw(win)


COLORS = ['blue', 'yellow', 'black', 'green', 'orange']

"""Function create left part of map"""
def LeftPart(win, lhXY, mhXY, rhXY, lmXY, mmXY, rmXY, ldXY, mdXY, rdXY, k):
    board = [lhXY, mhXY, rhXY, rmXY, rdXY, mdXY, ldXY, lmXY]
    allSM = []  # All Static Models (LeftPart)
    buf = []
    for i in range(len(board)):
        buf += [[Line(board[i], board[(i + 1) % len(board)]).draw(win)]]

    allSM += [buf]
    pK = 36 * k
    dis = 50 * k
    cirRad = 60 * k
    rad = 5 * k
    hsliv = 25 * k
    PlaceforBall = 23 * k
    # Баки для воды
    allSM += [[Rectangle(lhXY, Point(lhXY.getX() + pK, lhXY.getY() - pK)).draw(win)]]
    # Cтратовые зоны
    allSM += [[Rectangle(lhXY, Point(lhXY.getX() + pK, lhXY.getY() + 2 * pK)).draw(win)]]

    # Зоны для маячков слева
    allSM += [[Rectangle(lhXY, Point(lhXY.getX() - pK / 3, lhXY.getY() + pK / 3)).draw(win),
               Rectangle(lmXY, Point(lmXY.getX() - pK / 3, lmXY.getY() - pK / 3)).draw(win),
               Rectangle(ldXY, Point(ldXY.getX() - pK / 3, ldXY.getY() - pK / 3)).draw(win)]]

    # Сливы для воды слева\справа
    allSM += [[Circle(Point(lmXY.getX() + cirRad / 4, lmXY.getY() - cirRad / 4), rad).draw(win)]]

    # Сливы для воды снизу - слева\справа
    allSM += [[Circle(Point(ldXY.getX() + cirRad, ldXY.getY() - cirRad / 4), rad).draw(win)]]

    # Место для грязных водных шаров
    allSM += [[Rectangle(mdXY, Point(mdXY.getX() + cirRad, mdXY.getY() - hsliv)).draw(win)]]

    # Место "цветка"
    allSM += [[Rectangle(mdXY, Point(mdXY.getX() - PlaceforBall, mdXY.getY() + PlaceforBall)).draw(win)]]

    # Зона пчелки
    StartPointForBeeLeftXY = Point(ldXY.getX(), ldXY.getY() + PlaceforBall / 2)
    allSM += [[Line(ldXY, StartPointForBeeLeftXY).draw(win)]]

    allSM += [
        [Line(StartPointForBeeLeftXY, Point(mdXY.getX() - PlaceforBall, mdXY.getY() + PlaceforBall / 2)).draw(win)]]

    mlhmhXY = Point(mhXY.getX() - dis, mhXY.getY())
    mmhrlXY = Point(mhXY.getX() + dis, mhXY.getY())
    allSM += [[Rectangle(mlhmhXY, Point(mmhrlXY.getX(), mmhrlXY.getY() - 20 * k)).draw(win)]]

    # Линии езды

    allSM += [[Line(Point(lhXY.getX(), lhXY.getY() + pK), Point(mhXY.getX(), mhXY.getY() + pK)).draw(win)]]

    allSM += [[
        Line(Point(ldXY.getX() + cirRad, rdXY.getY() - pK), Point(ldXY.getX() + cirRad, lhXY.getY() + pK)).draw(win)]]

    allSM += [[Line(Point(lmXY.getX() + cirRad / 2, lmXY.getY() - cirRad / 4),
                    Point(mmXY.getX() - cirRad, lmXY.getY() - cirRad / 4)).draw(win)]]

    # полукруги
    rad1 = 35 * k

    allSM += [[Circle(Point(ldXY.getX() + cirRad, rdXY.getY()), rad1).draw(win)]]
    return allSM

"""Function reflects all static element regarding x
    :param win -- Graphic Window
    :param x -- asic
    :param allSM -- all Static Models
    :return 
"""
def Mirrow(win, x, allSM):
    p = Point(1, 1)
    Rect = Rectangle(p, p)
    Circ = Circle(p, 1)
    line = Line(p, p)
    RP = []
    LP = allSM[:]
    for objL in allSM:
        buf = []
        for obj in objL:
            if type(Rect) == type(obj):
                x1 = obj.getP1().getX()
                y1 = obj.getP1().getY()
                x2 = obj.getP2().getX()
                y2 = obj.getP2().getY()
                buf += [Rectangle(Point(x + (x - x1), y1), Point(x + (x - x2), y2)).draw(win)]
            elif type(Circ) == type(obj):
                x1 = obj.getCenter().getX()
                y1 = obj.getCenter().getY()
                r = obj.getRadius()
                buf += [Circle(Point(x + (x - x1), y1), r).draw(win)]
            elif type(line) == type(obj):
                x1 = obj.getP1().getX()
                y1 = obj.getP1().getY()
                x2 = obj.getP2().getX()
                y2 = obj.getP2().getY()
                buf += [Line(Point(x + (x - x1), y1), Point(x + (x - x2), y2)).draw(win)]
        RP += [buf]
    return LP, RP

"""Function for creating building kubs
 :return [], where every element is Rectanle
 """
def sklad(win, center, k):
    a = 6 * k
    x = center.getX()
    y = center.getY()
    rc = Rectangle(center, Point(x + a, y + a)).draw(win)
    ru = Rectangle(center, Point(x + a, y - a)).draw(win)
    rr = Rectangle(Point(x + a, y), Point(x + 2 * a, y + a)).draw(win)
    rd = Rectangle(Point(x, y + a), Point(x + a, y + 2 * a)).draw(win)
    rl = Rectangle(center, Point(x - a, y + a)).draw(win)

    skl = [rc, ru, rr, rd, rl]
    return skl


"""
    The function for drawing kubs for bulding
    :param objs -- [] , where every element is Rectangle
    :return [] 
"""


def drawingSklad(objs):
    for i in range(len(COLORS)):
        rand = random.randint(0, len(COLORS) - 1)
        COLORS[i], COLORS[rand] = COLORS[rand], COLORS[i]
    for j, k in enumerate(objs):
        k.setFill(COLORS[j])
    return objs


def main():
    win = GraphWin("My model", 4000, 4000)
    lhXY = Point(200, 200)
    k = 2
    h = 100 * k
    w = 150 * k
    mhXY = Point(lhXY.getX() + w, lhXY.getY())
    rhXY = Point(mhXY.getX() + w, mhXY.getY())

    lmXY = Point(lhXY.getX(), lhXY.getY() + h)
    mmXY = Point(lmXY.getX() + w, lmXY.getY())
    rmXY = Point(mmXY.getX() + w, mmXY.getY())

    ldXY = Point(lmXY.getX(), lmXY.getY() + h)
    mdXY = Point(ldXY.getX() + w, ldXY.getY())
    rdXY = Point(mdXY.getX() + w, mdXY.getY())

    # staticModels(win, lhXY, mhXY, rhXY, lmXY, mmXY, rmXY, ldXY, mdXY, rdXY, k)
    allModels = LeftPart(win, lhXY, mhXY, rhXY, lmXY, mmXY, rmXY, ldXY, mdXY, rdXY, k)
    Mirrow(win, mmXY.getX(), allModels)
    BRsize = 30 * k
    MRsize = 20 * k
    BigRobot = Rectangle(lhXY, Point(lhXY.getX() + BRsize, lhXY.getY() + BRsize)).draw(win)
    BigRobot.setFill("red")
    MedRobot = Rectangle(Point(lhXY.getX(), lhXY.getY() + 36 * k),
                         Point(lhXY.getX() + MRsize, lhXY.getY() + 36 * k + MRsize)).draw(win)
    MedRobot.setFill(("blue"))
    cirRad = 60 * k
    centerS1 = Point(lmXY.getX() + cirRad / 2, lmXY.getY() + cirRad / 4.5)
    centerS2 = Point(mmXY.getX() - 1.15 * cirRad, lmXY.getY() - cirRad / 1.5)
    centerS3 = Point(mmXY.getX() - 0.9 * cirRad, ldXY.getY() - cirRad / 1.5)
    S1 = sklad(win, centerS1, k)
    S2 = sklad(win, centerS2, k)
    S3 = sklad(win, centerS3, k)
    LS, RS = Mirrow(win, mmXY.getX(), [S1, S2, S3])
    for i in LS:
        drawingSklad(i)
    for i in RS:
        drawingSklad(i)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


if __name__ == '__main__':
    main()
