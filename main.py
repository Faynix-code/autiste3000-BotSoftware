#Bye Faynix-code 

def on_button_pressed_a():
    radio.send_value("status", 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    Démarer()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_value("status", 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global people, diameter
    if name == "commande":
        if value == 1:
            Démarer()
        if True:
            Arreter()
    if name == "people":
        people = value
    if name == "diameter":
        diameter = 0
radio.on_received_value(on_received_value)

def Démarer():
    global find, tour
    while find == 0:
        radio.send_value("find", 0)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            255)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            50)
        basic.pause(2800)
        maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            50)
        basic.pause(800)
        maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
        basic.pause(3000)
        if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            maqueenPlusV2.show_color(DigitalPin.P15,
                maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.GREEN))
            maqueenPlusV2.set_rgbl_led(maqueenPlusV2.DirectionType.ALL,
                maqueenPlusV2.CarLightColors.GREEN)
            find = 1
            maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
            radio.send_value("find", 1)
            music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("Comment vas tu ? ")
            basic.show_string("A : ")
            basic.show_icon(IconNames.HAPPY)
            basic.show_string("B : ")
            basic.show_icon(IconNames.SAD)
            return
        basic.pause(500)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.BACKWARD,
            55)
        basic.pause(1000)
        maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
        tour += 1
def Arreter():
    maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
tour = 0
find = 0
people = 0
diameter = 0
music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.IN_BACKGROUND)
diameter = 120
people = 5
find = 0
maqueenPlusV2.i2c_init()
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
radio.set_group(67)

def on_forever():
    huskylens.request()
    if maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14) <= 15:
        basic.show_icon(IconNames.BUTTERFLY)
        radio.send_string("Obstacle")
        maqueenPlusV2.control_motor_stop(maqueenPlusV2.MyEnumMotor.ALL_MOTOR)
    else:
        basic.show_icon(IconNames.YES)
    if huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        maqueenPlusV2.show_color(DigitalPin.P15,
            maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.RED))
    else:
        maqueenPlusV2.show_color(DigitalPin.P15,
            maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.PURPLE))
    radio.send_value("accelerationy", input.acceleration(Dimension.Y))
    radio.send_value("accelerationx", input.acceleration(Dimension.X))
    radio.send_value("temperature", input.temperature())
    radio.send_value("niveausonore", input.sound_level())
    radio.send_value("signal",
        radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH))
basic.forever(on_forever)
