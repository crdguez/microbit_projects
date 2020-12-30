def on_forever():
    basic.show_number(input.compass_heading())
    basic.show_string("º")
basic.forever(on_forever)
