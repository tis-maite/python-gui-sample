def requirements_definition_from_text(text: str) -> str:
    """テキストをインプットに、要求定義を生成する"""
    return (
        text
        + """サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
        """
    )


def requirements_definition_from_file(file) -> str:
    """AIにテキスト入力を問い合わせる"""
    input = file.read()
    return (
        input
        + """サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。サンプルテキスト。
        """
    )


def search(query: str) -> str:
    """AIにテキスト入力を問い合わせる"""
    return (
        query
        + """
    <div>
      <h1 style="color: blue;">Sample HTL</h1>
    </div>
    <div>
      <ul>
        <li>リンク１</li>
        <li>リンク２：<a alt="外部リンク(Google)" href="https://www.google.com/">Google</a></li>
        <li>リンク３</li>
      </ul>
    </div>
    <div>
      <h1 style="color: blue;">Sample HTL</h1>
    </div>
    <div>
      <ul>
        <li>リンク１</li>
        <li>リンク２：<a alt="外部リンク(Google)" href="https://www.google.com/">Google</a></li>
        <li>リンク３</li>
      </ul>
    </div>
    <div>
      <h1 style="color: blue;">Sample HTL</h1>
    </div>
    <div>
      <ul>
        <li>リンク１</li>
        <li>リンク２：<a alt="外部リンク(Google)" href="https://www.google.com/">Google</a></li>
        <li>リンク３</li>
      </ul>
    </div>
    <div>
      <h1 style="color: blue;">Sample HTL</h1>
    </div>
    <div>
      <ul>
        <li>リンク１</li>
        <li>リンク２：<a alt="外部リンク(Google)" href="https://www.google.com/">Google</a></li>
        <li>リンク３</li>
      </ul>
    </div>
    """
    )
