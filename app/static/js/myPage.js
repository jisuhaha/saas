function changePasswordForm() {
    let password = $('#password').val();
    let userID = $('#userID').val();
    let isPosoblePost = false;
    if (password.length === 0) {
        $('#password').focus();
        $('#errorPassword').text('비밀번호를 입력해주세요');
    } else {
        $('#errorPassword').text('');
        isPosoblePost = true
    }
    if ( isPosoblePost ) {
        $.ajax({
            url: '/modifyUser',
            dataType: 'json',
            type: "POST",
            data: {
                password: password,
                userID: userID
            },
            success: function (data) {
                if(data.status==='successed'){
                    alert(data.message);
                    location.href='/myPage';
                }else{
                    alert(data.message);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
            }


        })
    }

}