import math


def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def mirrored(ball, startX, startY, m, n):
    x, y = ball
    if not (x == startX and y < startY):
        yield x, -y
    if not (x == startX and y > startY):
        yield x, y + 2 * (n-y)
    if not (x < startX and y == startY):
        yield -x, y
    if not (x > startX and y == startY):
        yield x + 2 * (m-x), y


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        min_distance = math.inf
        direct_distance = distance(startX, startY, ball[0], ball[1])
        for endX, endY in mirrored(ball, startX, startY, m, n):
            if (new_distance := distance(startX, startY, endX, endY)) == direct_distance:
                continue
            min_distance = min(min_distance, new_distance)
        answer.append(min_distance)

    return answer
