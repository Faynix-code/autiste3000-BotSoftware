// Bye Faynix-code 
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendValue("status", 1)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    Démarer()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendValue("status", 2)
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (name == "commande") {
        if (value == 1) {
            Démarer()
        }
        
        if (true) {
            Arreter()
        }
        
    }
    
    if (name == "people") {
        people = value
    }
    
    if (name == "diameter") {
        diameter = 0
    }
    
})
function Démarer() {
    
    while (find == 0) {
        radio.sendValue("find", 0)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Forward, 255)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 50)
        basic.pause(2800)
        maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 50)
        basic.pause(800)
        maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
        basic.pause(3000)
        if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
            maqueenPlusV2.showColor(DigitalPin.P15, maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.Green))
            maqueenPlusV2.setRgblLed(maqueenPlusV2.DirectionType.All, maqueenPlusV2.CarLightColors.Green)
            find = 1
            maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
            radio.sendValue("find", 1)
            music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
            basic.showString("Comment vas tu ? ")
            basic.showString("A : ")
            basic.showIcon(IconNames.Happy)
            basic.showString("B : ")
            basic.showIcon(IconNames.Sad)
            return
        }
        
        basic.pause(500)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Backward, 55)
        basic.pause(1000)
        maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
        tour += 1
    }
}

function Arreter() {
    maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
}

let tour = 0
let find = 0
let people = 0
let diameter = 0
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
diameter = 120
people = 5
find = 0
maqueenPlusV2.I2CInit()
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
radio.setGroup(67)
basic.forever(function on_forever() {
    huskylens.request()
    if (maqueenPlusV2.readUltrasonic(DigitalPin.P13, DigitalPin.P14) <= 15) {
        basic.showIcon(IconNames.Butterfly)
        radio.sendString("Obstacle")
        maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
    } else {
        basic.showIcon(IconNames.Yes)
    }
    
    if (huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
        maqueenPlusV2.showColor(DigitalPin.P15, maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.Red))
    } else {
        maqueenPlusV2.showColor(DigitalPin.P15, maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.Purple))
    }
    
    radio.sendValue("accelerationy", input.acceleration(Dimension.Y))
    radio.sendValue("accelerationx", input.acceleration(Dimension.X))
    radio.sendValue("temperature", input.temperature())
    radio.sendValue("niveausonore", input.soundLevel())
    radio.sendValue("signal", radio.receivedPacket(RadioPacketProperty.SignalStrength))
})
