
$(function () {
	$.ajax({
		url: '/searchFestival',
		dataType: 'json',
		type: "POST",
		success: function (data) {
			let titleArr = [];
			let imgSrcArr = [];
			for(let i=0; i<data.length; i=i+1){
				titleArr[i] = data[i].title
				imgSrcArr[i] = data[i].first_image

			}

			festivalUpdate(titleArr, imgSrcArr);
		},
		error: function (xhr, textStatus, errorThrown) {
			$('.related_search').hide();
		}
	});

	function festivalUpdate(titleArr, imgSrcArr) {
		for(let i = 0; i< imgSrcArr.length; i=i+1){
			$("#main_festival00"+(i+1)).attr("src", imgSrcArr[i]);
		}
		var slides = $('.slides'),
			images = slides.find('img');

		images.each(function (i) {
			$(this).attr('data-id', i + 1);
		})

		var typed = new Typed('.typed-words', {
			strings: titleArr,
			typeSpeed: 80,
			backSpeed: 80,
			backDelay: 4000,
			startDelay: 1000,
			loop: true,
			showCursor: true,
			preStringTyped: (arrayPos, self) => {
				arrayPos++;
				id = '#main_festival00' + arrayPos;
				$('.slides img').removeClass('active');
				$('.slides img[data-id="' + arrayPos + '"]').addClass('active');
			}

		});

	}
	
})