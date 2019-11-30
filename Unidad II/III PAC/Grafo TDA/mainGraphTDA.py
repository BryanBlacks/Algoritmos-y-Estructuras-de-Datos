#-*- coding: utf8 -*-
from GraphTDA import
g = graph()
g.add("Hola Mundo")
g.add(1)
g.edge(
    vertexA = "Hola Mundo",
    vertexB = 1,
    weight = g.calculateWeight(
        bumbp=1, 
        crossWalk=5, 
        delayByTimeOfDay=0.4, 
        delayByDayOfWeek=0.3
    )
)

print(g)