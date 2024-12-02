import customtkinter
from tkhtmlview import HTMLLabel


class View(customtkinter.CTkFrame):
    """要件定義をAIで生成する画面。テキストで入力するタイプ"""

    def __init__(self, master, ask_ai_fn, **kw):
        super().__init__(master, **kw)

        self.ask_ai_fn = ask_ai_fn

        self.label = customtkinter.CTkLabel(
            master=master,
            height=5,
            text="作成したいアプリケーションを記述してください",
            font=("Arial", 12),
        )
        self.label.grid(row=0, column=0, pady=(0, 10), sticky="we")

        self.textbox = customtkinter.CTkTextbox(
            master=master,
            height=100,
            corner_radius=10,
            border_width=1,
            border_spacing=1,
        )
        self.textbox.grid(row=1, column=0, pady=(0, 10), sticky="we")

        self.execButton = customtkinter.CTkButton(
            master=master,
            text="実行",
            corner_radius=10,
            command=self.on_exec_button_click,
        )
        self.execButton.grid(row=2, column=0, pady=(0, 20), sticky="we")

        self.answer = ScrollableAnswer(master=master, height=450, fg_color="black")
        self.answer.grid(row=3, column=0, padx=0, pady=(0, 10), sticky="we")

    def ask_ai(self, input: str) -> str:
        return self.ask_ai_fn(input)

    def on_exec_button_click(self):
        input = self.textbox.get("1.0", "end")
        answer = self.ask_ai(input)
        self.answer.label.set_html(answer)
        self.answer.label.fit_height()


class ScrollableAnswer(customtkinter.CTkScrollableFrame):
    """スクロール可能なAIの回答表示欄

    回答によって長さが変わるため、スクロール可能なフレームに表示する
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = HTMLLabel(
            master=self,
            html="<h2>hoge</h2>",
        )
        self.label.grid(row=0, column=0, padx=0, pady=0, sticky="wens")
        self.label.fit_height()
