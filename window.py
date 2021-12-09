import tkinter
import tkinter.ttk

import config
import translation_ru

import drawing_canvas
import image_manager


class Window:
    def __init__(self, img_manager: image_manager.ImageManager) -> None:
        self.img_manager = img_manager

        self.window = tkinter.Tk()
        self.window.title(config.WIN_TITLE)
        self.window.geometry(config.WIN_SIZE_TK)

        self.radio_value = tkinter.IntVar(self.window, 0)
        self.selected_image_name = config.RADIO_BUTTON_OPTIONS[self.radio_value.get()]

        self.__drawing_canvas = drawing_canvas.DrawingCanvas(
            self.window,
            config.CANVAS_WIDTH,
            config.CANVAS_HEIGHT,
            config.CANVAS_BG_COLOR,
            config.CANVAS_BRUSH_COLOR,
            config.CANVAS_BRUSH_SIZE
        )

        self.__drawing_canvas.get_canvas().bind("<Button-1>", self.__drawing_canvas.press)
        self.__drawing_canvas.get_canvas().bind("<Button1-ButtonRelease-1>", self.__drawing_canvas.release)
        self.__drawing_canvas.get_canvas().bind("<Button1-Motion>", self.__drawing_canvas.motion)

        self.save_button = tkinter.ttk.Button(
            text=translation_ru.BTN_SAVE,
            command=self.__save_image
        )

        self.reset_button = tkinter.ttk.Button(
            text=translation_ru.BTN_RESET,
            command=self.__reset_image
        )

        self.window.bind('<KeyPress>', lambda event: self.__save_image() if event.keycode == 36 else 0)

        self.radio_buttons = self.__init_radio_buttons()

        self.__drawing_canvas.get_canvas().pack()
        self.save_button.pack()
        self.reset_button.pack()
        [radio.pack() for radio in self.radio_buttons]
        self.window.mainloop()

    def __init_radio_buttons(self) -> list:
        radios = []

        for index, name in config.RADIO_BUTTON_OPTIONS.items():
            radio = tkinter.ttk.Radiobutton(
                self.window,
                text=name,
                variable=self.radio_value,
                value=index,
                command=self.__radio_callback
            )
            radios.append(radio)

        return radios

    def __radio_callback(self) -> None:
        name = config.RADIO_BUTTON_OPTIONS[self.radio_value.get()]
        self.selected_image_name = name

    def __save_image(self, event: tkinter.Event = None) -> None:
        self.img_manager.save_image_from_canvas(self.__drawing_canvas, self.selected_image_name)
        self.__reset_image()

    def __reset_image(self) -> None:
        self.__drawing_canvas.reset_canvas()
