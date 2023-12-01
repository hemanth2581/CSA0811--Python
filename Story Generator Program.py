import tkinter as tk
import random

# Characters in the story
start_character = "Tom"

end_character = "jerry"

# Story components
plot_points = [
   "Tom woke up in a magical forest and started exploring.",
    "He met a friendly rabbit named Fluffy who showed him the way.",
    "Tom discovered a hidden treasure chest filled with shiny jewels.",
    "He decided to share the treasure with the creatures of the forest.",
    "Tom and his new friends celebrated with a joyful feast.",
    "But suddenly, they heard a faint noise coming from the bushes...",
    "It was Jerry, the mischievous mouse, looking for an adventure!",
    "Jerry joined the celebration, and they all danced under the stars.",
    "As the night fell, everyone bid goodbye, promising to meet again soon.",
    "Tom waved happily as he walked back home, carrying joyful memories.",
    f"At home, {end_character} was waiting, eager to hear about Tom's magical day!"
]

# Function to generate the story
def generate_story(start_character, end_character, plot_points):
    story = f" "" \n                                 Tom and his adventure  " "\n \n" "Once upon a time, there was a boy named Tom "
    story += '  '
    for point in plot_points:
        story += point + '  '
    story += "The end. "
    story += f"{start_character} had an amazing adventure, especially with {end_character} by her side."
    return story

# Randomize the plot points for a unique story each time
random.shuffle(plot_points)

# Generate the story
story_text = generate_story(start_character, end_character, plot_points)

# Create a new window using tkinter
root = tk.Tk()
root.title(" Random Story Generator for kids using Python ")
root.geometry("500x400")

# Create a text widget to display the story
text_widget = tk.Text(root, wrap="word", font=("pink", 12))
text_widget.pack(expand=True, fill="both")
text_widget.insert("1.0", story_text)

# Start the tkinter main loop
root.mainloop()
