import os
import gradio as gr

from datetime import datetime, timezone

from config import check_openai_api_key
from agent.research_agent import ResearchAgent
from agent.toolkits import english_polishing
from agent import prompts
from statics.style import *


check_openai_api_key()
report_history_buffer = ""
report_history_tasks = []
polish_history_buffer = ""

REPORT_HISTORY_FILE_PATH = "./statics/report_history_buffer.md"


def load_report_history():
    global report_history_buffer
    if os.path.exists(REPORT_HISTORY_FILE_PATH):
        with open(REPORT_HISTORY_FILE_PATH, "r") as f:
            report_history_buffer = f.read()
    else:
        open(REPORT_HISTORY_FILE_PATH, "w").close()
    return report_history_buffer

def run_agent(task, agent_type, report_type, system_prompt, extra_prompt):
    global report_history_tasks
    report_history_tasks.append(task)
    assistant = ResearchAgent(task, agent_type, system_prompt)
    report_type_func = prompts.get_report_by_type(report_type)
    yield from assistant.call_agent_stream(report_type_func(assistant.question,
                                                            assistant.search_online(),
                                                            extra_prompt=extra_prompt))


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
            
            with gr.Accordion("Additional settings", open=False):
                system_prompt = gr.TextArea(prompts.generate_agent_role_prompt(agent_type.value), label="Agent prompt", interactive=True, show_copy_button=True)
                report_type_prompt = gr.TextArea(prompts.generate_report_prompt(f'{input_box.value}', report_type.value), label="Report type prompt (no editable)", interactive=False, show_copy_button=True)
                extra_prompt = gr.TextArea(label="Extra prompt", interactive=True, show_copy_button=True)

                def on_select_agent(evt: gr.SelectData):
                    return f"{prompts.generate_agent_role_prompt(evt.value)}"
                def on_select_input_box(input, report_type):
                    return f"{prompts.generate_report_prompt(f'{input}', report_type)}"
                def on_select_report_type(evt: gr.SelectData, input_box):
                    return f"{prompts.generate_report_prompt(f'{input_box}', evt.value)}"
                
                agent_type.select(on_select_agent, None, system_prompt)
                input_box.input(on_select_input_box, inputs=[input_box, report_type], outputs=report_type_prompt)
                report_type.select(on_select_report_type, inputs=[input_box], outputs=report_type_prompt)

            submit_btn = gr.Button("Generate Report", elem_id="primary-btn")

            gr.Examples(["Should I invest in the Large Language Model industry in 2023?", 
                         "Is it advisable to make investments in the electric car industry during the year 2023?",
                         "What constitutes the optimal approach for investing in the Bitcoin industry during the year 2023?",
                         "What are the most recent advancements in the domain of superconductors as of 2023?"], 
                         inputs=input_box)
            
            with gr.Accordion(label="# Report History", elem_id="history", open=False):
                report_history = gr.Markdown(value=load_report_history)

            def store_report(content):
                global report_history_tasks, report_history_buffer
                report_task = report_history_tasks[-1][:min(100, len(report_history_tasks[-1]))]
                time_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %p")
                new_report = f'<details> \
                                   <summary>UTC {time_stamp}: \
                                       <i>{report_task}</i></summary> \
                                   <div id="history_box">{content}</div> \
                               </details>'
                report_history_buffer += new_report
                with open("./statics/report_history_buffer.md", "a+") as f:
                    f.write(new_report)
                return report_history_buffer

            submit_btn.click(run_agent, inputs=[input_box, agent_type, report_type, system_prompt, extra_prompt], outputs=report)\
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