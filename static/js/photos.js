(function() {
	'use_strict';

	$('.js-photo').click(function () {
        var imgSrc = $(this).data('src'),
            $modal = $('<div>').addClass('modal'),
            $img = $('<img>').prop('src', imgSrc),
            $modalClose = $('<div>').addClass('modal__close');

        $modal.append($img);
        $modal.append($modalClose);
        $(document.body).addClass('modal--open');
        $(document.body).append($modal);

        $modal.click(function (e) {
            $(document.body).removeClass('modal--open');
            $modal.remove();
        });
        $modalClose.click(function (e) {
            $(document.body).removeClass('modal--open');
            $modal.remove();
        });
    });
})();