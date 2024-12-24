from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class Anagram(Scene):
    def construct(self):
        source = Text("two eleven", font="Consolas", font_size=90)
        target = Text("one twelve", font="Consolas", font_size=90)

        self.play(Write(source))
        self.wait(0.5)
        kw = {"run_time": 2, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait(0.5)
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait(0.5)
