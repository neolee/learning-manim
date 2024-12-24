from manimlib import * # type: ignore

class AnimatedTriangleInCoordinateSystem(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-5, 5, 1),  # x range and step
            y_range=(-5, 5, 1),  # y range and step
            axis_config={"include_numbers": False}  # hide on-axis tips
        )
        axes.add_coordinate_labels()  # add labels

        self.play(ShowCreation(axes))

        triangle = Polygon(
            axes.c2p(0, 1, 0),
            axes.c2p(-1, -1, 0),  # coordinates to screen position
            axes.c2p(1, -1, 0),
            color=BLUE,
            fill_opacity=0.5
        )

        self.play(FadeIn(triangle))

        # animating: `triangle.animate.scale` stretch the object on both dimensions
        self.play(triangle.animate.scale(2), run_time=2)
        self.play(triangle.animate.scale(0.5), run_time=2)

        # animating: `ApplyMethod(triangle.stretch, scale, dim)` let us assign a `dim`
        self.play(ApplyMethod(triangle.stretch, 2, 0), run_time=2)
        self.play(ApplyMethod(triangle.stretch, 2, 1), run_time=2)
        self.play(ApplyMethod(triangle.stretch, 0.5, 1), run_time=2)
        self.play(ApplyMethod(triangle.stretch, 0.5, 0), run_time=2)

        self.wait()
