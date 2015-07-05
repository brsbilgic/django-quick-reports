(function () {
    'use strict';

    angular
        .module('jrApp.layout.controllers')
        .controller('LayoutController', LayoutController);

    LayoutController.inject = ['Models'];

    function LayoutController(Models) {
        var vm = this;

        activate();
        function activate() {

            Models.all()
                .then(fnSuccess);

            function fnSuccess(data) {
                vm.models = data.data;
            }
        }
    }
})();