from ctransformers import AutoModelForCausalLM

model_file_path = r"C:\Users\kishan\Downloads\mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Load the model
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file=model_file_path, model_type="mistral", gpu_layers=50)
