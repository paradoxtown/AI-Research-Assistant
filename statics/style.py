css = """
    .top-bar {
        padding-bottom: 10px;
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
    
    .main {
        max-width: 800px;
        align-self: center;
    }
    
    .output {
        padding: 10px;
        min-height: 200px;
        border: #c0c0c0 1px solid;
        border-radius: 5px;
        margin-bottom: 10px;
    }
"""

top_bar = """
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@200..900&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css">
    </head>
    <body>
        <div class="top-bar">
            <div class="top-bar-left">
                <span class="in-bar-title">
                    AI Research Assistant
                    <a href="https://github.com/paradoxtown/AI-Research-Assistant">
                        <i class="fab fa-github" style="font-size:23px;"></i>
                    </a>
                </span>
                <span class="in-bar-subtitle">Your personal free GPT researcher</span>
            </div>
        </div>
    <body>
"""

research_report_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")># Research Report</span>
"""

english_polishing_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")># Polished Result</span>
"""

history_result_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")># History Result</span>
"""