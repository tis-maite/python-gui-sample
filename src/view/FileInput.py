import customtkinter


class View(customtkinter.CTkFrame):
    """要件定義をAIで生成する画面。ファイルで入力するタイプ"""

    def __init__(self, master, ask_ai_fn, **kw):
        super().__init__(master, **kw)

        self.ask_ai_fn = ask_ai_fn

        self.label = customtkinter.CTkLabel(
            master=master,
            height=5,
            text="作成したいアプリケーションについてマークダウンファイルを設定してください",
            font=("Arial", 12),
        )
        self.label.grid(row=0, column=0, pady=(0, 10), sticky="we")

        self.execButton = customtkinter.CTkButton(
            master=master,
            text="ファイルを選択",
            corner_radius=10,
            command=self.on_exec_button_click,
        )
        self.execButton.grid(row=1, column=0, pady=(0, 20), sticky="we")

        self.answer = ScrollableAnswer(master=master, height=400, fg_color="black")
        self.answer.grid(row=2, column=0, padx=0, pady=10, sticky="we")

    def on_exec_button_click(self):
        filename = customtkinter.filedialog.askopenfilename(
            parent=self,
            title="ファイルを選択",
            multiple=False,
            filetypes=[("マークダウンファイル", "*.md"), ("テキストファイル", "*.txt")],
        )

        if filename:
            # ファイルの文字コードを選択可能にするなら追加実装が必要。ここではutf-8固定
            with open(filename, encoding="utf-8") as f:
                answer = self.ask_ai(f)
                self.answer.label.configure(text=answer)
        else:
            print("ファイルが選択されていません")

    def ask_ai(self, input: str) -> str:
        return self.ask_ai_fn(input)


class ScrollableAnswer(customtkinter.CTkScrollableFrame):
    """スクロール可能なAIの回答表示欄

    回答によって長さが変わるため、スクロール可能なフレームに表示する
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(
            master=self,
            text="",  # ここにAIの結果を表示する
            justify="left",
            anchor="w",
            wraplength=535,
            corner_radius=10,
            fg_color="black",
            font=("Arial", 12),
        )
        self.label.grid(row=0, column=0, padx=0, pady=10, sticky="we")
