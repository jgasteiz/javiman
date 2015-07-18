(function () {
    'use_strict';

    var bindings = document.querySelectorAll('[data-bind]');
    [].forEach.call(bindings, function(bindingEl) {
        var inputId = bindingEl.dataset.bind,
            format = bindingEl.dataset.format,
            input = document.getElementById(inputId);

        var formatText;
        if (format === 'markdown') {
            formatText = function(text) {
                bindingEl.innerHTML = marked(text);
            };
        } else {
            formatText = function(text) {
                bindingEl.innerText = text;
            };
        }

        input.addEventListener('keyup', function() {
            formatText(input.value);
        });

        formatText(input.value);
    });
})();
