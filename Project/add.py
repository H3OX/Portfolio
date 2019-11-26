from Project.models import Project

p1 = Project(
    title='Weather App',
    description='A simple Weather App based on Dark Sky API',
    image='img/weather.png',
    technology='Node.js'
)

p1.save()

p2 = Project(
    title='Calculator App',
    description='A Calculator for Android OS',
    image='img/calc.png',
    technology='Kotlin/Java'
)

p2.save()
