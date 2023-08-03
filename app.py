import gradio as gr

from config import check_openai_api_key
from agent.research_agent import ResearchAgent
from agent.toolkits import english_polishing
from statics.style import *


check_openai_api_key()
history = ""
history_num = 0
history_tasks = []
max_histroy_num = 30

def run_agent(task, agent, report_type):
    global history, history_num, history_tasks
    history_num += 1
    history_tasks.append(task)
    assistant = ResearchAgent(task, agent)
    yield from assistant.write_report(report_type)


with gr.Blocks(theme=gr.themes.Base(),
               title="AI Research Assistant",
               css=css) as demo:
    gr.HTML(top_bar)
    with gr.Tab(label="🔦Report"):
        with gr.Column():
            gr.HTML(research_report_html)
            research_report = gr.Markdown(value="&nbsp;&nbsp;**Report will appear here...**",
                                          elem_classes="output")
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
            submit_btn = gr.Button("Generate Report", elem_id="primary-btn")

            gr.Examples(["Should I invest in the Large Language Model industry in 2023?", 
                         "Is it advisable to make investments in the electric car industry during the year 2023?",
                         "What constitutes the optimal approach for investing in the Bitcoin industry during the year 2023?",
                         "What are the most recent advancements in the domain of superconductors as of 2023?"], 
                         inputs=input_box)
            
            with gr.Accordion(label="# Research History (Max 30)", elem_id="history", open=False):
                research_history = gr.Markdown()
            
            def store_research(content):
                global history_num, history_tasks, history
                if 0 < history_num <= max_histroy_num:
                    history += f'<details>\
                                    <summary>Research History {history_num}: <i>{history_tasks[-1]}</i></summary>\
                                    <div id="history_box">{content}</div>\
                                 </details>'
                return history
                    
            submit_btn.click(run_agent, inputs=[input_box, agent_type, report_type], outputs=research_report)\
                      .then(store_research, inputs=[research_report], outputs=research_history)

    
    with gr.Tab("✒️English Polishing"):
        gr.HTML(english_polishing_html)
        polished_result = gr.Markdown("&nbsp;&nbsp;**Polished result will appear here...**", elem_classes="output")
        sentences = gr.Textbox(label="# What would you like to polish?", placeholder="Enter your sentence here")
        
        with gr.Row():
            polish_btn = gr.Button("Polish", elem_id="primary-btn")
            save_btn = gr.Button("Save", elem_id="primary-btn")
        
        polish_btn.click(english_polishing, inputs=[sentences], outputs=polished_result)
        
        def save_result(history, origin, result):
            history += f"\n**Origin** : {origin}\n\n**Polished Result** : {result}"
            return history
        
        gr.HTML(history_result_html)
        history_result = gr.Markdown("&nbsp;&nbsp;**History result will appear here...**")
        save_btn.click(save_result, inputs=[history_result, sentences, polished_result], outputs=history_result)

    with gr.Tab("📑Literature Review"):
        gr.HTML(literature_review_html)

demo.queue().launch()