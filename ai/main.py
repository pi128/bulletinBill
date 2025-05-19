import re
from ai.prompts import get_prompt
from ai.generator import generate_code
from ai.file_writer import save_code

task = input("What would you like to build?\n")
prompt = get_prompt(task)
code = generate_code(prompt)

# Convert task to snake_case filename
def task_to_filename(task: str) -> str:
    task = re.sub(r"[^\w\s]", "", task)          # Remove punctuation
    task = "_".join(task.lower().split())        # Convert to snake_case
    return f"{task[:40]}.py"                     # Limit length if needed

filename = task_to_filename(task)
save_code(code, filename)

print(f"Saved generated code to: {filename}")