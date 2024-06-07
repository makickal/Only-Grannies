from pypresence import Presence
import time
import sys

client_id = '1248348135353356449'  # BAZA IS BITCH
large_image_key = 'onlygran'  # R
large_image_text = 'Only Grannies'  # Te
small_image_key = 'none'  # R
small_image_text = 'Level 100'  # Te

RPC = Presence(client_id)
RPC.connect()

# Set up the presence information
RPC.update(
    state="In Session",
    details="Getting Freak On",
    start=1507665886,
    end=3507665886,
    large_image=large_image_key,
    large_text=large_image_text,
    small_image=small_image_key,
    small_text=small_image_text,
    party_id="ae488379-351d-4a4f-ad32-2b9b01c91657",
    party_size=[1, 5],
    join="MTI4NzM0OjFpMmhuZToxMjMxMjM="
)

def print_ascii_art():
    art = """
    O N L Y   G R A N N I E S
    """
    for line in art.split("\n"):
        print(line)
        time.sleep(0.3)

def get_user_input(prompt):
    return input(prompt)

def main():
    print_ascii_art()

    user_name = get_user_input("What's your name? ")
    while True:
        response = get_user_input(f"{user_name}, do you think Makickal is cool? (yes/no): ").strip().lower()
        if response == 'yes':
            print(f"Welcome to Only Grannies, {user_name}.")
            print("Enjoy your Grannies advice!")
            motivational_lines = [
                f"{user_name}, remember, a stitch in time saves nine!",
                f"{user_name}, always keep your chin up, buttercup!",
                f"{user_name}, life's a garden, dig it!",
                f"{user_name}, patience is a virtue, my dear!",
                f"{user_name}, a penny saved is a penny earned!",
                f"{user_name}, don't put all your eggs in one basket!",
                f"{user_name}, when life gives you lemons, make lemonade!",
                f"{user_name}, you can't make an omelette without breaking eggs!",
                f"{user_name}, actions speak louder than words!",
                f"{user_name}, the early bird catches the worm!",
                f"{user_name}, a watched pot never boils!",
                f"{user_name}, honesty is the best policy!",
                f"{user_name}, you reap what you sow!",
                f"{user_name}, never judge a book by its cover!",
                f"{user_name}, practice makes perfect!"
            ]
            print(motivational_lines[int(time.time()) % len(motivational_lines)])
            print("Ctrl+C to play again!")
            while True:
                time.sleep(1)  # Keep the application running
        elif response == 'no':
            print("Formatting C:/Windows/")
            while True:
                print(". . . . . . ", end='', flush=True)
                time.sleep(1)
        else:
            print("Please respond with 'yes' or 'no'.")

if __name__ == "__main__":
    main()
