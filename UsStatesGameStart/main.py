import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



##To Get the state Co-ordinate form image
# def get_mouse_click_coor(x, y):
# 	print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
all_status = data['state'].to_list()
guesses_states = []


while len(guesses_states) < 51:
	answer_states = screen.textinput(title=f"{len(guesses_states)}/50 State correct? ", prompt="What is another state name?")
	answer_states = answer_states.title()
	searched_state = data[data.state == answer_states]

	if(answer_states == 'Exit'):
		#missing_states = list(set(all_status) - set(guesses_states))
		missing_states = [statelc for statelc in all_status if statelc not in guesses_states]
		data_dict = {
			"state": missing_states,
		}
		data = pandas.DataFrame(data_dict)
		data.to_csv("states_to_learn.csv")
		break

	if not searched_state.empty:
		guesses_states.append(answer_states)
		new_state = turtle.Turtle()
		new_state.hideturtle()
		new_state.penup()
		new_state.goto(int(searched_state.x.item()), int(searched_state.y.item()))
		new_state.write(answer_states, True, align="center")





