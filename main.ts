input.onButtonPressed(Button.A, function () {
    for (let a = 0; a <= 4; a++) {
        for (let i = 0; i <= 4; i++) {
            led.toggle(a, i)
            basic.pause(pauseLen)
            led.toggle(a, i)
            basic.pause(pauseLen)
        }
    }
})
input.onButtonPressed(Button.B, function () {
	
})
let pauseLen = 0
pauseLen = 100
