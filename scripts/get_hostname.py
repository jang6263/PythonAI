import gradio as gr
import socket

def get_hostname():
    return socket.gethostname()

def on_ui_tabs():
    with gr.Blocks() as demo:
        gr.Markdown("## Hostname")
        output = gr.Textbox(label="Hostname")
        btn = gr.Button("Hostname")
        btn.click(get_hostname, outputs=output)
    return [(demo, "Hostname", "hostname_extension")]

try:
    import modules.scripts as scripts
    scripts.script_callbacks.on_ui_tabs(on_ui_tabs)
except ImportError:
    print("You Must Run Stable Diffusion WebUI")
