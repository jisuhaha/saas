$('#btn_content_edit').click(function () {
    let urlParams = new URLSearchParams(window.location.search);

    $.ajax({
        url: '/contentEdit',
        type: 'POST',
        data: { 'contentID': urlParams.get('contentID') },
        success: function onData(data) {
            if (data.status === 'success') {
                editPageByContentID(urlParams.get('contentID'));
            }
        },
        error: function onError(error) {

        }

    })
});

function editPageByContentID(contentID){
    var form = document.createElement('form');
    var objs;
    objs = document.createElement('input');
    objs.setAttribute('type', 'text');
    objs.setAttribute('name', 'contentID');
    objs.setAttribute('value', contentID );
    form.appendChild(objs);
    form.setAttribute('method', 'post');
    form.setAttribute('action', "/boardEdit"); 
    document.body.appendChild(form);
    form.submit();
}

$('#btn_content_delete').click(function () {
    let urlParams = new URLSearchParams(window.location.search);
    $.ajax({
        url: '/contentDelete',
        type: 'POST',
        data: { 'contentID': urlParams.get('contentID') },
        success: function onData(data) {
            if (data.status === 'success') {
                alert(data.message);
                location.href = '/board';
            } else {
                alert(data.message);
            }

        },
        error: function onError(error) {
            console.error(error);
        }
    })

    console.log('click Delete');
});



const sliderWrap = document.querySelector(".slider__wrap");
const sliderImg = document.querySelector(".slider__img");       // 보여지는 영역
const sliderInner = document.querySelector(".slider__inner");   // 움직이는 영역
const slider = document.querySelectorAll(".slider");            // 각각의 이미지

let currentIndex = 0;                                               // 현재 보이는 이미지
let sliderCount = slider.length;                                    // 이미지 갯수
let sliderWidth = sliderImg.offsetWidth;                            // 이미지 가로값
let sliderClone = sliderInner.firstElementChild.cloneNode(true);    // 첫번째 이미지 복사
sliderInner.appendChild(sliderClone);                               // 첫번째 이미지를 마지막에 넣어줌

function sliderEffect() {
    if (slider.length == 1) {
        return;
    }
    currentIndex++;
    sliderInner.style.transition = "all 0.6s";

    sliderInner.style.transform = "translateX(-" + sliderWidth * currentIndex + "px)";

    // sliderInner.style.transform = "translateX(-600px)";      600*1
    // sliderInner.style.transform = "translateX(-1200px)";     600*2
    // sliderInner.style.transform = "translateX(-1800px)";     600*3
    // sliderInner.style.transform = "translateX(-2400px)";     600*4
    // sliderInner.style.transform = "translateX(-3000px)";     600*5
    // sliderInner.style.transform = "translateX(-3600px)";     600*1

    // 마지막 사진에 위치했을 때 
    if (currentIndex == sliderCount) {
        setTimeout(() => {
            sliderInner.style.transition = "0s";
            sliderInner.style.transform = "translateX(0px)";
        }, 700);

        currentIndex = 0;
    }


}

setInterval(sliderEffect, 2000);