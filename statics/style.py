css = """
    .top-bar {
        padding-bottom: 10px;
        background-color: transparent;
        border-bottom: #E9E4ED 1px solid;
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
        min-width: min(100%, 800px);
        align-self: center;
    }
    
    .output {
        padding: 10px;
        min-height: 300px;
        border: 1.5px solid #AC7DD280;
        border-radius: 10px;
        margin-bottom: 10px;
        transition: opacity .1s ease-in-out;
        background: var(--block-background-fill);
    }
    
    #history {
        padding: 10px !important;
        border: 1.5px dashed #AC7DD2 !important;
        border-radius: 10px !important;
    }
    
    #primary-btn {
        border: 1.5px solid #AC7DD2;
        font-size: 20px;
    }
    
    summary {
        font-size: 14px;
        font-weight: bold;
    }
    
    #history_box {
        border-bottom: 1.5px dashed #9A73B5;
        padding: 10px;
    }
    
    .tab-nav {
        border-bottom: 1.5px solid #9A73B5 !important;
    }
    
    .selected {
        border: 1.5px solid #9A73B5 !important;
        border-bottom: none !important;
    }
    
    .tabitem {
        border: 1.5px solid #9A73B5 !important;
        border-top: none !important;
    }
"""

# #809A73B5

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
                        <i class="fab fa-github" style="font-size:25px;"></i>
                    </a>
                </span>
                <span class="in-bar-subtitle">Your personal free GPT researcher</span>
            </div>
        </div>
    <body>
"""

report_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")># Report</span>
"""

english_polishing_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")># Polished Result</span>
"""

history_result_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")># History Result</span>
"""

literature_review_html = """
    <span data-testid="block-info" class="svelte-1gfkn6j custom_label")>under construction...</span>
"""