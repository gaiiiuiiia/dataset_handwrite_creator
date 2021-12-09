import tkinter


class DrawingCanvas:
    def __init__(
            self,
            window: tkinter.Tk,
            width: int,
            height: int,
            bg_color: str,
            brush_color: str,
            brush_size: int) -> None:
        self.__window = window
        self.__width = width
        self.__height = height
        self.__bg_color = bg_color
        self.__brush_color = brush_color
        self.__brush_size = brush_size

        self.__canvas = tkinter.Canvas(
            self.__window,
            width=self.__width,
            height=self.__height,
            bg=self.__bg_color
        )

    def get_canvas(self) -> tkinter.Canvas:
        return self.__canvas

    def reset_canvas(self) -> None:
        self.__canvas.create_rectangle(0, 0, self.__width, self.__height, fill=self.__bg_color)

    def __draw(self, x: int, y: int) -> None:
        self.__canvas.create_oval(
            x - self.__brush_size,
            y - self.__brush_size,
            x + self.__brush_size,
            y + self.__brush_size,
            fill=self.__brush_color,
            outline=self.__brush_color
        )

    def press(self, event: tkinter.Event) -> None:
        self.__draw(event.x, event.y)

    def release(self, event: tkinter.Event) -> None:
        # self.draw(event.x, event.y)
        pass

    def motion(self, event: tkinter.Event) -> None:
        self.__draw(event.x, event.y)

    def get_canvas_rectangle_coordinates(self) -> tuple:
        """
        Вернуть прямоугольную область холста
        с координатами относительно самого приложения
        """

        x1 = self.__canvas.winfo_rootx()  # + self.__canvas.winfo_x()
        y1 = self.__canvas.winfo_rooty()  # + self.__canvas.winfo_y()
        x2 = x1 + self.__canvas.winfo_width()
        y2 = y1 + self.__canvas.winfo_height()

        return x1, y1, x2, y2
