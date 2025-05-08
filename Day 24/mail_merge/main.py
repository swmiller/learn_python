NAME_PLACEHOLDER = "[name]"

# Rread letter text
letter_text = ""
# mail_merge\Input\Letters\starting_letter.txt
with open("mail_merge\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_text = letter_file.read()


# Read invitations
names = []
with open("mail_merge\\Input\\Names\\invited_names.txt") as names_file:
    names = [name.strip() for name in names_file.readlines()]


# Create personalized letters
for name in names:
    personalized_letter = letter_text.replace(NAME_PLACEHOLDER, name)
    with open(
        f"mail_merge\\Output\\ReadyToSend\\letter_for_{name}.txt", "w"
    ) as output_file:
        output_file.write(personalized_letter)
