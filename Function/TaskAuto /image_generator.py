import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from PIL import Image

# Load the model
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
stable_diffusion_model = StableDiffusionPipeline.from_pretrained(model_id, varient="fp16", torch_dtype=torch.float16)
stable_diffusion_model.to(device)

def generate_image(prompt):
    with autocast(device):
        image = stable_diffusion_model(prompt, guidance_scale=8.5)["sample"][0]
    image.save('generated_image.png')
    return image

# Main loop to take live prompts from the user
if __name__ == "__main__":
    while True:
        prompt = input("Enter a prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            print(f"Generating image for prompt: {prompt}")
            generated_image = generate_image(prompt)
            generated_image.show()  # This will open the image using the default image viewer
        except Exception as e:
            print(f"An error occurred: {e}")
