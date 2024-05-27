$(function () {
    $.ajax({
        url: '/loginTopFrame',
        type: "POST",
        success: function (data) {
            let innerHtml;
            if (data.name.length > 0) {
                innerHtml = '<li id="logout"><a id="a_mypage"href="/myPage">마이페이지</a> <a href="#" onclick="logout()">로그아웃</a></li>';
            } else {
                innerHtml = '<li id="login"><a href="/login">로그인</a></li>';
            }
            var target = $('.li_board');
            target.after(innerHtml);
        },
        error: function (xhr, textStatus, errorThrown) {

        }

    })
})