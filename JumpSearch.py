import gradio as gr
import math
import random
import time

numbers = []
log_text = ""

# Generate a new sorted list
def generate_numbers():
    global numbers, log_text
    numbers = [
        random.randint(1,10), random.randint(11,20), random.randint(21,30),
        random.randint(31,40), random.randint(41,50), random.randint(51,60),
        random.randint(61,70), random.randint(71,80), random.randint(81,90),
        random.randint(91,100)
    ]
    numbers.sort()
    log_text = ""
    return render_list(), log_text, 0  # Reset number input to 0

# Render the list with highlighted index
def render_list(current_index=None, bad=False):
    html = """
    <div style='display:flex; gap:6px; justify-content:center; padding:12px; background-color:#111; border-radius:6px;'>
    """
    for i, num in enumerate(numbers):
        color = "#2a2a2a"  # normal
        if bad:
            color = "#8b1e1e"  # red for invalid
        if i == current_index:
            color = "#ffe066"  # yellow highlight
        html += f"""
        <div style='width:42px; height:42px; line-height:42px; text-align:center; border:1px solid #444; background:{color}; color:white; font-family:Arial; font-size:14px; border-radius:4px;'>{num}</div>
        """
    html += "</div>"
    return html

# Flash red for invalid number
def flash_invalid():
    global log_text
    log_text = "Your number is not in the list. Try again.\n"
    yield render_list(bad=True), log_text
    time.sleep(0.8)
    yield render_list(), log_text

# Jump search animation with very simple steps
def jump_search(target):
    global log_text

    # Validate input type
    if not isinstance(target, (int, float)) or target not in numbers:
        for frame in flash_invalid():
            yield frame
        return

    log_text = ""
    n = len(numbers)
    step = int(math.sqrt(n))
    prev = 0

    log_text += f"We will jump {step} steps each time to find the number.\n"

    # Jump phase
    while prev < n:
        next_index = min(step, n) - 1
        log_text += f"Jumping to index {next_index} which has the number {numbers[next_index]}.\n"
        yield render_list(next_index), log_text
        time.sleep(0.9)  # slower jump

        if numbers[next_index] == target:
            log_text += f"We landed on the number! Found it at index {next_index}.\n"
            yield render_list(next_index), log_text
            return

        if numbers[next_index] > target:
            log_text += f"The number we jumped to is bigger than our target. We will check each number step by step now.\n"
            break

        prev = step
        step += int(math.sqrt(n))

    # Linear search phase
    log_text += f"Checking each number one by one starting from index {prev}.\n"
    while prev < n and numbers[prev] < target:
        log_text += f"Checking index {prev}, it is {numbers[prev]}, not our number.\n"
        yield render_list(prev), log_text
        time.sleep(0.8)  # slower linear search
        prev += 1

    # Final check
    if prev < n and numbers[prev] == target:
        log_text += f"Found our number at index {prev}!\n"
        yield render_list(prev), log_text
    else:
        log_text += "We reached the end and did not find the number.\n"
        yield render_list(), log_text

# Gradio interface
with gr.Blocks() as demo:
    list_display = gr.HTML()
    target = gr.Number(precision=0)
    run = gr.Button("Run")
    regen = gr.Button("New List")
    log = gr.Textbox(lines=10)

    regen.click(generate_numbers, outputs=[list_display, log, target])
    run.click(jump_search, inputs=target, outputs=[list_display, log])
    demo.load(generate_numbers, outputs=[list_display, log, target])

demo.launch()