---
title: AI-Research-Assistant
app_file: app.py
sdk: gradio
sdk_version: 3.38.0
---
<div style="width: 100%;">
    <img src="./statics/title.svg" style="width: 100%;">
    <div align="right">
        <a href="./README.md">English</a> |
        <a href="./statics/README_zh.md">中文</a>
    </div>
</div>

Inspired by [gpt-researcher](https://github.com/assafelovic/gpt-researcher). This project offers an alternative approach to generating research reports by utilizing a third-party API instead of the official one. For access to this third-party API, please refer to [chimeragpt](https://chimeragpt.adventblocks.cc/) or [GPT-API-free](https://github.com/chatanywhere/GPT_API_free). Before running the project, kindly ensure that you set the environment variables `OPENAI_API_KEY` and `OPENAI_API_BASE`.

```shell
$ export OPENAI_API_KEY = your_api_key
$ export OPENAI_API_BASE = your_api_base
```

or you can set the api key and base in `.env` file.


## Installation

1. Clone the repository
    
    ```shell
    $ git clone git@github.com:paradoxtown/ai_research_assistant.git
    $ cd ai_research_assistant
    ```

2. Install the dependencies

    ```shell
    $ pip install -r requirements.txt
    ```

3. Export evnironment variables

    ```shell
    $ export OPENAI_API_KEY = your_api_key
    $ export OPENAI_API_BASE = your_api_base
    ```
    or modify the `.env` file.

4. Run the project

    ```shell
    $ python app.py
    ```

## TODO

- [x] Switch Google Search to DuckDuckGo
- [ ] Literature review
- [x] Third-party API
- [ ] Prettify report
- [x] Add medical agent and social agent
- [ ] Add option for users to customize the number of words and temperature