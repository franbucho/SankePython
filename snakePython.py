import turtle
import time
import random

# Configuración del juego
delay = 0.1
score = 0
high_score = 0

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Culebrita")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactivar la actualización automática de la pantalla

# Cabeza de la culebra
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Cuerpo de la culebra
segments = []

# Funciones
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Teclado
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Bucle principal del juego
while True:
    wn.update()

    # Verificar colisiones con los bordes
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Ocultar los segmentos del cuerpo
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpiar la lista de segmentos
        segments.clear()

        # Restablecer marcador
        score = 0

        # Actualizar marcador
        delay = 0.1
        wn.update()

    # Verificar colisión con la comida
    if head.distance(food) < 20:
        # Mover la comida a una ubicación aleatoria
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Agregar un segmento al cuerpo
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Reducir el tiempo de espera
        delay -= 0.001

        # Aumentar el marcador
        score += 10

        if score > high_score:
            high_score = score

        # Actualizar el marcador en la pantalla
        wn.title("Culebrita - Puntuación: {}  Mejor Puntuación: {}".format(score, high_score))

    # Mover los segmentos en orden inverso
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Mover el primer segmento a la posición de la cabeza
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Mover la cabeza de la culebra
    move()

    # Verificar colisiones con el cuerpo
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Ocultar los segmentos del cuerpo
            for seg in segments:
                seg.goto(1000, 1000)

            # Limpiar la lista de segmentos
            segments.clear()

            # Restablecer marcador
            score = 0

            # Actualizar marcador
            delay = 0.1
            wn.update()
#timeSleep
    # Pausar el juego
    time.sleep(delay)
