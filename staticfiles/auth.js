/*
<script type="text/javascript">
	var keyboardzone = document.getElementById("keyboardzone");
	var input = document.getElementById("myinput");

	var keyboard = new customKeyboard(
		keyboardzone,
		input, 
        function() {
            console.log("click : ", text);
        },
        function() {
            console.log("esc");
        },
        function(e) {
            console.log("앤터 : ", text);
        }, 
        null
    );

	input.addEventListener("click", function() {
        //input 태그를 자신으로 설정
        keyboard.setInput(this);
        //키패드 클릭 이벤트 설정
        keyboard.setClick(function(text) {
            console.log("input을 click한 후 : ", text);
        })
        //앤터 이벤트 설정
        keyboard.setEnter(function(e) {
            menu3searching(e)
        });
    })
</script>
*/
window.addEventListener('DOMContentLoaded', function() {
    var keyboardzone = document.getElementById("keyboard-div");
    
    const keyboard = new customKeyboard(
        keyboardzone,
        null,
        function () {},
        function () {},
        function () {},
    );

    let inputElements = document.getElementsByTagName('input');
    for (let i = 0; i < inputElements.length; i++) {
        inputElements[i].addEventListener("click", function () {
            keyboard.setInput(inputElements[i]);
        })
    }
})
