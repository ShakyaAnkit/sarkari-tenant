jQuery('.temperament-prev-btn').hide();

	var x;
	var count;
	var current;
	var percent;
	var z = [];

	init();
	getCurrentSlide();
	// goToNext();
	// goToPrev();
	// getCount();
	// checkStatus();
	// buttonConfig();
	buildStatus();
	deliverStatus();
	submitData();
	goBack();

	function init() {
		
		jQuery('.temperament-survey-container .temperament-survey-page').each(function() {

			var item;
			var page;

			item = jQuery(this);
			page = item.data('page');

			item.addClass('temperament-page-'+page);
			//item.html(page);

		});

	}

	function getCount() {

		count = jQuery('.temperament-survey-page').length;
		return count;

	}

	// function goToNext() {

	// 	jQuery('.temperament-next-btn').on('click', function() {
	// 		goToSlide(x);
	// 		getCount();
	// 		current = x + 1;
	// 		var g = current/count;
	// 		// buildProgress(g);
	// 		var y = (count + 1);
	// 		getButtons();
	// 		jQuery('.temperament-survey-page').removeClass('active');
	// 		jQuery('.temperament-page-'+current).addClass('active');
	// 		getCurrentSlide();
	// 		checkStatus();
	// 		if( jQuery('.temperament-page-'+count).hasClass('active') ){
	// 			if( jQuery('.temperament-page-'+count).hasClass('pass') ) {
	// 				jQuery('.temperament-finish-btn').addClass('active');
	// 			}
	// 			else {
	// 				jQuery('.temperament-page-'+count+' .temperament-survery-content .temperament-survey-item').on('click', function() {
	// 					jQuery('.temperament-finish-btn').addClass('active');
	// 				});
	// 			}
	// 		}
	// 		else {
	// 			jQuery('.temperament-finish-btn').removeClass('active');
	// 			if( jQuery('.temperament-page-'+current).hasClass('pass') ) {
	// 				jQuery('.temperament-survey-container').addClass('good');
	// 				jQuery('.temperament-survey').addClass('okay');
	// 			}
	// 			else {
	// 				jQuery('.temperament-survey-container').removeClass('good');
	// 				jQuery('.temperament-survey').removeClass('okay');
	// 			}
	// 		}
	// 		buttonConfig();
	// 	});

	// }

	// function goToPrev() {

	// 	jQuery('.temperament-prev-btn').on('click', function() {
	// 		goToSlide(x);
	// 		getCount();			
	// 		current = (x - 1);
	// 		var g = current/count;
	// 		// buildProgress(g);
	// 		var y = count;
	// 		getButtons();
	// 		jQuery('.temperament-survey-page').removeClass('active');
	// 		jQuery('.temperament-page-'+current).addClass('active');
	// 		getCurrentSlide();
	// 		checkStatus();
	// 		jQuery('.temperament-finish-btn').removeClass('active');
	// 		if( jQuery('.temperament-page-'+current).hasClass('pass') ) {
	// 			jQuery('.temperament-survey-container').addClass('good');
	// 			jQuery('.temperament-survey').addClass('okay');
	// 		}
	// 		else {
	// 			jQuery('.temperament-survey-container').removeClass('good');
	// 			jQuery('.temperament-survey').removeClass('okay');
	// 		}
	// 		buttonConfig();
	// 	});

	// }

	// function buildProgress(g) {

	// 	if(g > 1){
	// 		g = g - 1;
	// 	}
	// 	else if (g === 0) {
	// 		g = 1;
	// 	}
	// 	g = g * 100;
	// 	jQuery('.temperament-survey-progress-bar').css({ 'width' : g+'%' });

	// }

	function goToSlide(x) {

		return x;

	}

	function getCurrentSlide() {

		jQuery('.temperament-survey-page').each(function() {

			var item;

			item = jQuery(this);

			if( jQuery(item).hasClass('active') ) {
				x = item.data('page');
			}
			else {
				
			}

			return x;

		});

	}

	// function getButtons() {

	// 	if(current === 0) {
	// 		current = y;
	// 	}
	// 	if(current === count) {
	// 		jQuery('.temperament-next-btn').hide();
	// 	}
	// 	else if(current === 1) {
	// 		jQuery('.temperament-prev-btn').hide();
	// 	}
	// 	else {
	// 		jQuery('.temperament-next-btn').show();
	// 		jQuery('.temperament-prev-btn').show();
	// 	}

	// }

	jQuery('.temperament-survey-q li input').each(function() {

		var item;
		item = jQuery(this);

		jQuery(item).on('click', function() {
			if( jQuery('input:checked').length > 0 ) {
		    	// console.log(item.val());
		    	jQuery('label').parent().removeClass('active');
		    	item.closest( 'li' ).addClass('active');
			}
			else {
				//
			}
		});

	});

	percent = (x/count) * 100;
	jQuery('.temperament-survey-progress-bar').css({ 'width' : percent+'%' });

	function checkStatus() {
		jQuery('.temperament-survery-content .temperament-survey-item').on('click', function() {
			var item;
			item = jQuery(this);
			item.closest('.temperament-survey-page').addClass('pass');
		});
	}

	function buildStatus() {
		jQuery('.temperament-survery-content .temperament-survey-item').on('click', function() {
			var item;
			item = jQuery(this);
			item.addClass('bingo');
			item.closest('.temperament-survey-page').addClass('pass');
			jQuery('.temperament-survey-container').addClass('good');
		});
	}

	function deliverStatus() {
		jQuery('.temperament-survey-item').on('click', function() {
			if( jQuery('.temperament-survey-container').hasClass('good') ){
				jQuery('.temperament-survey').addClass('okay');
			}
			else {
				jQuery('.temperament-survey').removeClass('okay');	
			}
			buttonConfig();
		});
	}

	function lastPage() {
		if( jQuery('.temperament-next-btn').hasClass('cool') ) {
			alert('cool');
		}
	}

	function buttonConfig() {
		if( jQuery('.temperament-survey').hasClass('okay') ) {
			jQuery('.temperament-next-btn button').prop('disabled', false);
		}
		else {
			jQuery('.temperament-next-btn button').prop('disabled', true);
		}
	}

	function submitData() {
		jQuery('.temperament-finish-btn').on('click', function() {
			collectData();
			jQuery('.temperament-survey-bottom').slideUp();
			jQuery('.temperament-survey-results').slideDown();
		});
	}

	function collectData() {
		
		var map = {};
		var ax = ['0','red','mercedes','3.14','3'];
		var answer = '';
		var total = 0;
		var ttl = 0;
		var g;
		var c = 0;

		jQuery('.temperament-survey-item input:checked').each(function(index, val) {
			var item;
			var data;
			var name;
			var n;

			item = jQuery(this);
			data = item.val();
			name = item.data('item');
			n = parseInt(data);
			total += n;

			map[name] = data;

		});

		jQuery('.temperament-survey-results-container .temperament-survey-results-list').html('');

		for (i = 1; i <= count; i++) {

			var t = {};
			var m = {};
			answer += map[i] + '<br>';
			
			if( map[i] === ax[i]) {
				g = map[i];
				p = 'correct';
				c = 1;
			}
			else {
				g = map[i];
				p = 'incorrect';
				c = 0;
			}

			jQuery('.temperament-survey-results-list').append('<li class="temperament-survey-results-item '+p+'"><span class="temperament-item-number">'+i+'</span><span class="temperament-item-info">'+g+' - '+p+'</span></li>');

			m[i] = c;
			ttl += m[i];

		}

		var results;
		results = ( ( ttl / count ) * 100 ).toFixed(0);

		jQuery('.temperament-survey-results-score').html( results + '%' );

	}

	function goBack() {
		jQuery('.temperament-back-btn').on('click', function() {
			jQuery('.temperament-survey-bottom').slideDown();
			jQuery('.temperament-survey-results').slideUp();
		});
	}