(function () {
    'use strict';

    angular
        .module('jrApp', [
            'jrApp.routes',
            'jrApp.config',
            'jrApp.layout',
            'jrApp.report',
            'jrApp.app'
        ])
        .run(run);

    angular
        .module('jrApp.routes', ['ui.router']);

    angular
        .module('jrApp.config', []);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();