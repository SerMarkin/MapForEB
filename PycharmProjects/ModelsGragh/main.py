import turtle
from graphics import *
import math


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
    Rectangle(lmXY, Point(lmXY.getX() - pK / 3, lmXY.getY() + pK / 3)).draw(win)
    Rectangle(ldXY, Point(ldXY.getX() - pK / 3, ldXY.getY() - pK / 3)).draw(win)

    # Зоны для маячков справа
    Rectangle(rhXY, Point(rhXY.getX() + pK / 3, rhXY.getY() + pK / 3)).draw(win)
    Rectangle(rmXY, Point(rmXY.getX() + pK / 3, rmXY.getY() + pK / 3)).draw(win)
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

    # полукруги
    rad1 = 35 * k
    Circle(Point(ldXY.getX() + cirRad, rdXY.getY()), rad1).draw(win)
    Circle(Point(rdXY.getX() - cirRad, rdXY.getY()), rad1).draw(win)


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

    staticModels(win, lhXY, mhXY, rhXY, lmXY, mmXY, rmXY, ldXY, mdXY, rdXY, k)

    BRsize = 30 * k
    MRsize = 20 * k
    BigRobot = Rectangle(lhXY, Point(lhXY.getX() + BRsize, lhXY.getY() + BRsize)).draw(win)
    BigRobot.setFill("red")
    MedRobot = Rectangle(Point(lhXY.getX(), lhXY.getY() + 36 * k),
                         Point(lhXY.getX() + MRsize, lhXY.getY() + 36 * k + MRsize)).draw(win)
    MedRobot.setFill(("blue"))
    # BigRobot.move(0,200)

    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


if __name__ == '__main__':
    main()
