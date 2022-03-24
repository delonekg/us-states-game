import turtle
import pandas

# Retrieve coordinate data
states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.to_list()


# Setting up the screen
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) <= 50:

    # Ask user for answer
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's the name of another U.S. state you can think of?").title()

    if answer == "Exit":
        break

    for state in state_names:
        if answer == state and answer not in guessed_states:
            state_row = states_data[states_data.state == state].to_dict()
            line_num_x = list(state_row["x"].keys())[0]
            line_num_y = list(state_row["y"].keys())[0]
            state_xcor = state_row["x"][line_num_x]
            state_ycor = state_row["y"][line_num_y]
            state_text = turtle.Turtle()
            state_text.hideturtle()
            state_text.penup()
            state_text.goto(state_xcor, state_ycor)
            state_text.write(arg=answer, font=("Arial", 10, "normal"))
            guessed_states.append(answer)

# Generate a CSV file which contains all the states the user needs to learn
states_to_learn = []
df_dict = {
    "State": states_to_learn
}

for state in state_names:
    if state not in guessed_states:
        states_to_learn.append(state)

df = pandas.DataFrame(df_dict)
df.to_csv("states_to_learn.csv")
