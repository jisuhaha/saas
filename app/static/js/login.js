let currentUrl = window.location.href;
var naver_id_login = new naver_id_login("naver_developer_APIKey", currentUrl.replace('/login','/naverLoginCallback') );
var state = naver_id_login.getUniqState();
naver_id_login.setButton("white", 3, 40);
naver_id_login.setDomain(currentUrl.replace('/login','/naverLogin'));
naver_id_login.setState(state);
naver_id_login.init_naver_id_login();

Kakao.init('kakao_APIKey');

function loginWithKakao() {
    Kakao.Auth.authorize({
        redirectUri: currentUrl.replace('/login','/kakaoLoginCallback'),
    });
}
displayToken()
function displayToken() {
    var token = getCookie('authorize-access-token');

    if (token) {
        Kakao.Auth.setAccessToken(token);
        Kakao.Auth.getStatusInfo()
            .then(function (res) {
                if (res.status === 'connected') {
                    document.getElementById('token-result').innerText
                        = 'login success, token: ' + Kakao.Auth.getAccessToken();
                }
            })
            .catch(function (err) {
                Kakao.Auth.setAccessToken(null);
            });
    }
}

function getCookie(name) {
    var parts = document.cookie.split(name + '=');
    if (parts.length === 2) { return parts[1].split(';')[0]; }
}


function submitLogin() {
    let email = $('#email').val();
    let password = $('#password').val();
    $.ajax({
        url: '/loginFromPortal',
		dataType: 'json',
        data: {
            email: email,
            password: password
        },
		type: "POST",
		success: function (data) {
			if ( data.status =='success'){
                location.href = "/";
            }else{
                alert(data.message);
            }
		},
		error: function (xhr, textStatus, errorThrown) {
			
		}

    })
}