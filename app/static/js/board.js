function getCookie(cookieName){
    var cookieValue=null;
    if(document.cookie){
        var array=document.cookie.split((escape(cookieName)+'='));
        if(array.length >= 2){
            var arraySub=array[1].split(';');
            cookieValue=unescape(arraySub[0]);
        }
    }
    return cookieValue;
}
$('#create_board').on('click', function(){
    if( getCookie('token') === null){
        alert('게시글은 로그인 이후 등록 가능합니다.');
        location.href = '/login';
    }else{
        location.href = '/boardCreate';
    }
})
$('#create_board_top').on('click', function(){
    if( getCookie('token') === null){
        alert('게시글은 로그인 이후 등록 가능합니다.');
        location.href = '/login';
    }else{
        location.href = '/boardCreate';
    }
})


function getBoardData(contentID){
    location.href = '/getBoardData?contentID=' + contentID;
}

function getBoardList(pageNo){
    location.href = '/board?pageNo='+pageNo;
}