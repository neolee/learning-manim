from manimlib import * # type: ignore


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()


class Anagram(Scene):
    def construct(self):
        # source = Text("two eleven", font="Consolas", font_size=90)
        # target = Text("one twelve", font="Consolas", font_size=90)
        source = Text("two eleven", height=1)
        target = Text("one twelve", height=1)
        saved_source = source.copy()

        self.play(Write(source))
        self.wait()
        # kw = dict(run_time=3, path_arc=PI/2)
        kw = {"run_time": 3, "path_arc": PI/2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, saved_source, **kw))
        self.wait()
