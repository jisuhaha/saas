const completechk = () => {
    let keyword = $('#location').val();
    if (keyword != '') {
        $.ajax({
            url: 'https://korean.visitkorea.or.kr/json/jsp' + '/trans_json.jsp',
            dataType: 'json',
            type: "POST",
            data: {
                type: 'ark',
                target: 'content',	// 사용자입력 단어: common, 데이터 : content
                convert: 'fw',
                query: keyword,
                datatype: 'json',
                charset: 'UTF-8'
            },
            success: function (data) {
                let resultArr = [];
                let compHtml = '';
                if (data.result[0].totalcount > 0)
                    data.result[0].items.forEach((item, index) => { if (index < 6) resultArr.push(item.keyword); });
                if (resultArr.length < 6 && data.result[1].totalcount > 0)
                    data.result[1].items.forEach((item) => { if (resultArr.length < 6) resultArr.push(item.keyword); });

                if (resultArr.length === 0) {
                    $('.related_search dl').empty();
                    $('.related_search').hide();
                    return;
                }
                resultArr.forEach((item, index) => {
                    let keyTxt = '';
                    if (item.indexOf(keyword) > -1)
                        keyTxt = item.replace(keyword, `<strong>${keyword}</strong>`);
                    else
                        keyTxt = item;
                    compHtml += `<dd id='searchResult'><a href="javascript:selectItem('${item}');">${keyTxt}</a></dd>`;
                });

                $('.related_search dl').html(compHtml);
                $('.related_search').show();
            },
            error: function (xhr, textStatus, errorThrown) {
                $('.related_search').hide();
            }
        });
    } else {
        $('.search_wrap .form .delete').hide();
        $('.related_search').hide();
    }
}
//단어기준 검색결과
$("#location").on("change keyup paste", function () {
    completechk();
});

//검색결과 선택 시 
function selectItem(itemText) {
    $('.related_search').hide();
    $('#location').val(itemText);

}

//취소 버튼
function cancleSubmit() {
    history.back();
}
let submitFlag = 0;
//등록버튼
function submitForm() {
    let title = $('#title').val();
    let location = $('#location').val();
    let content = $('#content').val();
    if (content.length === 0) {
        $('#content').focus();
        $('#errorContent').text('본문을 입력해주세요');
    } else {
        $('#errorContent').text('');
    }
    if (location.length === 0) {
        $('#location').focus();
        $('#errorLocation').text('장소를 입력해주세요');
    } else {
        $('#errorLocation').text('');
    }
    if (title.length === 0) {
        $('#title').focus();
        $('#errorTitle').text('제목을 입력해주세요');
    } else {
        $('#errorTitle').text('');
    }
    if (content.length !== 0 && location.length !== 0 && title.length !== 0) {
        if (submitFlag === 0) {
            submitBoardData(title, location, content);
            submitFlag = 1;
        }
    }
}

function submitBoardData(title, location, content) {
    $('#boardForm').submit();
}


var sec9 = document.querySelector('#ex9');
var btnUpload = sec9.querySelector('.btn-upload');
var inputFile = sec9.querySelector('input[type="file"]');
var uploadBox = sec9.querySelector('.upload-box');

/* 박스 안에 Drag 들어왔을 때 */
uploadBox.addEventListener('dragenter', function (e) {
    console.log('dragenter');
});

/* 박스 안에 Drag를 하고 있을 때 */
uploadBox.addEventListener('dragover', function (e) {
    e.preventDefault();
    var vaild = e.dataTransfer.types.indexOf('Files') >= 0;

    if (!vaild) {
        this.style.backgroundColor = 'red';
    }
    else {
        this.style.backgroundColor = 'green';
    }

    this.style.backgroundColor = 'green';
});

/* 박스 밖으로 Drag가 나갈 때 */
uploadBox.addEventListener('dragleave', function (e) {
    console.log('dragleave');

    this.style.backgroundColor = 'white';
});

/* 박스 안에서 Drag를 Drop했을 때 */
uploadBox.addEventListener('drop', function (e) {
    e.preventDefault();
    $('.thumbnailContainer').remove();
    $('#upload_container')
    let targetFile = document.querySelector('.file_tag');
    targetFile.files = e.dataTransfer.files;
    lastModifiedArr = [];
    let onloadIndex = 0;
    for (let i = 0; i < targetFile.files.length; i = i + 1) {
        var fReader = new FileReader();
        fReader.readAsDataURL(document.querySelector('.file_tag').files[i]);
        lastModifiedArr[i] = document.querySelector('.file_tag').files[i].lastModified;
        fReader.onloadend = function (event) {
            let div = '<div class="thumbnailContainer"><img class="thumbnailImage" src="' + event.target.result + '"><button class="deletebtn ' + onloadIndex + '" onclick="deleteItem(this)" type="button" data-index="' + lastModifiedArr[onloadIndex++] + '"><img src="/static/images/delete_btn.png"></button></div>'
            $('#image_container').append(div);
        }
    }
    this.style.backgroundColor = 'white';
});



function setThumbnail(event) {
    $('.thumbnailImage').remove();
    let targetFile = document.querySelector('.file_tag');
    lastModifiedArr = [];
    let onloadIndex = 0;
    for (let i = 0; i < targetFile.files.length; i = i + 1) {
        var fReader = new FileReader();
        fReader.readAsDataURL(document.querySelector('.file_tag').files[i]);
        lastModifiedArr[i] = document.querySelector('.file_tag').files[i].lastModified;
        fReader.onloadend = function (event) {
            let div = '<div class="thumbnailContainer"><img class="thumbnailImage" src="' + event.target.result + '"><button class="deletebtn ' + onloadIndex + '" onclick="deleteItem(this)" type="button" data-index="' + lastModifiedArr[onloadIndex++] + '"><img src="/static/images/delete_btn.png"></button></div>'
            $('#image_container').append(div);
        }
    }

}

function deleteItem(target) {
    console.log(target);
    const removeTargetId = target.dataset.index;
    let files = document.querySelector('.file_tag').files;
    const dataTranster = new DataTransfer();
    let removeTarget = target.parentElement;

    Array.from(files)
        .filter(file => file.lastModified != removeTargetId)
        .forEach(file => {
            dataTranster.items.add(file);
        });
    document.querySelector('.file_tag').files = dataTranster.files;

    removeTarget.remove();
}