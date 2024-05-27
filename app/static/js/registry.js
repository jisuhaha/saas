function submitForm() {
    let user_Name = $('#user_Name').val();
    let user_Email = $('#user_Email').val();
    let password = $('#password').val();
    const expEmailText = /^[A-Za-z-0-9\-\.]+@[A-Ja-z-0-9\-\.]+\.[A-Ja-z-0-9]+$/;
    let isPosoblePost = [0, 0, 0]
    if (user_Name.length === 0) {
        $('#user_Name').focus();
        $('#errorName').text('닉네임을 입력해주세요');
    } else {
        $('#errorName').text('');
        isPosoblePost[0] = 1
    }
    if (user_Email.length === 0) {
        $('#user_Email').focus();
        $('#errorEmail').text('메일을 입력해주세요');
    } else {
        if (!expEmailText.test(user_Email)) {
            $('#errorEmail').text('이메일 형식을 확인하세요');
            $('#email').focus();
        } else {
            $('#errorEmail').text('');
            isPosoblePost[1] = 1
        }
    }
    if (password.length === 0) {
        $('#password').focus();
        $('#errorPassword').text('비밀번호를 입력해주세요');
    } else {
        $('#errorPassword').text('');
        isPosoblePost[2] = 1
    }
    if (isPosoblePost[0] === 1 && isPosoblePost[1] === 1 && isPosoblePost[2] === 1) {
        $.ajax({
            url: '/registryUser',
            dataType: 'json',
            type: "POST",
            data: {
                user_Name: user_Name,
                user_Email: user_Email,
                password: password
            },
            success: function (data) {
                if(data.status==='successed'){
                    alert(data.message);
                    location.href='/login';
                }else{
                    alert(data.message);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
            }


        })
    }

}