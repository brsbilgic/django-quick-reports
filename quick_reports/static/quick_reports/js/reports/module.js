(function () {
    'use strict';

    angular
        .module('jrApp.report',[
            'jrApp.report.controllers',
            'jrApp.report.services'
        ]);

    angular
        .module('jrApp.report.controllers', ['angular-flot']);

    angular
        .module('jrApp.report.services', []);

})();