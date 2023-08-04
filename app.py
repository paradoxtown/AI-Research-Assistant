import gradio as gr

from config import check_openai_api_key
from agent.research_agent import ResearchAgent
from agent.toolkits import english_polishing
from statics.style import *


check_openai_api_key()
report_history_buffer = ""
report_history_num = 0
report_history_tasks = []
polish_history_buffer = ""

def run_agent(task, agent, report_type):
    global report_history_num, report_history_tasks
    report_history_num += 1
    report_history_tasks.append(task)
    assistant = ResearchAgent(task, agent)
    yield from assistant.write_report(report_type)


with gr.Blocks(theme=gr.themes.Base(),
               title="AI Research Assistant",
               css=css) as demo:
    gr.HTML(top_bar)
    with gr.Tab(label="🔦Report"):
        with gr.Column():
            gr.HTML(report_html)
            report = gr.Markdown(value="&nbsp;&nbsp;Report will appear here...",
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
            
            with gr.Accordion(label="# Report History", elem_id="history", open=False):
                report_history = gr.Markdown()
            
            def store_report(content):
                global report_history_num, report_history_tasks, report_history_buffer
                report_history_buffer += f'<details> \
                                               <summary>Research History {report_history_num}: \
                                                   <i>{report_history_tasks[-1]}</i></summary> \
                                               <div id="history_box">{content}</div> \
                                           </details>'
                return report_history_buffer
                    
            submit_btn.click(run_agent, inputs=[input_box, agent_type, report_type], outputs=report)\
                      .then(store_report, inputs=[report], outputs=report_history)
 
    with gr.Tab("✒️English Polishing"):
        gr.HTML(english_polishing_html)
        polished_result = gr.Markdown("&nbsp;&nbsp;Polished result will appear here...", elem_classes="output")
        sentences = gr.Textbox(label="# What would you like to polish?", placeholder="Enter your sentence here")
        
        with gr.Row():
            polish_btn = gr.Button("Polish", elem_id="primary-btn")
        
        with gr.Accordion(label="# Polishing History", elem_id="history", open=False):
            polish_history = gr.Markdown()        

        def store_polished_result(origin, result):
            global polish_history_buffer
            polish_history_buffer += f'<details> \
                                           <summary><i>{origin}</i></summary> \
                                           <div id="history_box">{result}</div> \
                                       </details>'
            return polish_history_buffer

        polish_btn.click(english_polishing, inputs=[sentences], outputs=polished_result) \
                  .then(store_polished_result, inputs=[sentences, polished_result], outputs=polish_history)

    with gr.Tab("📑Literature Review"):
        gr.HTML(literature_review_html)

demo.queue().launch()