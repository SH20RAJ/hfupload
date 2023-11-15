import gradio as gr
from gradio.components import File
from huggingface_hub import login, upload_file
import time

login(token="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")

def upload(file):

  # Generate filename with timestamp
  filename = f"{time.time()}_{file.name}" 
  
  upload_file(
    file.file,
    filename, 
    "droidcv/sopdrive",
    repo_type="space"
  )

  url = f"https://huggingface.co/droidcv/sopdrive/resolve/{filename}"

  return f"Uploaded to: {url}"

demo = gr.Interface(
  fn=upload,
  inputs=File(type="file"),
  outputs="text"
)

if __name__ == "__main__":
  demo.launch()