(function () {
    'use_strict';

    var bindings = document.querySelectorAll('[data-bind]');
    [].forEach.call(bindings, function(bindingEl) {
        var inputId = bindingEl.dataset.bind,
            format = bindingEl.dataset.format,
            input = document.getElementById(inputId);

        var formatText;
        if (format === 'markdown') {
            format = function(text) {
                bindingEl.innerHTML = marked(text);
            };
        } else if (format === 'text') {
            format = function(text) {
                bindingEl.innerText = text;
            };
        } else if (format === 'image') {
            format = function(imageUrl) {
                bindingEl.src = imageUrl;
            };
        }

        input.addEventListener('keyup', function() {
            format(input.value);
        });

        format(input.value);
    });
})();
