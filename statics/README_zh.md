<div style="width: 100%;">
    <img src="../statics/title.svg" style="width: 100%;">
</div>

受[gpt-researcher](https://github.com/assafelovic/gpt-researcher)启发，本项目提供了一种利用第三方API而不是官方API生成研究报告的替代方法。要访问此第三方API，请参阅[chimeragpt](https://chimeragpt.adventblocks.cc/)或者[GPT-API-free](https://github.com/chatanywhere/GPT_API_free)。一旦获得API密钥，您就可以使用它来访问chimeragpt API。因此，在运行项目之前，请确保您设置了环境变量`OPENAI_API_KEY`和`OPENAI_API_BASE`。

```shell
$ export OPENAI_API_KEY = your_api_key
$ export OPENAI_API_BASE = your_api_base
```

或者您可以在`.env`文件中设置api密钥和基础。

## 安装

1. 克隆存储库

    ```shell
    $ git clone git@github.com:paradoxtown/ai_research_assistant.git
    $ cd ai_research_assistant
    ```

2. 安装依赖项

    ```shell
    $ pip install -r requirements.txt
    ```

3. 导出环境变量

    ```shell
    $ export OPENAI_API_KEY = your_api_key
    $ export OPENAI_API_BASE = your_api_base
    ```
    或修改`.env`文件。

4. 运行项目

    ```shell
    $ python app.py
    ```