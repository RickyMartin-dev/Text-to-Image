# Imports
from text_to_image import TextToImageTool
import gradio as gr

# Define Text to Image Tool
tool = TextToImageTool()

# Helper Function, necessary for Gradio
def fn(*args, **kwargs):
    return tool(*args, **kwargs)

# Gradio Interface 
gr.Interface(
    fn=fn,
    inputs=tool.inputs,
    outputs=tool.outputs,
    title="TextToImageTool",
    article=tool.description,
).queue(concurrency_count=5).launch()