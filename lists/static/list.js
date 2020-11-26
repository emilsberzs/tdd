window.Superlists = {};
window.Superlists.initialize = function () {
    $('input[name="text"]').on('keypress', function () {
        $('.form-group-has-error').hide();
    });
};
