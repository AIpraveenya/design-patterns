class Renderer:
    def render_circle(self, radius):
        raise NotImplementedError

    def render_square(self, side):
        raise NotImplementedError


# Step 2: Create ConcreteImplementors

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using vector graphics.")

    def render_square(self, side):
        print(f"Drawing a square with side {side} using vector graphics.")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using raster graphics.")

    def render_square(self, side):
        print(f"Drawing a square with side {side} using raster graphics.")


# Step 3: Define the Abstraction

class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError

    def resize(self, factor):
        raise NotImplementedError


# Step 4: Create RefinedAbstractions

class Circle(Shape):
    def __init__(self, radius, renderer: Renderer):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Square(Shape):
    def __init__(self, side, renderer: Renderer):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor


# Client code to demonstrate the usage
def main():
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle = Circle(5, vector_renderer)
    square = Square(3, raster_renderer)

    print("Initial shapes:")
    circle.draw()  # Output: Drawing a circle with radius 5 using vector graphics.
    square.draw()  # Output: Drawing a square with side 3 using raster graphics.

    # Resize the shapes
    circle.resize(2)
    square.resize(1.5)

    print("\nAfter resizing:")
    circle.draw()  # Output: Drawing a circle with radius 10 using vector graphics.
    square.draw()  # Output: Drawing a square with side 4.5 using raster graphics.


if __name__ == "__main__":
    main()