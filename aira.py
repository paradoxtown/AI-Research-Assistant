import gradio as gr

from config import check_openai_api_key
from agent.research_agent import ResearchAgent
from style import css, top_bar, research_report_html

# theme = gr.themes.Soft(
#     chue=gr.themes.Color(c100="#e0e7ff", c200="#c7d2fe", c300="#a5b4fc", c400="#818cf8", c50="#eef2ff", c500="#6366f1", c600="#61398f", c700="#4338ca", c800="#3730a3", c900="#312e81", c950="#61398f"),
#     font_mono=[gr.themes.GoogleFont('Fira Code'), 'ui-monospace', 'Consolas', 'monospace'],
# ).set(
#     embed_radius='*radius_md'
# )

theme = gr.themes.Soft(
    primary_hue=gr.themes.Color(c100="#e0e7ff", c200="#c7d2fe", c300="#a5b4fc", c400="#818cf8", c50="#eef2ff", c500="#6366f1", c600="#5e5aaa", c700="#4338ca", c800="#3730a3", c900="#312e81", c950="#2b2c5e"),
)

check_openai_api_key()

assistant = None
async def search(task, agent):
    global assistant
    assistant = ResearchAgent(task, agent)
    research_summary = await assistant.search_online()
    return research_summary

def run_agent(report_type):
    yield from assistant.write_report(report_type)
    
def test_run_agent(report_type):
    return "# Heading\n\nThis is a *test* report"


with gr.Blocks(theme=theme, 
               title="AI Research Assistant",
               css=css) as demo:
    gr.HTML(top_bar)
    with gr.Tab(label="Report"):
        with gr.Column():
            gr.HTML(research_report_html)
            research_report = gr.Markdown("&nbsp;&nbsp;**Research report will appear here...**")
            agent_output = gr.Textbox(label="# Agent Output", 
                                      lines=10, 
                                      placeholder="Agent output will appear here", 
                                      interactive=False)
            with gr.Row():
                agent_type = gr.Dropdown(label="# Agent Type", 
                                         value="Default Agent",
                                         interactive=True,
                                         allow_custom_value=False,
                                         choices=["Default Agent", 
                                                 "Business Analyst Agent",
                                                 "Finance Agent",
                                                 "Travel Agent",
                                                 "Academic Research Agent",
                                                 "Computer Security Analyst Agent",
                                                 "Clinical Medicine Agent",
                                                 "Basic Medicine Agent",
                                                 "Social Science Research Agent"])
                report_type = gr.Dropdown(label="# Report Type",
                                         value="Research Report",
                                         interactive=True,
                                         allow_custom_value=False,
                                         choices=["Research Report",
                                                 "Resource Report",
                                                 "Outline Report"])
            input_box = gr.Textbox(label="# What would you like to research next?", placeholder="Enter your question here")
            search_btn = gr.Button("Search Online")
            search_btn.click(search, inputs=[input_box, agent_type], outputs=agent_output)
            submit_btn = gr.Button("Generate Report")
            submit_btn.click(run_agent, inputs=[report_type], outputs=research_report)
            gr.Examples(["Should I invest semi-conductor industry in 2023?"], inputs=input_box)
            
    with gr.Tab("Literature Review"):
        pass

demo.queue().launch(width=400)