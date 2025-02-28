import gradio as gr
import socket

def get_hostname():
    return socket.gethostname()

def on_ui_tabs():
    with gr.Blocks() as demo:
        gr.Markdown("## 호스트네임 확인")
        output = gr.Textbox(label="호스트네임")
        btn = gr.Button("호스트네임 가져오기")
        btn.click(get_hostname, outputs=output)
    return [(demo, "호스트네임 확장", "hostname_extension")]

# Stable Diffusion WebUI에서 확장 프로그램을 인식하도록 함
try:
    import modules.scripts as scripts
    scripts.script_callbacks.on_ui_tabs(on_ui_tabs)
except ImportError:
    print("Stable Diffusion WebUI에서 실행해야 합니다.")
