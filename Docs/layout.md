GAME PLAN (so to speak)

Outline what the game looks like, what the implementations are on paper or sep
document first. Right now I'm using comments inside the code itself which is
acceptable but a proper outline is important.

Order should be:

  Outline -> Code -> Debug -> Code -> Finishing touches

However, coding bit by bit and checking the working status I think is important
and as soon as I have a general idea starting on that is not a bad idea.

I'm using markdown, here's the run-down:
- #### indicates heading for a room or instance
- \*()* italicized is an action, something to implement.
- [] is just like () in english strings for thoughts.


#### MAIN MENU
An intro to the game with a start function and a command list that's basic?
I want the player to be able to interact with the environment zork-style,
research zork?

*(list commands)* - Should I have a commands list default displayed when action
is insisted? Could look like:

        `|| LOOK || USE || FIGHT || MOVE || INVENTORY || STATS || HELP ||`


*(start game)* - `start()`
*(initialize character)* - Starting with a character of your choice could be
interesting, attributes would change based on race. Currently defining `name`,
`race`, and `class` upon init.

#### DARK ROOM
Starting in a dark room [underground?] you *(fumble around)* to find a ladder.
Don't know how you got here, *(what's your name)*? --> conflicts with init
of Player, could have separate functions for definition.
*(Climb the ladder)*=]

`if light_source in inventory:`  # define light_source and inventory
    `room_state = illuminated`  # room_state and illuminated must be defined
    `return room_state`  


#### COURTYARD
On the surface you see a courtyard with a fountain and 4 doors, you are
completely walled in.
*(weather system - but it will be sunny everytime on the first loop)*
There is daylight and it's sunny.
*(door choice)* Which will you choose? [Should some be locked?]}

#### DOOR 1
