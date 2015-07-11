(function () {
    'use strict';

    angular
        .module('jrApp.layout.controllers')
        .controller('LayoutController', LayoutController);

    LayoutController.inject = ['App'];

    function LayoutController(App) {
        var vm = this;

        activate();
        function activate() {

            App.all()
                .then(fnSuccess);

            function fnSuccess(data) {
                vm.apps = data.data;
            }
        }
    }
})();