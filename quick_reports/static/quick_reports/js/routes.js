(function () {
    'use strict';

    angular
        .module('jrApp.routes')
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('layout');

        $stateProvider
            .state('layout', {
                url: '/',
                controller: 'LayoutController',
                controllerAs: 'vm',
                templateUrl: '/static/quick_reports/js/layout/views/layout.html'
            })
            .state('layout.reports', {
                url: ':appLabel/:modelName/?reportSlug',
                controller: 'ReportController',
                controllerAs: 'vm',
                templateUrl: '/static/quick_reports/js/reports/views/report.html'
            })
    }
})();