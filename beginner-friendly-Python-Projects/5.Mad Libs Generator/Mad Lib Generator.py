# Define the Story Template
story_template = """Once upon a time, there was a {adjective} {noun} 
who loved to {verb} all day long. One day, the {noun} decided to {verb} 
to the {adjective} {place} to see if there were any {plural_noun} to {verb} with.
When the {noun} arrived at the {place}, they saw a {adjective} {animal} 
and started to {verb} with it. Suddenly, a {adjective} {noun} appeared 
out of nowhere and tried to {verb} the {noun}. But the {noun} was too {adjective} and {verb} away to safety."""


# Define the Mad libs Generator Function
def generate_story(template):
    # Get user input for the placeholders
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    plural_noun = input("Enter a plural noun: ")
    animal = input("Enter an animal: ")

    # Replace the placeholders with user input
    story = template.format(adjective=adjective, noun=noun, verb=verb, place=place, plural_noun=plural_noun, animal=animal)

    return story


# Print the Generated Story
story = generate_story(story_template)
print(story)
