<style>
    .top-bar {
        padding-bottom: 5px;
        background-color: transparent;
        border-bottom: #dfe4ea 1px solid;
    }
    
    .top-bar .in-bar-title {
        background-image: linear-gradient(45deg, #8B5FBF, #D6C6E1, #ffffff);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: Gelion, "Open Sans", Helvetica, "Helvetica Neue", Arial;
        font-size: 2rem;
        font-weight: bold;
        text-align: left;
        display: block;
    }

    .top-bar .in-bar-subtitle {
        font-family: 'Crimson Pro';
        color: #878787;
        font-size: 1.4rem;
        margin-top: -5px;
        display: block;
    }
</style>
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@200..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css">
</head>
<div class="top-bar">
    <div class="top-bar-left">
        <span class="in-bar-title">
            AI Research Assistant
            <a href="https://github.com/paradoxtown/ai_research_assistant">
                <i class="fab fa-github" style="font-size:22px;"></i>
            </a>
        </span>
        <span class="in-bar-subtitle">Your personal free GPT researcher</span>
    </div>
</div>


Inspired by [gpt-researcher](https://github.com/assafelovic/gpt-researcher). 

This project offers an alternative approach to generating research reports by utilizing a third-party API instead of the official one. For access to this third-party API, please refer to [chimeragpt](https://chimeragpt.adventblocks.cc/). Once you obtain the API key, you can utilize it to access the chimeragpt API. Therefore, before running the project, kindly ensure that you set the environment variables `OPENAI_API_KEY` and `OPENAI_API_BASE`.

```
export OPENAI_API_KEY = your_api_key
export OPENAI_API_BASE = your_api_base
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
    $ python aira.py
    ```

## TODO

- [ ] Summarize the search results locally
- [ ] Literature review
- [x] Third-party API
- [x] Prettify report
- [x] Warning when agent and type are not selected
- [x] Add medical agent and social agent
- [ ] Add option for users to customize the number of words and temperature